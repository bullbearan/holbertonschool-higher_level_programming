#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count === 1) {
  console.log('Not a number');
} else if (count > 1) {
  if (isNaN(argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Math.floor(argv[2]));
  }
}
