#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  let len = list.length - 1;
  let x = 0;
  while ((len - x) > 0) {
    const aux = list[len];
    list[len] = list[x];
    list[x] = aux;
    x++;
    len--;
  }
  return list;
};
