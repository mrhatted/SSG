#!/bin/bash
python3 src/main.py "/mrhatted/SSG/tree/main"
cd docs && python3 -m http.server 8888
