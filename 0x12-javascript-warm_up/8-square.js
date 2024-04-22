#!/usr/bin/node
const argv = require('process:node');
const x = Number(argv[2]);

if (!argv[2] || !Number.isInteger(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let a = 0; a < x; a++) {
    for (let b = 0; b < x; b++) {
      console.log('X');
    }
  }
}
