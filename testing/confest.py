import sys
import os

# Add the project root so both:
#   from generate_log import generate_log      (CodeGrade style)
#   from lib.generate_log import generate_log  (test file style)
# both resolve correctly.
root = os.path.dirname(__file__)
sys.path.insert(0, root)

# Create a virtual 'lib' module that points to the root
# so the test import  `from lib.generate_log import generate_log` works
# even though generate_log.py lives at the root level.
import types
lib_module = types.ModuleType("lib")
lib_module.__path__ = [root]
lib_module.__package__ = "lib"
sys.modules["lib"] = lib_module