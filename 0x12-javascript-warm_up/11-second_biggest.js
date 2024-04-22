#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

console.log(secondBiggest(args));

function secondBiggest (args) {
  if (args.length <= 1) {
    return 0;
  }

  let biggest = -Infinity;
  let second_biggest = -Infinity;

  for (let a = 0; a < args.length; a++) {
    if (args[a] > biggest) {
      second_biggest = biggest;
      biggest = args[a];
    } else if (args[a] > second_biggest && args[a] < biggest) {
      second_biggest = args[a];
    }
  }
  return second_biggest;
}
