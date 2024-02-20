#!/usr/bin/node
/*
    prints all characters of a Star Wars movie
*/

const request = require('request');

const args = process.argv.slice(2);
const movieId = args[0];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const movie = JSON.parse(body);
  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) console.log(err);
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});

