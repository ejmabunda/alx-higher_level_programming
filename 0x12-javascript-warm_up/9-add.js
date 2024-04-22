#!/usr/bin/node
const argv = require('process:node');

console.log(add(argv[2] + argv[3]));

function add (a, b) {
  return a + b;
}
