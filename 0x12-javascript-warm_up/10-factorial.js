#!/usr/bin/node
const args = process.argv;

if (isNaN(args[2])) {
  console.log(factorial(1));
} else {
  console.log(factorial(Number(args[2])));
}

function factorial (a) {
  if (a === 1) {
    return 1;
  } return a * factorial(a - 1);
}
