#!/bin/bash
python3 src/main.py "/mrhatted/SSG/"
cd docs && python3 -m http.server 8888
