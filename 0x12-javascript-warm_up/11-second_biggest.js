#!/usr/bin/node
import { argv } from 'node:process';
let count;
argv.forEach((val, index) => {
  count = index;
});
if (count < 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < count + 1; i++) {
    arr.push(Math.floor(argv[i]));
  }
  let ele = arr[0];
  let n = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > ele) {
      ele = arr[i];
      n = i;
    }
  }
  arr.splice(n, 1);
  let l = arr[0];
  for (let j = 1; j < arr.length; j++) {
    if (l < arr[j]) {
      l = arr[j];
    }
  }
  console.log(l);
}
