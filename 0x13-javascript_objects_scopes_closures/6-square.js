#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        let shape = '';
        for (let j = 0; j < this.width; j++) {
          shape += 'X';
        }
        console.log(shape);
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        let shape = '';
        for (let j = 0; j < this.width; j++) {
          shape += 'C';
        }
        console.log(shape);
      }
    }
  }
}
module.exports = Square;
