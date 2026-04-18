# Copyright (c) 2026 Lachlan Harris. All Rights Reserved.
# This code is licensed under Apache 2.0
#
# Fix for VS code test discovery not finding the backend folder
# for module imports

import sys
from pathlib import Path


BACKEND_DIR = Path(__file__).resolve().parent / "backend"
sys.path.insert(0, str(BACKEND_DIR))
