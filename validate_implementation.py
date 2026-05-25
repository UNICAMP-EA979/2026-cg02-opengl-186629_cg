#!/usr/bin/env python3
"""
Script de validação de implementação
Testa todas as classes principais
"""

import sys
import os

os.chdir(r"C:\Users\saopa\Desktop\Nova pasta (3)\2026-cg02-opengl-186629_cg")

import numpy as np

print("=" * 60)
print("VALIDAÇÃO DE IMPLEMENTAÇÃO - RENDERIZADOR OPENGL")
print("=" * 60)

# Test 1: Import all modules
print("\n[1/5] Testando imports...")
try:
    import urenderer
    from urenderer.renderer.opengl import Shader, Texture, Material, OpenGLRenderer
    from urenderer.geometry.mesh import Mesh, get_mesh_cube, get_mesh_triangle
    from urenderer.node import Node, Camera
    from urenderer.application import Runtime
    print("✓ Todos os módulos importados com sucesso")
except Exception as e:
    print(f"✗ Erro ao importar: {e}")
    sys.exit(1)

# Test 2: Test OpenGL initialization
print("\n[2/5] Testando inicialização OpenGL...")
try:
    renderer = OpenGLRenderer(800, 600)
    print(f"✓ Renderer OpenGL criado")
except Exception as e:
    print(f"✗ Erro ao criar renderer: {e}")
    sys.exit(1)

# Test 3: Test Shader (com contexto)
print("\n[3/5] Testando Shader...")
try:
    os.chdir(r"C:\Users\saopa\Desktop\Nova pasta (3)\2026-cg02-opengl-186629_cg\entrypoints")
    shader = Shader("01-vertex.vs", "01-fragment.fs")
    print(f"✓ Shader compilado: {shader.shader_program}")
except Exception as e:
    print(f"✗ Erro ao compilar shader: {e}")
    sys.exit(1)

# Test 4: Test Mesh
print("\n[4/5] Testando Mesh...")
try:
    tri_mesh = get_mesh_triangle()
    cube_mesh = get_mesh_cube()
    print(f"✓ Triângulo: {len(tri_mesh.vertex)//3} verts, {len(tri_mesh.index)} indices")
    print(f"✓ Cubo: {len(cube_mesh.vertex)//3} verts, {len(cube_mesh.index)} indices")
except Exception as e:
    print(f"✗ Erro ao criar geometria: {e}")
    sys.exit(1)

# Test 5: Test Material
print("\n[5/5] Testando Material...")
try:
    material = Material(shader)
    material.set_uniform("test_float", 1.5)
    material.set_uniform("test_int", 42)
    material.set_uniform("test_bool", True)
    
    # Testar matrix
    mat4 = np.eye(4, dtype=np.float32)
    material.set_uniform("test_matrix", mat4)
    
    print(f"✓ Material criado com uniforms")
except Exception as e:
    print(f"✗ Erro ao criar material: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✓ VALIDAÇÃO COMPLETA - TODOS OS TESTES PASSARAM!")
print("=" * 60)
print("\nArquivos implementados:")
print("  • Shader.py - Compilação e linkagem de shaders")
print("  • Mesh.py - Gerenciamento de buffers VBO/EBO/VAO")
print("  • OpenGLRenderer.py - Inicialização e renderização")
print("  • Texture.py - Carregamento de texturas")
print("  • Triangle.py - Geometria de triângulo")
print("  • Shaders GLSL - 01, 02, 04, 05")
print("  • Entrypoints - 02, 03, 04, 05")
print("\nPara executar os entrypoints com Python 3.13:")
print("  python entrypoints/01-hello_cube.py")
print("  python entrypoints/02-cube_texture.py")
print("  python entrypoints/04-colors.py")

