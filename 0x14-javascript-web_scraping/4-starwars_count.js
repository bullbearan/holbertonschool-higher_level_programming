#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
axios.get(args[2])
  .then(function (response) {
    let res = 0;
    for (const e of response.data.results) {
      for (const ele of e.characters) {
        if (ele.includes('18')) {
          res += 1;
        }
      }
    }
    console.log(res);
  })
  .catch(function (error) {
    console.error(error);
  })
  .then(function () {
  });
