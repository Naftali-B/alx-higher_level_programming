/*  toggles the class of the <header> elemen
when the user clicks on the tag */
$(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
