/* LIBGIMP - The GIMP Library
 *
 * gimpmd5.h
 *
 * Use of this code is deprecated! Use %GChecksum from GLib instead.
 */

#ifndef __GIMP_MD5_H__
#define __GIMP_MD5_H__

G_BEGIN_DECLS

/* For information look into the C source or the html documentation */

#ifndef GIMP_DISABLE_DEPRECATED

void gimp_md5_get_digest (const gchar *buffer,
                          gint         buffer_size,
                          guchar       digest[16]);

#endif /* GIMP_DISABLE_DEPRECATED */

G_END_DECLS

#endif  /* __GIMP_MD5_H__ */
