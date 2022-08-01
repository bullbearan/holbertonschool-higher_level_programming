#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count === 1 || count > 1) {
  if (count === 1 || isNaN(argv[2])) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < argv[2]; i++) {
      console.log('C is fun');
    }
  }
}
