#!/bin/bash
test_dir=$(find . -name tests.py -exec dirname {} \;)
if [ -z "$test_dir" ]; then
  echo "Error: tests.py not found"
  exit 1
fi
cd "$test_dir"
python3 -m unittest project/tests.py