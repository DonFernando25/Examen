


const jugadoresArqueros = [
    { nombre: "Buffon", edad: "46 años", profesion:"" , imagen: "img/buffon.png" },
    { nombre: "Lev Yashin", edad: "95 años",profesion:"" , imagen: "img/lev.png" },
    { nombre: "Ivarov", edad: "47 años",profesion:"" , imagen: "img/iva.png" },
];

const jugadoresDefensas = [
    { nombre: "Valeny", edad: "49 años",profesion:"" , imagen: "img/val.png" },
    { nombre: "Jaric", edad: "56 años",profesion:"" , imagen: "img/jar.png" },
    { nombre: "Stremer", edad: "45 años",profesion:"" , imagen: "img/str.png" },
];

const jugadoresMediocampistas = [
    { nombre: "Dodo", edad: "46 años",profesion:"" , imagen: "img/dod.png" },
    { nombre: "Iouga", edad: "50 años",profesion:"" , imagen: "img/iou.png" },
    { nombre: "Espimas", edad: "47 años", profesion:"" ,imagen: "img/esp.png" },
    { nombre: "Ximelez", edad: "47 años",profesion:"" , imagen: "img/xim.png" },
    { nombre: "Minanda", edad: "52 años",profesion:"" , imagen: "img/mina.png" },
    
];

const jugadoresDelanteros = [
    { nombre: "Donraldinho", edad: "20 años",profesion:"" , imagen: "img/donra.png" },
    { nombre: "Leo Messi", edad: "36 años",profesion:"" , imagen: "img/mezi.png" },
    { nombre: "Ronaldo", edad: "39 años",profesion:"" , imagen: "img/ronaldo.png" },
    { nombre: "Castolo", edad: "48 años", profesion:"" ,imagen: "img/cas.png" },
];

const jugadoresCuerpoTecnico = [
    { nombre: "Guardiola", edad: "20 años",profesion:"Entrenador", imagen: "img/gua.png" },
    { nombre: "Mourinho", edad: "36 años", profesion:"Ayudante Técnico", imagen: "img/mou.png" },
    { nombre: "Jonathan Sánchez", edad: "45 años", profesion:"Medico de cancha", imagen: "img/js.png" },

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


generarTarjetasJugadores(jugadoresArqueros, document.getElementById("arqueros"));
generarTarjetasJugadores(jugadoresDefensas, document.getElementById("defensas"));
generarTarjetasJugadores(jugadoresMediocampistas, document.getElementById("mediocampistas"));
generarTarjetasJugadores(jugadoresDelanteros, document.getElementById("delanteros"));
generarTarjetasJugadores(jugadoresCuerpoTecnico, document.getElementById("cuerpoTecnico"));