#ifndef JOB_LIBXFPRINT_H
#define JOB_LIBXFPRINT_H

#include <glib.h>

typedef enum
{
  JOB_STATE_PENDING,
  JOB_STATE_PRINTING,
} JobState;


typedef struct _Job Job;

struct _Job
{
  gchar *name;
  guint id;
  gchar *user;
  JobState state;
  guint size;
  guint priority;
  gchar *creation_time;
  gchar *processing_time;
};

void job_free (Job * job);
void jobs_free (GList * jobs);

#endif
