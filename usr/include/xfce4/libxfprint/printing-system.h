/*
 * Copyright (c) 2004-2006 Jean-François Wauthy (pollux@xfce.org)
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

#ifndef PRINTING_SYSTEM_H
#define PRINTING_SYSTEM_H

#ifdef HAVE_CONFIG_H
#include <config.h>
#endif

#include <gtk/gtk.h>
#include <libxfcegui4/libxfcegui4.h>

#include <libxfprint/common.h>
#include <libxfprint/printer.h>
#include <libxfprint/job.h>
#include <libxfprint/printer-list-window.h>
#include <libxfprint/printer-queue-window.h>

G_BEGIN_DECLS
#define PRINTING_SYSTEM_TYPE         (printing_system_get_type ())
#define PRINTING_SYSTEM(o)           (G_TYPE_CHECK_INSTANCE_CAST ((o), PRINTING_SYSTEM_TYPE, PrintingSystem))
#define PRINTING_SYSTEM_CLASS(k)     (G_TYPE_CHECK_CLASS_CAST((k), PRINTING_SYSTEM_TYPE, PrintingSystemClass))
#define IS_PRINTING_SYSTEM(o)        (G_TYPE_CHECK_INSTANCE_TYPE ((o), PRINTING_SYSTEM_TYPE))
#define IS_PRINTING_SYSTEM_CLASS(k)  (G_TYPE_CHECK_CLASS_TYPE ((k), PRINTING_SYSTEM_TYPE))
#define PRINTING_SYSTEM_GET_CLASS(o) (G_TYPE_INSTANCE_GET_CLASS ((o), PRINTING_SYSTEM_TYPE, PrintingSystemClass))
typedef struct _PrintingSystemPrivate PrintingSystemPrivate;
typedef struct _PrintingSystemClass PrintingSystemClass;

struct _PrintingSystem
{
  GObject parent;

  gchar *name;
  gchar *description;
  gchar *version;
  gchar *author;
  gchar *homepage;

  PrintingSystemPrivate *priv;
};

struct _PrintingSystemClass
{
  GObjectClass parent_class;
};

GType printing_system_get_type ();

/********/
/* Enum */
/********/
enum
{
  PRINTER_TYPE_PRINTER,
  PRINTER_TYPE_CLASS,
};

enum
{
  PRINTER_STATE_UNKNOWN,
  PRINTER_STATE_IDLE,
  PRINTER_STATE_PROCESSING,
  PRINTER_STATE_STOPPED,
};

/*************/
/* Functions */
/*************/
PrintingSystem *printing_system_new (const gchar * path);

GList *printing_system_get_printers (PrintingSystem * ps);
Printer *printing_system_get_default_printer (PrintingSystem * ps);
gint printing_system_get_printer_state (PrintingSystem * ps, const gchar * printer);
gint printing_system_get_jobs_count (PrintingSystem * ps, const gchar * printer);

gboolean printing_system_remove_job (PrintingSystem * ps, const gchar * printer, gint id);
GList *printing_system_get_jobs (PrintingSystem * ps, const gchar * printer);

gboolean printing_system_print_file (PrintingSystem * ps, const gchar * printer, const gchar * original_name,
                                     const gchar * file, gboolean remove_file);

void printing_system_customize_printer_list_window (PrintingSystem * ps, PrinterListWindow * win);
void printing_system_customize_printer_queue_window (PrintingSystem * ps, PrinterQueueWindow * win);

G_END_DECLS
#endif
