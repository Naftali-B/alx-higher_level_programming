#!/usr/bin/node
/*
    a script that prints the number of movies
    where the character “Wedge Antilles” is present.
*/

const request = require('request');

const id = '18';
const url = process.argv.slice(2)[0];

request(url, (err, res, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  const wedgeFilms = films.map(film => film.characters)
    .filter(arr => arr.find(str => str.search(id) !== -1));
  console.log(wedgeFilms.length);
});
