$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  dataType: 'json',
  success: function (data) {
    $('#hello').text(data.hello);
  },
  error: function (jqXHR, textStatus, errorThrown) {
    // Handle errors if the request fails
    console.error('Error fetching character data:', textStatus, errorThrown);
  }
});
