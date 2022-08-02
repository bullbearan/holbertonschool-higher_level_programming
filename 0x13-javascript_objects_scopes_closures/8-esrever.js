#!/usr/bin/node
exports.esrever = function (list) {
  const last = list.length - 1;
  for (let i = 0; i < list.length / 2; i++) {
    const tmp = list[i];
    list[i] = list[last - i];
    list[last - i] = tmp;
  }
  return list;
};
