#!/usr/bin/node
const argv = require('process:node');

console.log(factorial(argv[2]));

function factorial (a) {
  if (a === 1) {
    return 1;
  } return 1 + factorial(a - 1);
}
