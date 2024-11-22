async function getName() {
    const name = await response.json();
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    return name;
}

getName().then(name => {
    document.getElementById('character').textContent = name.name;
});
