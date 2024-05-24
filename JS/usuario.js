var newUser, formValues, objUser, formulario, text;

newUser = localStorage.getItem("nuevoUsuario");
formValues = ["Nombre", "Apellido", "DNI", "Género", "Fecha", "Calle", "Número",
              "zona_geo", "Usuario", "Clave", "email", "foto"];
objUser = JSON.parse(newUser);

formulario = document.querySelector("#content");
formulario.innerHTML = "<tr><th>Atributo del Formulario</th><th>Valor Registrado</th></tr>";


for (let i in formValues) {
    const fila = document.createElement("tr");
    const datosA = document.createElement("td");
    const datosB = document.createElement("td");
    
    let main = formValues[i]
    let sub = objUser[main]
    let atributo = document.createTextNode(main);
    let valor = document.createTextNode(sub);
    datosA.appendChild(atributo);
    datosB.appendChild(valor);
    fila.appendChild(datosA);
    fila.appendChild(datosB);
    formulario.appendChild(fila);
}