/*
 * Copyright (c) 2006 Jean-François Wauthy (pollux@xfce.org)
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Library General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */
#ifndef PRINTER_LIST_WINDOW_H
#define PRINTER_LIST_WINDOW_H

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <gtk/gtk.h>

#include <libxfprint/common.h>

G_BEGIN_DECLS
#define PRINTER_LIST_WINDOW_TYPE         (printer_list_window_get_type ())
#define PRINTER_LIST_WINDOW(o)           (G_TYPE_CHECK_INSTANCE_CAST ((o), PRINTER_LIST_WINDOW_TYPE, PrinterListWindow))
#define PRINTER_LIST_WINDOW_CLASS(k)     (G_TYPE_CHECK_CLASS_CAST((k), PRINTER_LIST_WINDOW_TYPE, PrinterListWindowClass))
#define IS_PRINTER_LIST_WINDOW(o)        (G_TYPE_CHECK_INSTANCE_TYPE ((o), PRINTER_LIST_WINDOW_TYPE))
#define IS_PRINTER_LIST_WINDOW_CLASS(k)  (G_TYPE_CHECK_CLASS_TYPE ((k), PRINTER_LIST_WINDOW_TYPE))
#define PRINTER_LIST_WINDOW_GET_CLASS(o) (G_TYPE_INSTANCE_GET_CLASS ((o), PRINTER_LIST_WINDOW_TYPE, PrinterListWindowClass))
typedef struct _PrinterListWindowPrivate PrinterListWindowPrivate;
typedef struct _PrinterListWindowClass PrinterListWindowClass;
typedef struct _PrinterListWindow PrinterListWindow;

struct _PrinterListWindow
{
  GtkWindow parent;

  PrinterListWindowPrivate *priv;
};

struct _PrinterListWindowClass
{
  GtkWindowClass parent_class;
};

enum
{
  PRINTERS_ICON_COLUMN,
  PRINTERS_ALIAS_COLUMN,
  PRINTERS_NAME_COLUMN,
  PRINTERS_STATE_COLUMN,
  PRINTERS_JOBS_COLUMN,
  PRINTERS_N_COLUMNS
};

typedef enum
{
  PRINTER_LIST_WINDOW_ALIAS_COLUMN,
  PRINTER_LIST_WINDOW_STATE_COLUMN,
} PrinterListWindowColumn;

GType printer_list_window_get_type ();

/*************/
/* Functions */
/*************/
GtkWidget *printer_list_window_new (PrintingSystem * ps);
GtkUIManager *printer_list_window_get_ui_manager (PrinterListWindow * win);

gchar *printer_list_window_get_selected_printer (PrinterListWindow * win);
void printer_list_window_hide_column (PrinterListWindow * win, PrinterListWindowColumn column);

G_END_DECLS
#endif /*PRINTER_LIST_WINDOW_H */
