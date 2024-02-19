#!/usr/bin/node
import axios from 'axios';

const API_URL = 'https://swapi-api.hbtn.io/api';


async function getFilmCharacters(filmId) {
  try {
    const { data } = await axios.get(`${API_URL}/films/${filmId}/`);
    const charactersURL = data.characters;

    const charactersName = await Promise.all(
      charactersURL.map(async (url) => {
        const { data: characterData } = await axios.get(url);
        return characterData.name;
      })
    );

    console.log(charactersName.join('\n'));
  } catch (error) {
    console.error(error.message);
  }
}

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  getFilmCharacters(filmId);
}