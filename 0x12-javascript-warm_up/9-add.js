#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    return Math.floor(a) + Math.floor(b);
  }
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  console.log(add(process.argv[2], process.argv[3]));
}
