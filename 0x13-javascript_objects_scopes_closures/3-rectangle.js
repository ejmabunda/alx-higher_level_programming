#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        let line = '';
        for (let col = 0; col < this.width; col++) {
          line += '#';
        }
        console.log(line);
      }
    }
  }
}

module.exports = Rectangle;
