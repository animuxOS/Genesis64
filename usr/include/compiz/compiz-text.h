/*
 * text.h - adds text image support to beryl.
 * Copyright: (C) 2006 Patrick Niklaus
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 *
 */

#ifndef _COMPIZ_TEXT_H
#define _COMPIZ_TEXT_H

#define TEXT_ABIVERSION 20080421

#define TEXT_ID "TextToPixmap"

#define TEXT_STYLE_NORMAL		(1 << 0)
#define TEXT_STYLE_BOLD			(1 << 1)
#define TEXT_STYLE_ITALIC		(1 << 2)
#define TEXT_STYLE_BACKGROUND		(1 << 3)

typedef enum {
    TextRenderNormal = 0,
    TextRenderWindowTitle,
    TextRenderWindowTitleWithViewport
} TextRenderMode;

typedef struct _CompTextAttrib {
    TextRenderMode renderMode;

    void *data;

    CompScreen *screen;
    int        maxWidth;
    int        maxHeight;

    char           *family;
    int            size;
    unsigned short color[4];
    unsigned int   style;
    Bool           ellipsize;
    int            backgroundHMargin;
    int            backgroundVMargin;
    unsigned short backgroundColor[4];
} CompTextAttrib;

#endif