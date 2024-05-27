function mostrarArqueros() {
    document.getElementById("arqueros").scrollIntoView({ behavior: "smooth" });
}

function mostrarDefensas() {
    document.getElementById("defensas").scrollIntoView({ behavior: "smooth" });
}

function mostrarMediocampistas() {
    document.getElementById("mediocampistas").scrollIntoView({ behavior: "smooth" });
}

function mostrarDelanteros() {
    document.getElementById("delanteros").scrollIntoView({ behavior: "smooth" });
}

function mostrarCuerpoTecnico() {
    document.getElementById("cuerpoTecnico").scrollIntoView({ behavior: "smooth" });
}

window.onscroll = function() {
    mostrarFlecha();
};

function mostrarFlecha() {
    var flecha = document.getElementById("arrow-up");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        flecha.style.display = "block";
    } else {
        flecha.style.display = "none";
    }
}


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("arrow-up").addEventListener("click", function() {
        document.body.scrollTop = 0; 
        document.documentElement.scrollTop = 0; 
    });
});