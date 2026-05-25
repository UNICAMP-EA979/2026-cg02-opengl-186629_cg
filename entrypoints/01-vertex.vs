#version 330 core
// Recebe a position no location = 0
// e as uniforms mat4 modelTransformation, viewTransformation e projectionMatrix
// 
// Converte a position para o clip space usando as transformações e armazena em gl_Position.

// SEU CÓDIGO AQUI //////////////////////////////////////////////////////////////////////////
// Raciocínio: O pipeline gráfico transforma coordenadas através de vários espaços:
// 1. Local space: coordenadas do modelo
// 2. World space: aplicar transformação do modelo
// 3. View space: aplicar transformação da câmera
// 4. Projection space (clip space): aplicar matriz de projeção
// A ordem de multiplicação é: projection * view * model * position
// (nota: multiplicação de matrizes é da direita para esquerda em GLSL)

layout(location = 0) in vec3 position;

uniform mat4 modelTransformation;
uniform mat4 viewTransformation;
uniform mat4 projectionMatrix;

void main()
{
    gl_Position = projectionMatrix * viewTransformation * modelTransformation * vec4(position, 1.0);
}

/////////////////////////////////////////////////////////////////////////////////////////////