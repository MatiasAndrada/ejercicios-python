//! Tener en cuenta que es una buena practica usar una normalización de los datos para de que no halla un error con su valor en el codigo ASCII por que su valor cambia dependiendo el si es mmayuscula o minuscula

//Pedir al usuario que ingrese una letra y hacer un condicional para devolverle el grupo que pertenece separando el abecedario en 2 

let letra = prompt("Ingrese una letra");

//normalización de datos
letra = letra.toLowerCase();

if (letra >= "a" && letra <= "n") {
    console.log("Pertenece al grupo A");
} else if (letra >= "o" && letra <= "z") {
    console.log("Pertenece al grupo B");
} else {
    console.log("No es una letra valida");
}
