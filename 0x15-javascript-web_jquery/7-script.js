/* JavaScript script that fetches the character name from this URL:
https://swapi-api.alx-tools.com/api/people/5/?format=json */
$(() => {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (res) => {
    $('DIV#character').text(res.name);
  });
});
