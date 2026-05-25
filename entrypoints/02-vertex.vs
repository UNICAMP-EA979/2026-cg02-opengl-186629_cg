#version 330 core

// Utilize como base o 01-vertex.vs
// Adicione o input da UV na location=1, e crie uma nova saída para fornecer a UV ao fragment
// Raciocínio: UVs (coordenadas de textura) precisam ser interpoladas linearmente
// entre os vértices do triângulo. O fragment shader recebe essas coordenadas
// interpoladas automaticamente pelo rasterizador.

layout(location = 0) in vec3 position;
layout(location = 1) in vec2 uv_in;

out vec2 uv;

uniform mat4 modelTransformation;
uniform mat4 viewTransformation;
uniform mat4 projectionMatrix;

void main()
{
    gl_Position = projectionMatrix * viewTransformation * modelTransformation * vec4(position, 1.0);
    uv = uv_in;
}

/////////////////////////////////////////////////////////////////////////////////////////////