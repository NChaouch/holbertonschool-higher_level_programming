document.getElementById('toggle_header').addEventListener('click', toggleHeader);
const header = document.querySelector('header');

function toggleHeader(){
    if (header.classList.contains('red')){
        header.classList.remove('red');
        header.classList.add('green');
    }
    else{
        header.classList.remove('green');
        header.classList.add('red');
    }
}
