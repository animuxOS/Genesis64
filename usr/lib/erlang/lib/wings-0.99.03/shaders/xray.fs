// $Id: xray.fs 117 2007-07-19 16:44:01Z antoneos $
//
// vertex to fragment shader io

varying vec3 N;
varying vec3 I;
varying vec4 Cs;

// globals
float edgefalloff = 1.0;

// entry point
void main()
{
    float opac = dot(normalize(-N), normalize(-I));
    opac = abs(opac);
    opac = 1.0-pow(opac, edgefalloff);
    //opac = 1.0 - opac;
    gl_FragColor =  opac * Cs;
    gl_FragColor.a = opac;
}
