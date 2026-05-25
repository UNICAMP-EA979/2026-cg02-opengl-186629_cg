#!/usr/bin/env python3
import sys
print(f"Python: {sys.executable}")
print(f"Version: {sys.version}")

try:
    import urenderer
    print("✓ urenderer imported successfully")
except ImportError as e:
    print(f"✗ Failed to import urenderer: {e}")
    sys.exit(1)

try:
    from urenderer.renderer.opengl import Shader, Texture, Material
    from urenderer.geometry.mesh import Mesh
    from urenderer.node import Node, Camera
    print("✓ Core classes imported successfully")
except ImportError as e:
    print(f"✗ Failed to import classes: {e}")
    sys.exit(1)

print("\n✓ All imports successful!")

