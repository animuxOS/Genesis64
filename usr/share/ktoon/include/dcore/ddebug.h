/***************************************************************************
 *   Copyright (C) 2005 by David Cuadrado   *
 *   krawek@gmail.com   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/

#ifndef DDEBUG_H
#define DDEBUG_H

#include <QTextStream>
#include <QColor>

/**
 * @author David Cuadrado <krawek@gmail.com>
*/

#ifdef __GNUC__
#define D_FUNCINFO dDebug() << "[" << __PRETTY_FUNCTION__ << "] ";
#define DINIT dDebug() << "[Initializing " << __FUNCTION__ << "]";
#define DEND dDebug() << "[Destroying " << __FUNCTION__ << "]";
#define FUNC_NOT_IMPLEMENTED dWarning() << __FILE__ << ":" << __LINE__ << " " << __PRETTY_FUNCTION__ << " not implemented yet";
#else
#define D_FUNCINFO
#define DINIT dDebug() << "[Initializing " << __FILE__ << ":" << __LINE__ << "] ";
#define DEND dDebug() << "[Destroying " << __FILE__ << ":" << __LINE__ << "] ";
#define FUNC_NOT_IMPLEMENTED dWarning() << __FILE__<<":"<<__LINE__ << " not implemented yet";
#endif

#define SHOW_VAR(arg) dDebug() << #arg << " = " << arg;

class QPalette;

class QWidget;
class QDateTime;
class QDate;
class QTime;
class QPoint;
class QPointF;
class QSize;
class QRect;
class QRegion;
class QStringList;
class QColor;
class QPen;
class QBrush;
class QVariant;
class QPixmap;
class QIcon;
class QImage;

class QLinearGradient;
class QRadialGradient;
class QConicalGradient;
class QGradient;

template <class T> class QList;

enum DebugType
{
	DDebugMsg = 0,
	DWarningMsg,
	DErrorMsg,
	DFatalMsg 
};

#if !defined(D_NODEBUG)
class Q_DECL_EXPORT DDebug
{
	public:
		class Streamer : public QObject
		{
			public:
				Streamer() : space(true) {}
				~Streamer() {};
				QString buffer;
				bool space;
				Streamer & operator<< ( QChar c )
				{
					buffer += c;
					return *this;
				}
				Streamer & operator<< ( signed short i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( float f )
				{
					buffer += QString::number(f);
					return *this;
				}
				Streamer & operator<< ( const QString & string )
				{
					buffer += string;
					return *this;
				}
				Streamer & operator<< ( char c )
				{
					buffer += c;
					return *this;
				}
				Streamer & operator<< ( unsigned short i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( signed int i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( unsigned int i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( signed long i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( unsigned long i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( qlonglong i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( qulonglong i )
				{
					buffer += QString::number(i);
					return *this;
				}
				Streamer & operator<< ( double f )
				{
					buffer += QString::number(f);
					return *this;
				}
				Streamer & operator<< ( const QByteArray & array )
				{
					buffer += array.data();
					return *this;
				}
				Streamer & operator<< ( const char * string )
				{
					buffer += string;
					return *this;
				}
				Streamer & operator<< ( const void * ptr )
				{
					if ( !ptr )
					{
						buffer += "[Null pointer]";
					}
					return *this;
				}
		} *streamer;
		
		
		DDebug(DebugType t);
		DDebug(const DDebug &);
		~DDebug();
		
		void resaltWidget(QWidget *w, const QColor &color = QColor(Qt::magenta));
		
		inline DDebug &operator<<(QTextStreamManipulator /*m*/)
		{ 
// 			streamer->ts << m; 
			return *this; 
		}
		
		inline DDebug &operator<<(QTextStreamFunction /*f*/)
		{
// 			streamer->ts << f;
			return *this;
		}
		
		inline DDebug& operator << (const QString &str)
		{
			*streamer << "\"" << str << "\"";
			return *this;
		};
		
		inline DDebug& operator << (char c)
		{
			*streamer << "\'" << c << "\'";
			return *this;
		};
		
		inline DDebug &operator<<(bool t) 
		{ 
			*streamer << (t ? "true" : "false"); 
			return *this; 
		}

		inline DDebug &operator<<(signed short t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(unsigned short t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(signed int t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(unsigned int t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(signed long t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(unsigned long t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(float t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(double t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		inline DDebug &operator<<(const char* t) 
		{ 
			*streamer << t; 
			return *this; 
		}
		DDebug& operator<<( const QPixmap& p );
		DDebug& operator<<( const QIcon& p );
		DDebug& operator<<( const QImage& p ) ;
		DDebug& operator<<( const QDateTime& );
		DDebug& operator<<( const QDate&     );
		DDebug& operator<<( const QTime&     );
		DDebug& operator<<( const QPoint & ) ;
		DDebug& operator<<( const QPointF & ) ;
		DDebug& operator<<( const QSize & ) ;
		DDebug& operator<<( const QRect & ) ;
		DDebug& operator<<( const QRegion & );
		DDebug& operator<<( const QStringList & );
		DDebug& operator<<( const QColor & );
		DDebug& operator<<( const QPen & );
		DDebug& operator<<( const QBrush & );
		DDebug& operator<<( const QVariant & );
		DDebug& operator << (const QWidget*);
		DDebug& operator << (const QEvent*);
		
		DDebug& operator << (const QLinearGradient &);
		DDebug& operator << (const QRadialGradient &);
		DDebug& operator << (const QConicalGradient &);
		DDebug& operator << (const QGradient *);
		
		
		template <class T> DDebug& operator << ( const QList<T> &list );
		
	private slots:
		void write();
		
	private:
		DebugType m_type;
		QString m_toWrite;
};

template <class T> DDebug &DDebug::operator<<( const QList<T> &list )
{
	*this << "(";
	typename QList<T>::ConstIterator it = list.begin();
	if ( !list.isEmpty() ) 
	{
		*this << *it++;
	}
	for ( ; it != list.end(); ++it ) 
	{
		*this << "," << *it;
	}
	*this << ")";
	return *this;
}

// Global functions
inline DDebug dDebug()
{
	return DDebug(DDebugMsg);
}

inline DDebug dFatal()
{
	return DDebug(DFatalMsg);
}

inline DDebug dError()
{
	return DDebug(DErrorMsg);
}

inline DDebug dWarning()
{
	return DDebug(DWarningMsg);
}

#else // D_NODEBUG

class DNDebug
{
	public:
		inline DNDebug(){}
		inline DNDebug(const DNDebug &){}
		inline ~DNDebug(){}
		inline DNDebug &operator<<(QTextStreamFunction) { return *this; }
		inline DNDebug &operator<<(QTextStreamManipulator) { return *this; }
		inline DNDebug &space() { return *this; }
		inline DNDebug &nospace() { return *this; }
		inline DNDebug &maybeSpace() { return *this; }
		template<typename T> inline DNDebug &operator<<(const T &) { return *this; }
		void resaltWidget(QWidget */*w*/, const QColor &/*color*/ = QColor(Qt::magenta))
		{
		}
};

inline DNDebug dDebug()
{
	return DNDebug();
}

#define dFatal dDebug
#define dError dDebug
#define dWarning dDebug

#endif // D_NODEBUG

#endif
