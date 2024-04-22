#!/usr/bin/node
const args = process.argv;

if (args.length < 2 || !Number.isInteger(Number(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  const numOccurrences = Number(args[2]);
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
