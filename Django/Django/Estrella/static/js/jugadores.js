document.addEventListener("DOMContentLoaded", function() {
    const jugadoresArqueros = [
        { nombre: "Buffon", edad: "46 años", profesion: "", imagen: urls.buffon },
        { nombre: "Lev Yashin", edad: "95 años", profesion: "", imagen: urls.lev },
        { nombre: "Ivarov", edad: "47 años", profesion: "", imagen: urls.iva }
    ];

    const jugadoresDefensas = [
        { nombre: "Valeny", edad: "49 años", profesion: "", imagen: urls.val },
        { nombre: "Jaric", edad: "56 años", profesion: "", imagen: urls.jar },
        { nombre: "Stremer", edad: "45 años", profesion: "", imagen: urls.str }
    ];

    const jugadoresMediocampistas = [
        { nombre: "Dodo", edad: "46 años", profesion: "", imagen: urls.dod },
        { nombre: "Iouga", edad: "50 años", profesion: "", imagen: urls.iou },
        { nombre: "Espimas", edad: "47 años", profesion: "", imagen: urls.esp },
        { nombre: "Ximelez", edad: "47 años", profesion: "", imagen: urls.xim },
        { nombre: "Minanda", edad: "52 años", profesion: "", imagen: urls.mina }
    ];

    const jugadoresDelanteros = [
        { nombre: "Donraldinho", edad: "20 años", profesion: "", imagen: urls.donra },
        { nombre: "Leo Messi", edad: "36 años", profesion: "", imagen: urls.mezi },
        { nombre: "Ronaldo", edad: "39 años", profesion: "", imagen: urls.ronaldo },
        { nombre: "Castolo", edad: "48 años", profesion: "", imagen: urls.cas }
    ];

    const jugadoresCuerpoTecnico = [
        { nombre: "Guardiola", edad: "20 años", profesion: "Entrenador", imagen: urls.gua },
        { nombre: "Mourinho", edad: "36 años", profesion: "Ayudante Técnico", imagen: urls.mou },
        { nombre: "Jonathan Sánchez", edad: "45 años", profesion: "Medico de cancha", imagen: urls.js }
    ];

    function generarTarjetasJugadores(jugadores, contenedor) {
        jugadores.forEach(jugador => {
            const columna = document.createElement("div");
            columna.classList.add("col");

            const tarjetaJugador = `
                <div class="card" style="width: 18rem;">
                    <img src="${jugador.imagen}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title"><center>${jugador.nombre}</center></h5>
                        <p class="card-text"><center>${jugador.edad}</center></p>
                        <p class="card-text"><center>${jugador.profesion}</center></p>
                    </div>
                </div>
            `;

            columna.innerHTML = tarjetaJugador;
            contenedor.appendChild(columna);
        });
    }

    function mostrarArqueros() {
        const contenedor = document.getElementById("arqueros");
        contenedor.innerHTML = "";  // Limpiar contenido anterior
        generarTarjetasJugadores(jugadoresArqueros, contenedor);
    }

    function mostrarDefensas() {
        const contenedor = document.getElementById("defensas");
        contenedor.innerHTML = "";  // Limpiar contenido anterior
        generarTarjetasJugadores(jugadoresDefensas, contenedor);
    }

    function mostrarMediocampistas() {
        const contenedor = document.getElementById("mediocampistas");
        contenedor.innerHTML = "";  // Limpiar contenido anterior
        generarTarjetasJugadores(jugadoresMediocampistas, contenedor);
    }

    function mostrarDelanteros() {
        const contenedor = document.getElementById("delanteros");
        contenedor.innerHTML = "";  // Limpiar contenido anterior
        generarTarjetasJugadores(jugadoresDelanteros, contenedor);
    }

    function mostrarCuerpoTecnico() {
        const contenedor = document.getElementById("cuerpoTecnico");
        contenedor.innerHTML = "";  // Limpiar contenido anterior
        generarTarjetasJugadores(jugadoresCuerpoTecnico, contenedor);
    }

    // Mostrar los arqueros por defecto
    mostrarArqueros();
    mostrarDefensas();
    mostrarMediocampistas();
    mostrarDelanteros();
    mostrarCuerpoTecnico();
});
