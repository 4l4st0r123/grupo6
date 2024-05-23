(function () {  // Función anónima, https://geekytheory.com/javascript-funciones-anonimas-y-objetos/
    //Variables

    var formulario = document.getElementsByName('formulario')[0],
        elementos = formulario.elements,
        boton = document.getElementById('btn');

    // --------------------------------------------------------
    // Validamos Nombre
    // --------------------------------------------------------            
    var validarNombre = function (e) {
        if (formulario.nombre.value == 0) {
            alert("Tiene que escribir su nombre");
            document.formulario.nombre.focus()
            e.preventDefault();

        } else {
            var letras = /^[a-zA-Zá-üñÑ]+$/;
            if (!formulario.nombre.value.match(letras)) {
                alert("Complete el campo nombre solamente con caracteres");
                e.preventDefault();
            }
        }
    }

    var validarApellido = function (e) {
        if (formulario.apellido.value == 0) {      // Si el valor del campo id="nombre" del form está vacio...
            alert("Tiene que completar el campo apellido");
            document.formulario.apellido.focus()
            e.preventDefault();                 // Evita elcomportamiento por defecto, o sea, evita que se envíe el formulario
            //https://www.w3schools.com/jsref/event_preventdefault.asp

        } else { //valido que si no esté vacío el nombre sólo contenga letras
            var letras = /^[a-zA-Zá-üñÑ]+$/; //https://desarrollowp.com/blog/tutoriales/buscando-patron-con-expresiones-regulares/
            if (!formulario.apellido.value.match(letras)) {
                alert("Completa el campo nombre solamente con caracteres");
                e.preventDefault();
            }
        }
    }

    
    // --------------------------------------------------------   
    // Validamos Género   
    // --------------------------------------------------------                  
    var validarRadio = function (e) {
        if (formulario.genero[0].checked == true ||
            formulario.genero[1].checked == true ||
            formulario.genero[2].checked == true ||
            formulario.genero[3].checked == true) {
        } else {  //Si al menos uno de los Radio no está marcado....
            alert("Completa el campo género");
            formulario.genero.focus()
            e.preventDefault();
        }
    };
    
    // --------------------------------------------------------   
    // Validamos Edad
    // --------------------------------------------------------                      
    var validarFecha = function (e) {
        var nacimiento = formulario.fecha.valueAsDate.getFullYear(), fecha = new Date().getFullYear();
        if (nacimiento == Number) { //si es una cadena en blanco
            alert("Tiene que introducir un número entero en su edad.")
            formulario.fecha.focus()
            e.preventDefault();
        } else {
            var edad = fecha - nacimiento;
            if (edad < 18) {
                alert("Debe ser mayor de 18 años.")
                formulario.fecha.focus()
                e.preventDefault();
            }
        }   
    }
    
    // --------------------------------------------------------   
    // Validamos Terminos y Condiciones      
    // --------------------------------------------------------              
    var validarFecha = function (e) {
        if (formulario.zona.selectedIndex == 0) { //no elegí nada, entonces estoy en el índice 0
            alert("Debe seleccionar su localidad.")
            formulario.zona.focus()
            e.preventDefault();
        }
    }

    // --------------------------------------------------------   
    // Validamos Terminos y Condiciones      
    // --------------------------------------------------------              
    var validarCheckbox = function (e) {
        if (formulario.terminos.checked == false) {
            alert("Acepta los términos y condiciones");
            e.preventDefault();
        }
    };

    // --------------------------------------------------------   
    // Se ejecuta al presionar submit e invoca a las tres validaciones   
    // --------------------------------------------------------                  
    var validar = function (e) {  // "e" es el evento recibido del form (https://developer.mozilla.org/es/docs/Web/API/Event/preventDefault)
        validarNombre(e);
        validarApellido(e);
        validarFecha(e)
        validarRadio(e);
        validarCheckbox(e);
    };

    // --------------------------------------------------------
    // Espera que se presione "enviar" y llama a la función "validar"
    // submit es un evento DEL FORM, no del botón!
    formulario.addEventListener("submit", validar);
}())
