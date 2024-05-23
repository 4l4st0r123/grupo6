var cont = 1;
function mostrar() {
    console.log("hello");
    var elem = document.querySelector(".nav").style;
    if (cont == 1) {
        elem.visibility = "hidden";
        cont = 0;
    } else if (cont == 0) {
        elem.visibility = "visible";
        cont = 1;
    }
}

function redirect(e) {
    location.href = e;
}