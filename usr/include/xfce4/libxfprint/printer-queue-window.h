/*
 * Copyright (c) 2003 Benedikt Meurer (benedikt.meurer@unix-ag.uni-siegen.de)
 *               2004 Jean-François Wauthy (pollux@xfce.org)
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

#ifndef PRINTER_QUEUE_WINDOW_H
#define PRINTER_QUEUE_WINDOW_H

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <gtk/gtk.h>

#include <libxfprint/common.h>

G_BEGIN_DECLS
#define PRINTER_QUEUE_WINDOW_TYPE         (printer_queue_window_get_type ())
#define PRINTER_QUEUE_WINDOW(o)           (G_TYPE_CHECK_INSTANCE_CAST ((o), PRINTER_QUEUE_WINDOW_TYPE, PrinterQueueWindow))
#define PRINTER_QUEUE_WINDOW_CLASS(k)     (G_TYPE_CHECK_CLASS_CAST((k), PRINTER_QUEUE_WINDOW_TYPE, PrinterQueueWindowClass))
#define IS_PRINTER_QUEUE_WINDOW(o)        (G_TYPE_CHECK_INSTANCE_TYPE ((o), PRINTER_QUEUE_WINDOW_TYPE))
#define IS_PRINTER_QUEUE_WINDOW_CLASS(k)  (G_TYPE_CHECK_CLASS_TYPE ((k), PRINTER_QUEUE_WINDOW_TYPE))
#define PRINTER_QUEUE_WINDOW_GET_CLASS(o) (G_TYPE_INSTANCE_GET_CLASS ((o), PRINTER_QUEUE_WINDOW_TYPE, PrinterQueueWindowClass))
typedef struct _PrinterQueueWindowPrivate PrinterQueueWindowPrivate;
typedef struct _PrinterQueueWindowClass PrinterQueueWindowClass;
typedef struct _PrinterQueueWindow PrinterQueueWindow;

struct _PrinterQueueWindow
{
  GtkWindow parent;

  PrinterQueueWindowPrivate *priv;
};

struct _PrinterQueueWindowClass
{
  GtkWindowClass parent_class;
};

GType printer_queue_window_get_type ();

enum
{
  JOBS_ICON_COLUMN,
  JOBS_NAME_COLUMN,
  JOBS_ID_COLUMN,
  JOBS_USER_COLUMN,
  JOBS_STATE_COLUMN,
  JOBS_SIZE_COLUMN,
  JOBS_PRIORITY_COLUMN,
  JOBS_CREATION_TIME_COLUMN,
  JOBS_PROCESSING_TIME_COLUMN,
  JOBS_N_COLUMNS
};

typedef enum
{
  PRINTER_QUEUE_WINDOW_NAME_COLUMN,
  PRINTER_QUEUE_WINDOW_ID_COLUMN,
  PRINTER_QUEUE_WINDOW_USER_COLUMN,
  PRINTER_QUEUE_WINDOW_STATE_COLUMN,
  PRINTER_QUEUE_WINDOW_SIZE_COLUMN,
  PRINTER_QUEUE_WINDOW_PRIORITY_COLUMN,
  PRINTER_QUEUE_WINDOW_CREATION_TIME_COLUMN,
  PRINTER_QUEUE_WINDOW_PROCESSING_TIME_COLUMN,
} PrinterQueueWindowColumn;

GtkWidget *printer_queue_window_new (PrintingSystem * ps, const gchar * printer);
GtkUIManager *printer_queue_window_get_ui_manager (PrinterQueueWindow * win);
void printer_queue_window_hide_column (PrinterQueueWindow * win, PrinterQueueWindowColumn column);

guint printer_queue_window_get_selected_job (PrinterQueueWindow * win);
#endif
