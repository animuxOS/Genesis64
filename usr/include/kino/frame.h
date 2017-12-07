/*
* frame.h -- utilities for process digital video frames
* Copyright (C) 2000 Arne Schirmacher <arne@schirmacher.de>
* Copyright (C) 2001-2007 Dan Dennedy <dan@dennedy.org>
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

#ifndef _FRAME_H
#define _FRAME_H 1

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <iostream>
using std::cerr;
using std::endl;

#include <time.h>
#include <string>
#include <stdio.h>
#include <samplerate.h>

#include "endian_types.h"
#include "playlist.h"

#ifdef HAVE_LIBDV
#include <libdv/dv.h>
#include <libdv/dv_types.h>
#else
#define DV_AUDIO_MAX_SAMPLES 1944
#endif

#if defined(HAVE_LIBAVCODEC)
extern "C"
{
#   include <avcodec.h>
#   include <avformat.h>
#ifdef HAVE_SWSCALE
#   include <swscale.h>
#endif
}
#endif

#define FRAME_MAX_WIDTH 720
#define FRAME_MAX_HEIGHT 576

typedef struct Pack
{
	/// the five bytes of a packet
	unsigned char data[ 5 ];
}
Pack;

typedef struct TimeCode
{
	int hour;
	int min;
	int sec;
	int frame;
}
TimeCode;


typedef struct AudioInfo
{
	int frames;
	int frequency;
	int samples;
	int channels;
	int quantization;
}
AudioInfo;


class VideoInfo
{
public:
	int width;
	int height;
	bool isPAL;
	TimeCode timeCode;
	struct tm	recDate;

	VideoInfo();
};


class Frame
{
public:
	unsigned char *data;
	/// the number of bytes written to the frame
	int bytesInFrame;

#if defined(HAVE_LIBAVCODEC)
	AVCodecContext *libavcodec;
#if defined(HAVE_SWSCALE)
	struct SwsContext *imgConvertRgbCtx;
	struct SwsContext *imgConvertYuvCtx;
#endif
#endif

#ifdef HAVE_LIBDV
	dv_decoder_t *decoder;
	dv_encoder_t *encoder;
#endif

	int16_t *audio_buffers[ 4 ];

public:
	Frame();
	~Frame();

	Frame& operator=( const Frame& );
	bool GetSSYBPack( int packNum, Pack &pack ) const;
	bool GetVAUXPack( int packNum, Pack &pack ) const;
	bool GetAAUXPack( int packNum, Pack &pack ) const;
	bool GetTimeCode( TimeCode &timeCode ) const;
	bool GetRecordingDate( struct tm &recDate ) const;
	std::string GetRecordingDate( void ) const;
	bool GetAudioInfo( AudioInfo &info ) const;
	bool GetVideoInfo( VideoInfo &info ) const;
	int GetFrameSize( void ) const;
	float GetFrameRate( void ) const;
	bool IsPAL( void ) const;
	bool IsNewRecording( void ) const;
	bool IsNormalSpeed( void ) const;
	bool IsComplete( void ) const;
	int ExtractAudio( void *sound ) const;

#ifdef HAVE_LIBDV
	void SetPreferredQuality( );
	int ExtractAudio( int16_t **channels ) const;
	void ExtractHeader( void );
	void Deinterlace( uint8_t *pdst, uint8_t *psrc, int stride, int height );
	int ExtractRGB( void *rgb );
	int ExtractPreviewRGB( void *rgb );
	int ExtractYUV( void *yuv );
	int ExtractYUV420( uint8_t *yuv, uint8_t *output[ 3 ] );
	int ExtractPreviewYUV( void *yuv );
	void GetUpperField( void *image, int bpp );
	void GetLowerField( void *image, int bpp );
	bool IsWide( void ) const;
	int GetWidth();
	int GetHeight();
	bool CreateEncoder( bool isPAL, bool isWide );
	void SetRecordingDate( time_t *datetime, int frame );
	void SetTimeCode( int frame );
	bool EncodeAudio( AudioInfo &info, int16_le_t **channels );
#if BYTE_ORDER == BIG_ENDIAN
	bool EncodeAudio( AudioInfo &info, int16_ne_t **channels );
#endif
	int CalculateNumberSamples( int frequency, int iteration );
	void EncodeRGB( uint8_t *rgb );
#endif

private:
	/// flag for initializing the lookup maps once at startup
	static bool maps_initialized;
	/// lookup tables for collecting the shuffled audio data
	static int palmap_ch1[ 2000 ];
	static int palmap_ch2[ 2000 ];
	static int palmap_2ch1[ 2000 ];
	static int palmap_2ch2[ 2000 ];
	static int ntscmap_ch1[ 2000 ];
	static int ntscmap_ch2[ 2000 ];
	static int ntscmap_2ch1[ 2000 ];
	static int ntscmap_2ch2[ 2000 ];
	static short compmap[ 4096 ];
};

typedef enum {
    AUDIO_RESAMPLE_SRC_SINC_BEST_QUALITY = 0,
    AUDIO_RESAMPLE_SRC_SINC_MEDIUM_QUALITY = 1,
    AUDIO_RESAMPLE_SRC_SINC_FASTEST = 2,
    AUDIO_RESAMPLE_SRC_ZERO_ORDER_HOLD = 3,
    AUDIO_RESAMPLE_SRC_LINEAR = 4,
    AUDIO_RESAMPLE_INTERNAL = 5
}
AudioResampleType;

#define BUFFER_LEN 20480

template <class input_t, class output_t> class AudioResample
{
protected:
	double output_rate;
	input_t input[ BUFFER_LEN ];
	int m_silentFrameCount;

public:
	AudioResample( double rate ) : output_rate( rate ), m_silentFrameCount(0)
	{ }
	virtual ~AudioResample()
	{ }
	virtual void Resample( input_t *samples, double input_rate, int channels, int samples_this_frame )
	{ }
	void Resample( Frame &frame )
	{
		//  cerr << "Resample -----------------" << endl;
		if ( output_rate != 0 )
		{
			if ( frame.ExtractAudio( input ) == 0 )
			{
				size = frame.CalculateNumberSamples( int(output_rate), m_silentFrameCount++ );
				size *= 2 * sizeof(output_t);
				memset( output, 0, size );
				return;
			}

			AudioInfo info;
			frame.GetAudioInfo( info );
			/*
			cerr << "Audio info: "
			     << "  dec-..->frequency: "
			     << info.frequency
			     << "  samples: "
			     << info.samples << endl;
 			*/
			if ( info.frequency && output_rate != info.frequency )
			{
				Resample( input,
					  info.frequency,
					  info.channels,
					  info.samples );
			}
			else
			{
				for (int i=0; i<info.channels*info.samples; i++)
					output[i] = input[i];

				size = info.channels*info.samples*sizeof(output_t);
			}
		}
		else
		{
			size = 0;
		}
		// cerr << "size: " << size << endl;
	}
	void SetOutputFrequency( double output_rate )
	{
		this->output_rate = output_rate;
	}
	int GetOutputFrequency( )
	{
		return this->output_rate;
	}

	output_t output[ BUFFER_LEN ];
	int size;
};

template <class input_t, class output_t> class InternalAudioResample : public AudioResample<input_t, output_t>
{
public:
	InternalAudioResample( ) : AudioResample<input_t,output_t>( 0 )
	{ }
	InternalAudioResample( double output_rate ) : AudioResample<input_t,output_t>( output_rate )
	{ }
	virtual ~InternalAudioResample()
	{ }
	/** Simple up and down resampler for people unable to handle 48khz
	    audio. Also fixes mixed projects with 32khz and 48khz audio
	    sampling (yippee!).  
	*/
	void Resample( input_t *input, double input_rate, int channels, int samples )
	{
		float ratio = ( float ) this->output_rate / ( float ) input_rate;
		this->size = ( int ) ( ( float ) samples * ratio );

		int rounding = 1 << 15;
		unsigned int xfactor = ( samples << 16 ) / this->size;
		unsigned int xmax = xfactor * this->size;
		unsigned int i = 0;
		unsigned int o = 0;
		this->size *= sizeof(output_t) * channels;

		for ( unsigned int xft = 0; xft < xmax; xft += xfactor )
		{
			i = ( ( xft + rounding ) >> 16 ) * channels;
			for (int c=0; c < channels; c++)
				this->output[o+c] = input[i+c];
			o += channels;
		}

	}
};

template <class input_t, class output_t> class SrcAudioResample : public AudioResample<input_t, output_t>
{
public:
	SrcAudioResample( int converter ) : AudioResample<input_t,output_t>( 0 )
	{
		SrcAudioResample( converter, 0 );
	}
	SrcAudioResample( int converter, double output_rate, bool isStreaming ) :
		AudioResample<input_t,output_t>( output_rate )
	{
		int srcError = 0;

		state = src_new( converter, 2, &srcError );
		if ( srcError != 0 )
		{
			cerr << "SRC: " << src_strerror( srcError ) << endl;
		}
		else
		{
			data.data_in = input_buffer;
			data.data_out = output_buffer;
			data.end_of_input = isStreaming ? 0 : 1;
		}
	}
	virtual ~SrcAudioResample()
	{
		src_delete( state );
	}
	void Resample( input_t *input, double input_rate, int channels, int samples )
	{
		for ( int i = 0; i < samples * channels; ++i )
			input_buffer[ i ] = ( float ) input[ i ] / 32768.0;

		// Setup resampler
		data.input_frames = samples;
		data.output_frames = BUFFER_LEN / channels;
		data.src_ratio = this->output_rate / input_rate;

		// Resample
		int result = src_process ( state, &data );
		if ( result != 0 )
			cerr << "SRC: " << src_strerror( result ) << endl;
		this->size = data.output_frames_gen * channels * sizeof(output_t);

// cerr << "Resample in samples " << samples << " out rate " << this->output_rate << " in rate " << input_rate << " src_ratio " << data.src_ratio << "out samples " << this->size/4 << endl;

		for ( int i = 0; i < data.output_frames_gen * channels; ++i )
		{
			float sample = output_buffer[ i ];
			if ( sample > 1.0 )
				sample = 1.0;
			if ( sample < -1.0 )
				sample = -1.0;
			if ( sample >= 0 )
				this->output[ i ] = ( long int )( 32767.0 * sample );
			else
				this->output[ i ] = ( long int )( 32768.0 * sample );
		}
	}

private:
	SRC_STATE *state;
	SRC_DATA data;
	float input_buffer[ BUFFER_LEN ];
	float output_buffer[ BUFFER_LEN ];
};

template <class input_t, class output_t> class AudioResampleFactory
{
public:
	static AudioResample<input_t, output_t> *createAudioResample( AudioResampleType type, 
		double output_rate = 0, bool isStreaming = true )
	{
		switch ( type )
		{
		case AUDIO_RESAMPLE_SRC_SINC_BEST_QUALITY:
			return new SrcAudioResample<input_t, output_t>( SRC_SINC_BEST_QUALITY, output_rate, isStreaming );
		case AUDIO_RESAMPLE_SRC_SINC_MEDIUM_QUALITY:
			return new SrcAudioResample<input_t, output_t>( SRC_SINC_MEDIUM_QUALITY, output_rate, isStreaming );
		case AUDIO_RESAMPLE_SRC_SINC_FASTEST:
			return new SrcAudioResample<input_t, output_t>( SRC_SINC_FASTEST, output_rate, isStreaming );
		case AUDIO_RESAMPLE_SRC_ZERO_ORDER_HOLD:
			return new SrcAudioResample<input_t, output_t>( SRC_ZERO_ORDER_HOLD, output_rate, isStreaming );
		case AUDIO_RESAMPLE_SRC_LINEAR:
			return new SrcAudioResample<input_t, output_t>( SRC_LINEAR, output_rate, isStreaming );
		default:
			return new InternalAudioResample<input_t, output_t>( output_rate );
		}
	}
};


class FramePool
{
public:
	virtual ~FramePool()
	{ }
	virtual Frame *GetFrame( ) = 0;
	virtual void DoneWithFrame( Frame * ) = 0;
};

extern FramePool *GetFramePool( );


/// The asynchronous resampler is by export to prooduce locked audio.
/// The reading of frames is asynchronous with the reading of audio samples
/// from the resampler. Therefore, the reading of the samples out of the resampler
/// can follow a locked audio sequence. It conforms the incoming audio to a designated
/// frequency, and it applies another resampling ratio on the output side. The idea
/// with the output resampling is that you can request a sample rate with some
/// differential applied in order to coerce it into producing an intended number
/// of samples--i.e., locked audio.
template <class input_t, class output_t> class AsyncAudioResample
{
private:
	SRC_STATE* m_state;
	PlayList* m_playlist;
	int m_position;
	int m_every;
	input_t m_input[BUFFER_LEN];
	float m_internalInput[BUFFER_LEN];
	float m_internalConformed[BUFFER_LEN];
	float m_internalOutput[BUFFER_LEN];
	output_t m_output[BUFFER_LEN];
	int m_error;
	Frame& m_frame;
	double m_rate;
	SRC_STATE* m_conformer;
	SRC_DATA m_srcdata;
	AudioInfo m_info;
	int m_channels;
	int m_end;
	int m_silentFrameCount;

public:
	AsyncAudioResample( AudioResampleType type, PlayList *playlist, 
			double rate, int begin, int end, int every ) :
		m_playlist( playlist ),
		m_position( begin ),
		m_every( every ),
		m_error( 0 ),
		m_frame( *GetFramePool()->GetFrame() ),
		m_rate( rate ),
		m_conformer( 0 ),
		m_channels( 2 ),
		m_end( end ),
		m_silentFrameCount( 0 )
	{
		int src_type;
		switch ( type )
		{
		case AUDIO_RESAMPLE_SRC_SINC_BEST_QUALITY:
			src_type = SRC_SINC_BEST_QUALITY;
		case AUDIO_RESAMPLE_SRC_SINC_MEDIUM_QUALITY:
			src_type = SRC_SINC_MEDIUM_QUALITY;
		case AUDIO_RESAMPLE_SRC_SINC_FASTEST:
			src_type = SRC_SINC_FASTEST;
		case AUDIO_RESAMPLE_SRC_ZERO_ORDER_HOLD:
			src_type = SRC_ZERO_ORDER_HOLD;
		case AUDIO_RESAMPLE_SRC_LINEAR:
			src_type = SRC_LINEAR;
		default:
			src_type = SRC_SINC_FASTEST;
		}
		m_state = src_callback_new( AsyncAudioResample::callback, src_type, m_channels, &m_error, this );
		if ( m_error == 0 )
		{
			m_conformer = src_new( src_type, m_channels, &m_error );
			if ( m_error == 0 )
			{
				m_srcdata.data_in = m_internalInput;
				m_srcdata.data_out = m_internalConformed;
				m_srcdata.output_frames = BUFFER_LEN / m_channels;
			}
		}
	}

	~AsyncAudioResample()
	{
		GetFramePool()->DoneWithFrame( &m_frame );
		if ( m_state )
			src_delete( m_state );
		if ( m_conformer )
			src_delete( m_conformer );
	}

	bool IsError() const
	{
		return m_error || (m_state && src_error( m_state )) || (m_conformer && src_error( m_conformer ));
	}

	std::string GetError() const
	{
		if ( src_error( m_state ) )
			return src_strerror( src_error( m_state ) );
		else if ( src_error( m_conformer ) )
			return src_strerror( src_error( m_conformer ) );
		else
			return src_strerror( m_error );
	}

	long ReadAudio( float **data )
	{
// cerr << "AsyncAudioResample::ReadAudio" << endl;
		long output_frames = 0;
		if ( m_position <= m_end )
		{
			if ( m_playlist->GetFrame( m_position, m_frame ) )
			{
				int n = m_frame.ExtractAudio( m_input ) / m_channels / sizeof(input_t);
// cerr << "AsyncAudioResample::ReadAudio position " << m_position << " input samples " << n << endl;
				*data = m_internalConformed;
				if ( n == 0 )
				{
					output_frames = m_frame.CalculateNumberSamples( int(m_rate), m_silentFrameCount++ );
					memset( m_internalConformed, 0, sizeof( m_internalConformed ) );
				}
				else
				{
					m_frame.GetAudioInfo( m_info );
					if ( m_rate != m_info.frequency )
					{
						for ( int i = 0; i < n * m_channels; ++i )
							m_internalInput[ i ] = ( float ) m_input[ i ] / 32768.0;
						m_srcdata.input_frames = n;
						m_srcdata.src_ratio = m_rate / m_info.frequency;
						m_srcdata.end_of_input = (m_position > m_end );
						src_process( m_conformer, &m_srcdata );
						output_frames = m_srcdata.output_frames_gen;
					}
					else
					{
						for ( int i = 0; i < n * m_channels; ++i )
							m_internalConformed[ i ] = ( float ) m_input[ i ] / 32768.0;
						output_frames = n;
					}
				}
			}
			m_position += m_every;
		}

		return output_frames;
	}

	static long callback(void *cb_data, float **data)
	{
		AsyncAudioResample<input_t,output_t>* p = static_cast< AsyncAudioResample<input_t,output_t>* >( cb_data );
		return p->ReadAudio( data );
	}

	int Process( double rate, int samples )
	{
		int out_samples = src_callback_read( m_state, rate / m_rate, samples, m_internalOutput );
// cerr << "AsyncAudioResample::Process rate " << rate << " req samples " << samples << " out samples " << out_samples << endl;
		for ( int i = 0; i < out_samples * m_channels; ++i )
		{
			float sample = m_internalOutput[ i ];
			if ( sample > 1.0 )
				sample = 1.0;
			if ( sample < -1.0 )
				sample = -1.0;
			if ( sample >= 0 )
				m_output[ i ] = ( long int )( 32767.0 * sample );
			else
				m_output[ i ] = ( long int )( 32768.0 * sample );
		}
		return out_samples;
	}

	output_t* GetOutput( void )
	{
		return m_output;
	}
};

#endif
