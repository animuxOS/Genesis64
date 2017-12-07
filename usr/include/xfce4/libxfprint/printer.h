#ifndef PRINTER_LIBXFPRINT_H
#define PRINTER_LIBXFPRINT_H

#include <glib.h>

typedef struct _Printer Printer;

struct _Printer
{
  gint type;
  gchar *name;
  gchar *alias;
};


void printer_free (Printer * printer);
void printers_free (GList * printers);

Printer *printer_lookup_byname (GList * list, const gchar * name);
Printer *printer_lookup_byalias (GList * list, const gchar * alias);

#endif
