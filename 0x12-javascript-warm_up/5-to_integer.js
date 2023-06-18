#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Not a number');
} else if (process.argv.length > 2) {
  if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Math.floor(process.argv[2]));
  }
}
