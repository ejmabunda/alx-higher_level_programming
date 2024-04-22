#!/usr/bin/node
const { argv } = require('node:process');
const num = Number(argv[2]);

if (Number.isInteger(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
