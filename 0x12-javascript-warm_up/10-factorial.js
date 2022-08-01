#!/usr/bin/node
function fac (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return (n * fac(n - 1));
  }
}
if (process.argv.length < 3) {
  console.log(1);
} else {
  console.log(fac(Math.floor(process.argv[2])));
}
