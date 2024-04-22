#!/usr/bin/node
const args = process.argv;

console.log(secondBiggest(args));

function secondBiggest (args) {
  let biggest = 0
  let second_biggest = 0;
  
  for (let a = 2; a < args.length; a++) {
    if (args[a] > biggest) {
      second_biggest = biggest;
      biggest = args[a];
    }
  }
  return second_biggest;
}
