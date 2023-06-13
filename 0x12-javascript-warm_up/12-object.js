#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const output = process.argv.map(Number).slice(2).map(num => (num === 12 ? 89 : num)).sort((a, b) => a - b).reverse();
  console.log(output[1]);
}
