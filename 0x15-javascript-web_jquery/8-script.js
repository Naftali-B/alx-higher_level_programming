/* JavaScript script that fetches and lists the title for all movies
using the URL: https://swapi-api.alx-tools.com/api/films/?format=json */
$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (res) => {
    res.results.forEach((obj) => {
      $('UL#list_movies').append('<li>' + obj.title + '</li>');
    });
  });
});
