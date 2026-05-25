#!/usr/bin/env python3
"""
Teste simplificado do entrypoint 01-hello_cube.py
"""
import sys
import os

# Mude para o diretório de entrypoints
os.chdir(r"C:\Users\saopa\Desktop\Nova pasta (3)\2026-cg02-opengl-186629_cg\entrypoints")

import numpy as np
import urenderer

print("Starting 01-hello_cube test...")

try:
    urenderer.utils.clear_workdir("01-hello_cube")
    print("✓ Cleared workdir")
    
    renderer = urenderer.renderer.OpenGLRenderer(1920, 1080)
    print("✓ Created renderer")
    
    renderer.background_color = np.array([0, 0, 0, 1], np.float32)
    runtime = urenderer.application.Runtime(renderer, name="01-hello_cube")
    print("✓ Created runtime")

    shader = urenderer.renderer.Shader("01-vertex.vs", "01-fragment.fs")
    print("✓ Created shader")
    
    material = urenderer.renderer.opengl.Material(shader)
    print("✓ Created material")

    cube = urenderer.node.Node()
    print("✓ Created cube node")

    cube.translation = np.array([0, 0, -5], np.float64)
    cube.rotation = np.array([45, 45, 45], np.float64)
    cube.render_data["mesh"] = urenderer.geometry.mesh.get_mesh_cube()
    cube.render_data["material"] = material
    print("✓ Configured cube")

    runtime.scene.add_child(cube)
    print("✓ Added cube to scene")

    print("✓ Running one iteration...")
    runtime.iter(capture=True)
    print("✓ Test passed!")

except Exception as e:
    print(f"✗ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
