#!/usr/bin/node
/*
    a script that prints the title of a Star Wars movie
    where the episode number matches a given integer
*/

const request = require('request');

const num = process.argv.slice(2)[0];
const url = `https://swapi-api.hbtn.io/api/films/${num}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const output = JSON.parse(body).title;
  console.log(output);
});
