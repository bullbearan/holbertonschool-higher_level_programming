#!/usr/bin/node
exports.callMeMoby = function callMeMoby (number, theFunction) {
  for (let i = 0; i < number; i++) {
    theFunction();
  }
};
