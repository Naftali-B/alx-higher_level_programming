/* script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello. */
$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (res) => {
    $('DIV#hello').text(res.hello);
    console.log(res);
  });
});
