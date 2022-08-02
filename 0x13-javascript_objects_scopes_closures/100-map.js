#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const newList = list.map((ele, i) => {
  return (ele * i);
});
console.log(newList);
