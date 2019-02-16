
function confirmacion() {
    var pregunta = confirm("¿Desea salir de la web e ir a la documentación?")
    if (pregunta){
        window.location = "https://www.djangoproject.com/";
    }else{
        alert("Gracias por permanecer en la página!")
    }
}
function scroll(){
    window.scrollTo(0, 80);
}