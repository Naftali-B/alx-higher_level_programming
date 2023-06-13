#!/usr/bin/node
const numOf = parseInt(process.argv[2], 10);
if (Number.isNaN(numOf)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOf; i++) {
    console.log('C is fun');
  }
}
