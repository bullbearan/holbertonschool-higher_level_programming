#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length > 2) {
  if (process.argv.length === 2 || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < process.argv[2]; i++) {
      console.log('C is fun');
    }
  }
}