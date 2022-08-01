#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count === 1) {
  console.log('No argument');
} else if (count > 1) {
  console.log(argv[2]);
}
