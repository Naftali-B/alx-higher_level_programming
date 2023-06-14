#!/usr/bin/node
exports.converter = function (base) {
  return function (inp) {
    return inp.toString(base);
  };
};
