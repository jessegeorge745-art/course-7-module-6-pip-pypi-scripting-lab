import sys
import os

# Ensure the project root is on sys.path so that
# `from lib.generate_log import generate_log` resolves correctly
# regardless of which directory pytest is invoked from.
sys.path.insert(0, os.path.dirname(__file__))