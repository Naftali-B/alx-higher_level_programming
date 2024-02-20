#!/usr/bin/node
/*
    prints all characters of a Star Wars movie in
    the same order as the list "characters"
    in the /films/ response
*/

const request = require('request');

const args = process.argv.slice(2);
const movieId = args[0];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch characters in the same order as they appear in the /films/ response
function fetchCharactersInOrder(characterUrls) {
  const promises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  });

  return Promise.all(promises);
}

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  fetchCharactersInOrder(characterUrls)
    .then(characters => {
      characters.forEach(character => console.log(character));
    })
    .catch(error => console.error(error));
});

