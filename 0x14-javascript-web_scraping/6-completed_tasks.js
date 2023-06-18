#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
axios.get(reqUrl)
  .then(function (response) {
    const objs = response.data;
    const res = {};
    for (const task of objs) {
      if (task.completed === true) {
        if (res[task.userId]) {
          res[task.userId] += 1;
        } else {
          res[task.userId] = 1;
        }
      }
    }
    console.log(res);
  })
  .catch(function (error) {
    console.error(error);
  });
