import numpy as np

from .mesh import Mesh


def get_mesh_triangle() -> Mesh:
    '''
    Creates a triangle in mesh representation

    Returns:
        Mesh: triangle mesh
    '''

    ## SEU CÓDIGO AQUI ######################################################
    # Cria os vértices, índices e UVs de um triângulo
    # no plano z=0 e centrado em (0,0)
    # Raciocínio: Um triângulo simples é definido por 3 vértices.
    # Para centrar em (0,0), colocamos vértices em posições simétricas.
    # Os índices indicam qual vértice usar em qual ordem.
    # UVs mapeiam a textura ao triângulo.
    
    vertices = np.array([
        0.0,  0.5, 0.0,      # top
        -0.5, -0.5, 0.0,     # bottom left
        0.5, -0.5, 0.0       # bottom right
    ], dtype=np.float32)
    
    indices = np.array([0, 1, 2], dtype=np.uint32)
    
    uv = np.array([
        0.5, 1.0,    # top
        0.0, 0.0,    # bottom left
        1.0, 0.0     # bottom right
    ], dtype=np.float32)

    #########################################################################

    return Mesh(vertices, indices, uv)
