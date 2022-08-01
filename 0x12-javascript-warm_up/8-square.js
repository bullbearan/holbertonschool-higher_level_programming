#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count === 1 || count > 1) {
  if (count === 1 || isNaN(argv[2])) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < argv[2]; i++) {
      let str = '';
      for (let j = 0; j < argv[2]; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}
