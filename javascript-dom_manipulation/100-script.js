document.addEventListener('DOMContentLoaded', function () {
    const addBtn = document.getElementById('add_item');
    const removeBtn = document.getElementById('remove_item');
    const clearBtn = document.getElementById('clear_list');
    const myList = document.querySelector('.my_list');

    addBtn.addEventListener('click', function () {
        const li = document.createElement('li');
        li.textContent = 'Item';
        myList.appendChild(li);
    });

    removeBtn.addEventListener('click', function () {
        if (myList.lastElementChild) {
            myList.removeChild(myList.lastElementChild);
        }
    });

    clearBtn.addEventListener('click', function () {
        myList.innerHTML = '';
    });
});
