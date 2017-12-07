/***************************************************************************
 *   Copyright (C) 2006 by David Cuadrado                                  *
 *   krawek@gmail.com                                                      *
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

#ifndef SPELLER_H
#define SPELLER_H

#include <QObject>

#include <QStringList>
#include <QString>

#include "spellinterface.h"

/**
 * @author David Cuadrado <krawek@gmail.com>
*/
class Q_DECL_EXPORT Speller : public QObject
{
	Q_OBJECT;
	public:
		Speller(QObject *parent = 0);
		~Speller();
		
		bool checkWord(const QString &word);
		QStringList suggestions(const QString &word);
		
	private:
		QString removeExtraCharacters(const QString &str);
		
	private:
		SpellInterface *m_speller;
};

#endif
