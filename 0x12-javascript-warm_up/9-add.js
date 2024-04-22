#!/usr/bin/node
const args = process.argv;

console.log(add(args[2], args[3]));

function add (a, b) {
  return Number(a) + Number(b);
}
