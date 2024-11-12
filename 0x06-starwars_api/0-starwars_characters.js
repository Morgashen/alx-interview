#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node star-wars-character-extractor.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
