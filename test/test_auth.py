import os
import subprocess
import sys

# Get the path of the scripts directory
scripts_dir = os.path.join(os.path.dirname(__file__), "..", "scripts")

# Add the scripts directory to sys.path
sys.path.append(scripts_dir)

from auth import *

print(create_user("black", "black"))
print(authenticate_user("black", "black"))
