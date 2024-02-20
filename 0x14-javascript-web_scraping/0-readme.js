#!/usr/bin/node
/* a script that reads and prints the content of a file. */

const fs = require('fs');

const filepath = process.argv.slice(2)[0];

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
