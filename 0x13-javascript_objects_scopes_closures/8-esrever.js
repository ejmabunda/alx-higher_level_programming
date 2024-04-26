#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let a = list.length - 1; a >= 0; a--) {
    reversed.push(list[a]);
  }

  return reversed;
};
