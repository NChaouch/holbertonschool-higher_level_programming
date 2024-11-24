async function getTitle() {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
    const data = await response.json();
    return data.results;
}

getTitle().then(movies => {
    const listMovies = document.getElementById('list_movies');
    movies.forEach(movie =>
    {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
    });
});
