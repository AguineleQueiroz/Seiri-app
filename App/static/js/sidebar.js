// Comportamento da sidebar
let btn__menu = document.getElementById('btn_menu');

if (sidebar.classList.contains('sidebar_active')) {
    document.getElementById('content__page').style.marginLeft = "300px";
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('sidebar_active');
    if (sidebar.classList.contains('sidebar_active')) {
        document.getElementById('content__page').style.marginLeft = "300px";
    } else {
        document.getElementById('content__page').style.marginLeft = "0";
    }
}

btn__menu.addEventListener('click', toggleSidebar);

const lista = document.querySelectorAll('.links__sidebar');
lista.forEach(item => {
    item.onclick = () => {
        lista.forEach(item => item.classList.remove('active'));
        item.classList.add('active');
    }
})