/* script that fetches and prints how to say “Hello” depending on the language */
i$(() => {
  $('#btn_translate').click(() => {
    translateHello();
  });

  $('#language_code').keypress((e) => {
    if (e.which === 13) {
      translateHello();
    }
  });

  function translateHello() {
    const code = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + code;
    $.get(url, (res) => {
      $('#hello').text(res.hello);
    }).fail(() => {
      $('#hello').text('Error: Language code not found');
    });
  }
});

