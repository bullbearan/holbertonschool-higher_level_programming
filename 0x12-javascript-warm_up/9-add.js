#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    return Math.floor(a) + Math.floor(b);
  }
}

if (count < 3) {
  console.log('NaN');
} else {
  console.log(add(argv[2], argv[3]));
}
