#!/usr/bin/node
const args = process.argv;

if (args.length < 2 || !Number.isInteger(Number(args[2]))) {
  console.log('Missing size');
} else {
  const x = Number(args[2]);

  for (let a = 0; a < x; a++) {
    let line = '';
    for (let b = 0; b < x; b++) {
      line += 'X';
    }
    console.log(line);
  }
}
