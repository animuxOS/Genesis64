// $Id: depth.fs 130 2007-09-08 18:53:44Z antoneos $
// Depth

varying vec3 DepthColor;

void main()
{
	gl_FragColor = vec4(DepthColor, 1.0);
}
