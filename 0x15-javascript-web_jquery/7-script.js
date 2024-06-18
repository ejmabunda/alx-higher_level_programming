$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: function (data) {
    $('#character').text(data.name);
  },
  error: function (jqXHR, textStatus, errorThrown) {
    // Handle errors if the request fails
    console.error('Error fetching character data: ', textStatus, errorThrown);
  }
});
