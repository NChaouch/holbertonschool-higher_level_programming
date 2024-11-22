document.getElementById('add_item').onclick = () => {
    const newItem = document.createElement("li");
    const myList = document.querySelector(".my_list");
    newItem.textContent = "Item";
    myList.appendChild(newItem);
}
