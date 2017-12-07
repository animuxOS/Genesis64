/* babl - dynamically extendable universal pixel conversion library.
 * Copyright (C) 2005-2008, Øyvind Kolås and others.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General
 * Public License along with this library; if not, see
 * <http://www.gnu.org/licenses/>.
 */

#ifndef _BABL_H
#error  this file is only to be included by babl.h 
#endif

/****************************************************************/
/* BablFish */
BABL_CLASS (fish);
/*  Create a babl fish capable of converting from source_format to
 *  destination_format, source and destination can be
 *  either strings with the names of the formats or BablFormat objects.
 */
Babl * babl_fish       (const void *source_format,
                        const void *destination_format);

/** Process n pixels from source to destination using babl_fish,
 *  returns number of pixels converted. 
 */
long   babl_process    (Babl *babl_fish,
                        void *source,
                        void *destination,
                        long  n);

Babl *babl_fish_id     (int id);
void  babl_fish_each   (BablEachFunction  each_fun,
                        void             *user_data);

/* BablFish, common base class for various fishes.
 */
typedef struct
{
  BablInstance    instance;
  const Babl     *source;
  const Babl     *destination;

  double          error;    /* the amount of noise introduced by the fish */

  /* instrumentation */
  int             processings; /* number of times the fish has been used */
  long            pixels;      /* number of pixels translates */
  long            usecs;       /* usecs spent within this fish */
} BablFish;

/* BablFishSimple is the simplest type of fish, wrapping a single
 * conversion function, (note this might not be the optimal chosen
 * conversion even if it exists)
 *
 * TODO: exterminate
 */
typedef struct
{
  BablFish         fish;
  BablConversion  *conversion;
} BablFishSimple;


/* BablFishPath is a combination of registered conversions, both
 * from the reference types / model conversions, and optimized format to
 * format conversion.
 *
 * This is the most advanced scheduled species of fish, some future
 * version of babl might even be evovling path fishes in a background
 * thread, based on the fish instrumentation. For this to work in a future
 * version transmogrification between the fish classes would be used.
 */
typedef struct
{
  BablFish         fish;
  double           cost;   /* number of  ticks *10 + chain_length */
  double           loss;   /* error introduced */
  BablList         *conversion_list;
} BablFishPath;

/* BablFishReference
 *
 * A BablFishReference is not intended to be fast, thus the algorithm
 * encoded can use a multi stage approach, based on the knowledge babl
 * has encoded in the pixel formats.
 *
 * One of the contributions that would be welcome are new fish factories.
 *
 * TODO:
 *   * make optimal use of a single allocation containing enough space
 *     for the maximum amount of memory needed in two adjecant buffers
 *     at any time.
 */
typedef struct
{
  BablFish         fish;
} BablFishReference;
