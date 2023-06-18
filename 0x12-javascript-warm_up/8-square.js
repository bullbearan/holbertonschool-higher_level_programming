#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length > 2) {
  if (process.argv.length === 2 || isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < process.argv[2]; i++) {
      let str = '';
      for (let j = 0; j < process.argv[2]; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}
