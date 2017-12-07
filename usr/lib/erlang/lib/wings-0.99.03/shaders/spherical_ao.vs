// $Id: spherical_ao.vs 236 2008-01-26 23:02:59Z antoneos $
// Spherical Ambient Occlusion (spherical depth)

varying vec3 DepthColor;

void main()
{
	float z = length(gl_Vertex.xyz);
	z = pow(z, 8.0);
	vec4 color = gl_FrontMaterial.diffuse * gl_Color;
	DepthColor = vec3(color * vec4(z));
	gl_Position = ftransform();
}
