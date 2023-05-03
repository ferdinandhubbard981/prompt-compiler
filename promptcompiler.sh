#!/bin/bash

# Check for correct number of arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 input_file.txt output_file.txt"
    exit 1
fi

# Run docker command
docker run --rm -v $(pwd):/app/host compile-prompt --input /app/host/"$1" --output /app/host/"$2"
