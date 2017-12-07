// $Id: hemilight.fs 117 2007-07-19 16:44:01Z antoneos $
//
// Fragment shader for hemispherical lighting
//
// Author: Randi Rost
//
// Copyright (C) 2005 3Dlabs, Inc.
//
// See 3Dlabs-License.txt for license information
//

varying vec3  DiffuseColor;

void main(void)
{
    gl_FragColor = vec4(DiffuseColor, 1.0);
}
