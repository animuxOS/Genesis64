// $Id: langbein-cell.vs 117 2007-07-19 16:44:01Z antoneos $

varying vec3 normal;
varying vec4 position;

void main()
{
  normal = gl_NormalMatrix * gl_Normal;
  position = gl_ModelViewMatrix * gl_Vertex;
  gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}

