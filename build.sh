#!/bin/bash
python3 src/main.py "https://mrhatted.github.io/SSG/"
cd docs && python3 -m http.server 8888
