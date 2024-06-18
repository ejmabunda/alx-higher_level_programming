$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  dataType: 'json',
  success: function (data) {
    console.log(data.results);

    data.results.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  },
  error: function (jqXHR, textStatus, errorThrown) {
    // Handle errors if the request fails
    console.error('Error fetching character data:', textStatus, errorThrown);
  }
});
