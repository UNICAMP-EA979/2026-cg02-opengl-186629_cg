#version 330 core
// Define a saída FragColor para a cor branca
// Raciocínio: Todos os fragmentos terão a mesma cor branca (1, 1, 1, 1).
// Isso permite verificar se a geometria está renderizando corretamente.

out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0, 1.0, 1.0, 1.0);
}
/////////////////////////////////////////////////////////////////////////////////////////////