#!/usr/bin/node
const argv = require('process:node');

console.log(second_biggest(argv[2]));

function second_biggest (a) {
  if (a === 1) {
    return 1;
  } return 1 + factorial(a - 1);
}
