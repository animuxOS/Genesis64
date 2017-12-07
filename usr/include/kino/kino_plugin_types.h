/*
 * kino_plugin_types.h -- Helper Types for Plugins
 * Copyright (C) 2002-2007 Timothy M. Shead <tshead@k-3d.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

#ifndef KINO_PLUGIN_TYPES_H
#define KINO_PLUGIN_TYPES_H

#include "kino_plugin_utility.h"

#include <algorithm>
#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <stdint.h>

namespace kino
{

// forward class declarations
template<typename, typename>
class basic_luma;

template<typename, typename>
class basic_rgb;

template<typename, typename>
class basic_rgba;

class basic_hsv;

/// Defines data measured in pixels
typedef unsigned long pixel_size_type;

/// Enumerates input video interlace requirements for a plugin
typedef enum
{
	INTERLACE_ALLOWED,
	INTERLACE_NOT_ALLOWED,
} interlace_requirement_type;

/// Enumerates the interlace possibilities for a video stream - none, even field dominant, or odd field dominant
typedef enum
{
	NOT_INTERLACED,
	EVEN_FIELD_DOMINANT,
	ODD_FIELD_DOMINANT
} interlace_type;

/// Defines a universally-unique plugin type identifier (compatible with libuuid)
typedef uint8_t uuid_type[16];

////////////////////////////////////////////////////////////////////////
// color_traits

/// Describes traits of a type used as a sample within a color specification
template<typename SampleType>
class color_traits
{
public:
	typedef SampleType sample_type;

	/// Returns the maximum value of a sample
	static sample_type minimum();
	/// Returns the minimum value of a sample
	static sample_type maximum();
	/// Returns the sample value corresponding to transparent alpha
	static sample_type transparent() { return minimum(); }
	/// Returns the sample value corresponding to opaque alpha
	static sample_type opaque() { return maximum(); }
	/// Inverts the value of a sample
	static sample_type invert(const sample_type& Sample);
};

////////////////////////////////////////////////////////////////////////
// color_traits<unsigned char>

/// Specialization of color_traits for uint8_t samples
template<>
class color_traits<uint8_t>
{
public:
	/// Defines the sample type for this specialization
	typedef uint8_t sample_type;

	/// Returns the minimum value of a sample
	static sample_type minimum() { return 0; }
	/// Returns the maximum value of a sample
	static sample_type maximum() { return 255; }
	/// Returns the sample value corresponding to transparent alpha
	static sample_type transparent() { return minimum(); }
	/// Returns the sample value corresponding to opaque alpha
	static sample_type opaque() { return maximum(); }
	/// Inverts the value of a sample
	static sample_type invert(const sample_type& Sample) { return maximum() - Sample; }

	/// Converts a sample from a uint8_t
	static sample_type convert(const sample_type Sample) { return Sample; }
	/// Converts a sample from a double
	static sample_type convert(const double Sample) { return static_cast<uint8_t>(clamp(Sample, 0.0, 1.0) * maximum()); }
};

////////////////////////////////////////////////////////////////////////
// color_traits<double>

/// Specialization of color_traits for double samples
template<>
class color_traits<double>
{
public:
	/// Defines the sample type for this specialization
	typedef double sample_type;

	/// Returns the minimum value of a sample
	static sample_type minimum() { return 0; }
	/// Returns the maximum value of a sample
	static sample_type maximum() { return 1; }
	/// Returns the sample value corresponding to transparent alpha
	static sample_type transparent() { return minimum(); }
	/// Returns the sample value corresponding to opaque alpha
	static sample_type opaque() { return maximum(); }
	/// Inverts the value of a sample
	static sample_type invert(const sample_type& Sample) { return maximum() - Sample; }

	/// Converts a sample from a uint8_t
	static sample_type convert(const uint8_t Sample) { return static_cast<sample_type>(Sample) / 255.0; }
	/// Converts a sample from a double
	static sample_type convert(const sample_type Sample) { return Sample; }
};

////////////////////////////////////////////////////////////////////////
// basic_hsv

/// Encapsulates storage for an HSV color sample
class basic_hsv
{
public:
	typedef double sample_type;
	typedef color_traits<sample_type> sample_traits;
	typedef basic_hsv this_type;
	
	/// Default constructor sets all samples to zero
	basic_hsv() :
		hue(sample_traits::minimum()),
		saturation(sample_traits::minimum()),
		value(sample_traits::minimum())
	{
	}
	
	/// Constructor that takes hue, saturation, and value samples
	basic_hsv(const sample_type Hue, const sample_type Saturation, const sample_type Value) :
		hue(Hue),
		saturation(Saturation),
		value(Value)
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_hsv(const basic_luma<ForeignType, ForeignTraits>& RHS) :
		hue(sample_traits::minimum()),
		saturation(sample_traits::minimum()),
		value(sample_traits::convert(RHS.luma))
	{
	}

	template<typename ForeignType>
	basic_hsv(const ForeignType& RHS)
	{
		const sample_type red = sample_traits::convert(RHS.red);
		const sample_type green = sample_traits::convert(RHS.green);
		const sample_type blue = sample_traits::convert(RHS.blue);
		
		const sample_type maxcomponent = std::max(std::max(red, green), blue);
		const sample_type mincomponent = std::min(std::min(red, green), blue);
		const sample_type difference = maxcomponent - mincomponent;

		value = maxcomponent;

		saturation = maxcomponent ? difference / maxcomponent : sample_traits::minimum();

		if(saturation != sample_traits::minimum())
			{
				const sample_type reddistance = (maxcomponent - red) / difference;
				const sample_type greendistance = (maxcomponent - green) / difference;
				const sample_type bluedistance = (maxcomponent - blue) / difference;

				if (RHS.red == std::max(std::max(RHS.red, RHS.green), RHS.blue))
					{
						hue = bluedistance - greendistance;
					}
				else if (RHS.green == std::max(std::max(RHS.red, RHS.green), RHS.blue))
					{
						hue = 2 + reddistance - bluedistance;
					}
				else
					{
						hue = 4 + greendistance - reddistance;
					}

				hue *= 60;
				while(hue < 0)
					hue += 360;
				while(hue >= 360)
					hue -= 360;
			}
		else
			{
				hue = sample_traits::minimum();
			}
	}

	/// Serialization
	friend std::ostream& operator<<(std::ostream& Stream, const basic_hsv& RHS)
	{
		Stream << RHS.hue << " " << RHS.saturation << " " << RHS.value;
		return Stream;
	}

	/// Deserialization
	friend std::istream& operator>>(std::istream& Stream, basic_hsv& RHS)
	{
		Stream >> RHS.hue >> RHS.saturation >> RHS.value;
		return Stream;
	}

	sample_type hue;
	sample_type saturation;
	sample_type value;
};

////////////////////////////////////////////////////////////////////////
// basic_luma

/// Encapsulates storage for a luma color sample
template<typename SampleType, typename SampleTraits = color_traits<SampleType> >
class basic_luma
{
public:
	typedef SampleType sample_type;
	typedef SampleTraits sample_traits;
	typedef basic_luma<sample_type, sample_traits> this_type;
	
	/// Default constructor sets all samples to zero
	basic_luma() :
		luma(sample_traits::minimum()),
		alpha(sample_traits::opaque())
	{
	}

	/// Straightforward constructor that initializes samples	
	basic_luma(const sample_type Luma) :
		luma(Luma)
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_luma(const basic_luma<ForeignType, ForeignTraits>& RHS) :
		luma(sample_traits::convert(RHS.luma))
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_luma(const basic_rgb<ForeignType, ForeignTraits>& RHS) :
		luma(sample_traits::convert(std::max(RHS.red, std::max(RHS.green, RHS.blue))))
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_luma(const basic_rgba<ForeignType, ForeignTraits>& RHS) :
		luma(sample_traits::convert(std::max(RHS.red, std::max(RHS.green, RHS.blue))))
	{
	}
	
	basic_luma(const basic_hsv& RHS) :
		luma(sample_traits::convert(RHS.value))
	{
	}

	/// Serialization
	friend std::ostream& operator<<(std::ostream& Stream, const basic_luma<sample_type, sample_traits>& RHS)
	{
		Stream << RHS.luma;
		return Stream;
	}

	/// Deserialization
	friend std::istream& operator>>(std::istream& Stream, basic_luma<sample_type, sample_traits>& RHS)
	{
		Stream >> RHS.luma;
		return Stream;
	}

	sample_type luma;
	sample_type alpha;
};

////////////////////////////////////////////////////////////////////////
// basic_rgb

/// Encapsulates storage for an RGB color sample
template<typename SampleType, typename SampleTraits = color_traits<SampleType> >
class basic_rgb
{
public:
	typedef SampleType sample_type;
	typedef SampleTraits sample_traits;
	typedef basic_rgb<sample_type, sample_traits> this_type;
	
	/// Default constructor sets all samples to zero
	basic_rgb() :
		red(sample_traits::minimum()),
		green(sample_traits::minimum()),
		blue(sample_traits::minimum())
	{
	}
	
	/// Constructor that takes red, green, and blue samples
	basic_rgb(const sample_type Red, const sample_type Green, const sample_type Blue) :
		red(Red),
		green(Green),
		blue(Blue)
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgb(const basic_luma<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.luma)),
		green(sample_traits::convert(RHS.luma)),
		blue(sample_traits::convert(RHS.luma))
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgb(const basic_rgb<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.red)),
		green(sample_traits::convert(RHS.green)),
		blue(sample_traits::convert(RHS.blue))
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgb(const basic_rgba<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.red)),
		green(sample_traits::convert(RHS.green)),
		blue(sample_traits::convert(RHS.blue))
	{
	}

	basic_rgb(const basic_hsv& RHS)
	{
		// Easiest case - saturation is zero
		if(0 == RHS.saturation)
			{
				red = green = blue = sample_traits::convert(RHS.value);
				return;
			}
			
		const double h = RHS.hue / 60;
		const double i = floor(h);
		const double f = h - i;
		const double p = RHS.value * (1 - RHS.saturation);
		const double q = RHS.value * (1 - (RHS.saturation * f));
		const double t = RHS.value * (1 - (RHS.saturation * (1 - f)));

		if(0.0 == i)
			{
				red = sample_traits::convert(RHS.value);
				green = sample_traits::convert(t);
				blue = sample_traits::convert(p);
			}
		else if(1.0 == i)
			{
				red = sample_traits::convert(q);
				green = sample_traits::convert(RHS.value);
				blue = sample_traits::convert(p);
			}
		else if(2.0 == i)
			{
				red = sample_traits::convert(p);
				green = sample_traits::convert(RHS.value);
				blue = sample_traits::convert(t);
			}
		else if(3.0 == i)
			{
				red = sample_traits::convert(p);
				green = sample_traits::convert(q);
				blue = sample_traits::convert(RHS.value);
			}
		else if(4.0 == i)
			{
				red = sample_traits::convert(t);
				green = sample_traits::convert(p);
				blue = sample_traits::convert(RHS.value);
			}
		else if(5.0 == i)
			{
				red = sample_traits::convert(RHS.value);
				green = sample_traits::convert(p);
				blue = sample_traits::convert(q);
			}
	}

	/// Serialization
	friend std::ostream& operator<<(std::ostream& Stream, const basic_rgb<sample_type, sample_traits>& RHS)
	{
		Stream << RHS.red << " " << RHS.green << " " << RHS.blue;
		return Stream;
	}

	/// Deserialization
	friend std::istream& operator>>(std::istream& Stream, basic_rgb<sample_type, sample_traits>& RHS)
	{
		Stream >> RHS.red >> RHS.green >> RHS.blue;
		return Stream;
	}

	sample_type red;
	sample_type green;
	sample_type blue;
};

////////////////////////////////////////////////////////////////////////
// basic_rgba

/// Encapsulates storage for an RGBA color sample
template<typename SampleType, typename SampleTraits = color_traits<SampleType> >
class basic_rgba
{
public:
	typedef SampleType sample_type;
	typedef SampleTraits sample_traits;
	typedef basic_rgba<sample_type, sample_traits> this_type;
	
	/// Default constructor sets all samples to zero
	basic_rgba() :
		red(sample_traits::minimum()),
		green(sample_traits::minimum()),
		blue(sample_traits::minimum()),
		alpha(sample_traits::opaque())
	{
	}
	
	/// Constructor that takes red, green, and blue samples, and sets alpha opaque
	basic_rgba(const sample_type Red, const sample_type Green, const sample_type Blue) :
		red(Red),
		green(Green),
		blue(Blue),
		alpha(sample_traits::opaque())
	{
	}
	
	/// Constructor that takes red, green, blue, and alpha samples
	basic_rgba(const sample_type Red, const sample_type Green, const sample_type Blue, const sample_type Alpha) :
		red(Red),
		green(Green),
		blue(Blue),
		alpha(Alpha)
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgba(const basic_luma<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.luma)),
		green(sample_traits::convert(RHS.luma)),
		blue(sample_traits::convert(RHS.luma)),
		alpha(sample_traits::opaque())
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgba(const basic_rgb<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.red)),
		green(sample_traits::convert(RHS.green)),
		blue(sample_traits::convert(RHS.blue)),
		alpha(sample_traits::opaque())
	{
	}

	template<typename ForeignType, typename ForeignTraits>
	basic_rgba(const basic_rgba<ForeignType, ForeignTraits>& RHS) :
		red(sample_traits::convert(RHS.red)),
		green(sample_traits::convert(RHS.green)),
		blue(sample_traits::convert(RHS.blue)),
		alpha(sample_traits::convert(RHS.alpha))
	{
	}

	/// Serialization
	friend std::ostream& operator<<(std::ostream& Stream, const basic_rgba<sample_type, sample_traits>& RHS)
	{
		Stream << RHS.red << " " << RHS.green << " " << RHS.blue << " " << RHS.alpha;
		return Stream;
	}

	/// Deserialization
	friend std::istream& operator>>(std::istream& Stream, basic_rgba<sample_type, sample_traits>& RHS)
	{
		Stream >> RHS.red >> RHS.green >> RHS.blue >> RHS.alpha;
		return Stream;
	}

	sample_type red;
	sample_type green;
	sample_type blue;
	sample_type alpha;
};

////////////////////////////////////////////////////////////////////////
// basic_bitmap

/// Encapsulates a bitmap image
template<typename PixelType>
class basic_bitmap
{
public:
	typedef PixelType pixel_type;
	typedef PixelType* iterator;
	typedef const PixelType* const_iterator;
	typedef basic_bitmap<pixel_type> this_type;

	/// Creates an empty bitmap
	basic_bitmap() :
		m_width(0),
		m_height(0),
		m_data(0)
	{
	}
	
	/// Creates a new bitmap with given width and height in pixels
	basic_bitmap(const pixel_size_type Width, const pixel_size_type Height) :
		m_width(Width),
		m_height(Height),
		m_data(static_cast<pixel_type*>(std::malloc(m_width * m_height * sizeof(pixel_type))))
	{
		// Sanity checks ...
		assert(m_width);
		assert(m_height);
		assert(m_data);
	}

	/// Creates a new bitmap, copying "old fashioned" C-style data
	basic_bitmap(void* Data, const pixel_size_type Width, const pixel_size_type Height) :
		m_width(Width),
		m_height(Height),
		m_data(static_cast<pixel_type*>(std::malloc(m_width * m_height * sizeof(pixel_type))))
	{
		// Sanity checks ...
		assert(m_width);
		assert(m_height);
		assert(m_data);
		assert(Data);
		
		memcpy(m_data, Data, m_width * m_height * sizeof(pixel_type));
	}

	/// Copy constructor for bitmaps of similar type
	basic_bitmap(this_type& RHS) :
		m_width(RHS.m_width),
		m_height(RHS.m_height),
		m_data(static_cast<pixel_type*>(std::malloc(m_width * m_height * sizeof(pixel_type))))
	{
		memcpy(m_data, RHS.m_data, m_width * m_height * sizeof(pixel_type));
	}
	/// Copy constructor for bitmaps of dissimilar type
	template<typename ForeignType>
	basic_bitmap(basic_bitmap<ForeignType>& RHS) :
		m_width(RHS.width()),
		m_height(RHS.height()),
		m_data(static_cast<pixel_type*>(std::malloc(m_width * m_height * sizeof(pixel_type))))
	{
		std::copy(RHS.data(), RHS.data() + m_width * m_height, m_data);
	}

	/// Destructor
	virtual ~basic_bitmap()
	{
		clear();
	}

	/// Returns the bitmap width in pixels
	pixel_size_type width() const
	{
		return m_width;
	}
	
	/// Returns the bitmap height in pixels
	pixel_size_type height() const
	{
		return m_height;
	}

	/// Returns the raw bitmap data array	
	const pixel_type* const data() const
	{
		return m_data;
	}

	/// Returns the raw bitmap data array
	pixel_type* const data()
	{
		return m_data;
	}

	void clear()
	{
		if(m_data)
			std::free(m_data);
		
		m_width = 0;
		m_height = 0;
		m_data = 0;
	}
	
	void reset(const pixel_size_type Width, const pixel_size_type Height)
	{
		// Sanity checks ...
		assert(Width);
		assert(Height);
	
		pixel_type* const data = static_cast<pixel_type*>(std::malloc(Width * Height * sizeof(pixel_type)));
		assert(data);
		
		clear();
		
		m_width = Width;
		m_height = Height;
		m_data = data;
	}

	iterator begin()
	{
		return m_data;
	}
	
	const_iterator begin() const
	{
		return m_data;
	}
	
	iterator end()
	{
		return m_data + (m_width * m_height);
	}
	
	const_iterator end() const
	{
		return m_data + (m_width * m_height);
	}

private:
	/// Stores the bitmap width in pixels
	pixel_size_type m_width;
	/// Stores the bitmap height in pixels
	pixel_size_type m_height;
	/// Stores the bitmap data as a 1D array of pixels
	PixelType* m_data;
};

/// We define the standard pixel passed to plugins to be RGBA data with 8-bits-per-channel
typedef basic_rgba<uint8_t> pixel;
/// We define the standard frame passed to plugins to be RGBA data with 8-bits-per-channel
typedef basic_bitmap<pixel> video_frame;

/// Defines a random-access container of video frames
class video_sequence
{
public:
	typedef video_frame* pointer;
	typedef const video_frame* const_pointer;
	typedef video_frame& reference;
	typedef const video_frame& const_reference;
	typedef video_frame value_type;
	typedef unsigned long size_type;
	typedef long difference_type;
	
	virtual size_type size() const;
	virtual bool empty() const;
	
	virtual reference operator[](size_type Offset);
	virtual const_reference operator[](size_type Offset) const;
	
	virtual reference front();
	virtual const_reference front() const;
	
	virtual reference back();
	virtual const_reference back() const;
	
	class iterator :
		public std::iterator<std::random_access_iterator_tag, value_type>
	{
	public:
	
	private:
		class implementation;
		implementation* const m_implementation;
	};
	
	class const_iterator :
		public std::iterator<std::random_access_iterator_tag, value_type>
	{
	public:
	
	private:
		class implementation;
		implementation* const m_implementation;
	};

	virtual iterator begin();
	virtual const_iterator begin() const;
	
	virtual iterator end();
	virtual const_iterator end() const;

protected:
	virtual ~video_sequence() {}
};

/// We define the standard audio data passed to plugins to be 16-bit integers
typedef uint16_t audio_sample;

/// Defines a random-access container of audio samples
class audio_sequence 
{
public:
	typedef audio_sample* pointer;
	typedef const audio_sample* const_pointer;
	typedef audio_sample& reference;
	typedef const audio_sample& const_reference;
	typedef audio_sample value_type;
	typedef unsigned long size_type;
	typedef long difference_type;

	~audio_sequence();
	
	size_type size() const;
	bool empty() const;
	
	reference operator[](size_type Offset);
	const_reference operator[](size_type Offset) const;
	
	reference front();
	const_reference front() const;
	
	reference back();
	const_reference back() const;
	
	void push_back(const_reference Value);
	
	class iterator :
		public std::iterator<std::random_access_iterator_tag, value_type>
	{
	public:
		iterator(const iterator& RHS);
		~iterator();
		
		iterator& operator=(const iterator& RHS);
		
		iterator& operator++();
		iterator operator++(int);
		
		bool operator==(const iterator& RHS) const;
		
		reference operator*() const;
	
	private:
		class implementation;
		implementation* m_implementation;

	public:
		iterator(implementation* Implementation);
		
		friend class audio_sequence;
	};
	
	class const_iterator :
		public std::iterator<std::random_access_iterator_tag, value_type>
	{
	public:
		const_iterator(const const_iterator& RHS);
		~const_iterator();
		
		const_iterator& operator=(const const_iterator& RHS);
		
		const_iterator& operator++();
		const_iterator operator++(int);
		
		bool operator==(const const_iterator& RHS) const;
		
		const reference operator*() const;
	
	private:
		class implementation;
		implementation* const m_implementation;
	
	public:
		const_iterator(implementation* Implementation);
		
		friend class audio_sequence;
	};

	iterator begin();
	const_iterator begin() const;
	
	iterator end();
	const_iterator end() const;

private:
	class implementation;
	implementation* const m_implementation;

public:
	audio_sequence(implementation* Implementation);
};

} // namespace kino

#endif // !KINO_PLUGIN_TYPES_H
