#!/usr/bin/node

const size = parseInt(process.argv[2], 10);
const output = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(output.repeat(size));
  }
}
