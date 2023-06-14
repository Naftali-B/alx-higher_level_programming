#!/usr/bin/node
const { dict } = require('./101-data');
const sDict = {};
for (const userId in dict) {
  const occur = dict[userId];
  if (occur in sDict) {
    sDict[occur].push(userId);
  } else {
    sDict[occur] = [userId];
  }
}
console.log(sDict);
