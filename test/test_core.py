import os
import sys

# Get the path of the scripts directory
scripts_dir = os.path.join(os.path.dirname(__file__), "..", "scripts")

# Add the scripts directory to sys.path
sys.path.append(scripts_dir)

from core import *

print(unblock_port("8000"))
