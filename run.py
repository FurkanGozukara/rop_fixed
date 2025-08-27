#!/usr/bin/env python3

import sys
import os

# Add local BasicSR to path before any imports
current_dir = os.path.dirname(os.path.abspath(__file__))
basicsr_path = os.path.join(current_dir, 'BasicSR')
if os.path.exists(basicsr_path):
    sys.path.insert(0, basicsr_path)

from roop import core

if __name__ == '__main__':
    core.run()
