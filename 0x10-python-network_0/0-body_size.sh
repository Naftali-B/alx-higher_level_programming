#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
	  echo "Usage: $0 <URL>"
	    exit 1
fi

# Get the URL from command-line argument
url=$1

# Send a GET request using curl and output the size of the response body
size=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size
echo "Response size: $size bytes"
