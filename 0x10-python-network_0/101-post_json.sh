#!/bin/bash
file_content=$(cat "$2" 2>/dev/null)

if [[ $? -ne 0 ]]; then
	    echo "Failed to read file: $2"
	        exit 1
fi

curl -s -X POST -H "Content-Type: application/json" -d "$file_content" "$1"

