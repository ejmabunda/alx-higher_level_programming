$('#toggle_header').on('click', function () {
  $('header').toggleClass(function () {
    if ($('header').is('.red')) {
      return 'green';
    }

    return 'red';
  });
});
