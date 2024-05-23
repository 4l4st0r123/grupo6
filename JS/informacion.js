function visible() {
    var elem1 = document.querySelector(".TP_info").style,
        elem2 = document.querySelector(".TP_caracteristicas").style,
        elem3 = document.querySelector(".TP_info");
    elem1.display = "block";
    elem2.display = "block";
    elem3.focus();
}