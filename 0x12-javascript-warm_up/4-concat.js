#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count === 1) {
  console.log('undefined is undefined');
} else if (count === 2) {
  console.log(argv[2] + ' is undefined');
} else {
  console.log(argv[2] + ' is ' + argv[3]);
}
