#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const content = args[3];
fs.writeFile(args[2], content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
