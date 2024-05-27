function validarNombres(nombres) {
    return nombres.length >= 3 && /^[a-zA-Z]+$/.test(nombres);
}

function validarApellidos(apellidos) {
    return apellidos.length >= 3 && /^[a-zA-Z]+$/.test(apellidos);
}