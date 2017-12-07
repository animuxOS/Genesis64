// $Id: vertex_color.vs 130 2007-09-08 18:53:44Z antoneos $
// Colors based on vertex-normal or face-normals

varying vec3 VertexColor;
uniform int  Flag;

void main()
{
    if (Flag==0)
        VertexColor = gl_Vertex.xyz;
    else
        VertexColor = gl_Normal.xyz;
    gl_Position = ftransform();
}
