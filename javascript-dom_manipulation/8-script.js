async function getHello() {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    return data.hello;
}

getHello().then(hello => {
    const helloElement = document.getElementById('hello');
    helloElement.textContent = hello;
});
