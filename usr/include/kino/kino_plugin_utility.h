/*
 * kino_plugin_utility.h -- Helper Utilities for Plugins
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

#ifndef KINO_PLUGIN_UTILITY_H
#define KINO_PLUGIN_UTILITY_H

#include <cassert>
#include <deque>
#include <vector>
#include <numeric>

namespace kino
{

/// Clamps the input value to the range [MinVal, MaxVal]
template<typename ArgType>
ArgType clamp(const ArgType A, const ArgType MinVal, const ArgType MaxVal)
{
        return std::min(std::max(A, MinVal), MaxVal);
}

/// Linear interpolation between two values
template<typename ArgType>
inline ArgType lerp(const ArgType A, const ArgType B, const double Mix)
{
        return static_cast<ArgType>(A * (1.0 - Mix) + B * Mix);
}

inline double step(const double Edge, const double A)
{
        return A < Edge ? 0.0 : 1.0;
}

inline double linearstep(const double Edge1, const double Edge2, const double A)
{
        if(A < Edge1)
                return 0.0;
                
        if(A >= Edge2)
                return 1.0;
                
        return (A - Edge1) / (Edge2 - Edge1);
}

inline double smoothstep(const double Edge1, const double Edge2, const double A)
{
        if(A < Edge1)
                return 0.0;
                
        if(A >= Edge2)
                return 1.0;
                
        double a = (A - Edge1) / (Edge2 - Edge1);
        
        return (a * a * (3 - 2 * a));
}

inline double pulse(const double Edge1, const double Edge2, const double A)
{
        return step(Edge1, A) - step(Edge2, A);
}

inline double factorial(const unsigned int X)
{
	double result = 1;
	
	for(unsigned int i = 2; i <= X; ++i)
		result *= i;
		
	return result;
}

/// A general-purpose one-dimensional convolve filter that operates as a finite state machine
template<typename PixelType>
class convolve_filter
{
public:
	convolve_filter() :
		m_scale(0)
	{
	}
	
	void push_weight(const double Weight)
	{
		m_weights.push_back(Weight);
		m_values.resize(m_weights.size());
		
		m_scale = std::accumulate(m_weights.begin(), m_weights.end(), 0.0);
		if(m_scale)
			m_scale = 1.0 / m_scale;
	}
	
	unsigned int width()
	{
		return m_weights.size();
	}
	
	unsigned int neighbors()
	{
		return m_weights.size() / 2;
	}
	
	unsigned int middle()
	{
		return m_weights.size() / 2;
	}
	
	void push_value(const PixelType Value)
	{
		// Sanity checks ...
		assert(m_weights.size());
		assert(m_weights.size() == m_values.size());
		
		m_values.push_back(Value);
		m_values.pop_front();
	}
	
	PixelType get_value()
	{
		PixelType result;
		
		weight_collection_type::const_iterator weight = m_weights.begin();
		for(typename value_collection_type::iterator value = m_values.begin(); value != m_values.end(); ++value, ++weight)
			{
				result.red += (value->red) * (*weight);
				result.green += (value->green) * (*weight);
				result.blue += (value->blue) * (*weight);
			}
			
		result.red *= m_scale;
		result.green *= m_scale;
		result.blue *= m_scale;
		
		return result;
	}

	PixelType get_value(const unsigned int Start, const unsigned int End)
	{
		double scale = std::accumulate(m_weights.begin() + Start, m_weights.begin() + End, 0.0);
		if(scale)
			scale = 1.0 / scale;	
	
		PixelType result;
		
		weight_collection_type::const_iterator weight = m_weights.begin() + Start;
		for(typename value_collection_type::iterator value = m_values.begin() + Start; value != m_values.begin() + End; ++value, ++weight)
			{
				result.red += (value->red) * (*weight);
				result.green += (value->green) * (*weight);
				result.blue += (value->blue) * (*weight);
			}
			
		result.red *= scale;
		result.green *= scale;
		result.blue *= scale;
		
		return result;
	}

private:
	typedef std::vector<double> weight_collection_type;
	weight_collection_type m_weights;
	
	typedef std::deque<PixelType> value_collection_type;
	value_collection_type m_values;
	
	double m_scale;
};

/// Attempts to bring Resource Acquisition Is Initialization to legacy "C" constructs
template<typename ResourceType>
class raii
{
public:
	raii(ResourceType* const Resource, void (*ReleaseMethod)(ResourceType*)) :
		m_resource(Resource),
		m_release_method(ReleaseMethod)
	{
		// Sanity checks ...
		assert(m_release_method);
	}
	
	~raii()
	{
		if(m_resource)
			(*m_release_method)(m_resource);
	}

	ResourceType* get() const
	{
		return m_resource;
	}
			
	ResourceType* operator->() const
	{
		return m_resource;
	}
	
	ResourceType& operator*() const
	{
		return *m_resource;
	}

private:
	ResourceType* const m_resource;
	void (*m_release_method)(ResourceType*);
};

} // namespace kino

#endif // !KINO_PLUGIN_UTILITY_H
