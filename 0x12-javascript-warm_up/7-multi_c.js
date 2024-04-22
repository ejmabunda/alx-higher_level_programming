#!/usr/bin/node
const argv = require('process:node');
const x = Number(argv[2]);

if (!process.argv[2] || !Number.isInteger(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
