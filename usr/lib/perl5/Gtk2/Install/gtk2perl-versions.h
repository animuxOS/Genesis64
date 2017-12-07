#define PANGO_MAJOR_VERSION (1)
#define PANGO_MINOR_VERSION (14)
#define PANGO_MICRO_VERSION (5)
#define PANGO_CHECK_VERSION(major,minor,micro) \
	(PANGO_MAJOR_VERSION > (major) || \
	 (PANGO_MAJOR_VERSION == (major) && PANGO_MINOR_VERSION > (minor)) || \
	 (PANGO_MAJOR_VERSION == (major) && PANGO_MINOR_VERSION == (minor) && PANGO_MICRO_VERSION >= (micro)))
#define ATK_MAJOR_VERSION (1)
#define ATK_MINOR_VERSION (12)
#define ATK_MICRO_VERSION (3)
#define ATK_CHECK_VERSION(major,minor,micro) \
	(ATK_MAJOR_VERSION > (major) || \
	 (ATK_MAJOR_VERSION == (major) && ATK_MINOR_VERSION > (minor)) || \
	 (ATK_MAJOR_VERSION == (major) && ATK_MINOR_VERSION == (minor) && ATK_MICRO_VERSION >= (micro)))
