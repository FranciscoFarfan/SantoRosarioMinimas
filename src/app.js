// BASE DE REFLEXIONES (Extraído de reflections.json para evitar problemas de CORS local)
const reflectionsData = {
    "M": {
        "nombre": "Misterio Individual",
        "header": "Misterio Individual",
        "reflexiones": [
            "En este misterio, meditamos sobre la importancia de la oración constante y la devoción a María. Que cada Ave María nos acerque más al corazón de Jesús.",
            "El rosario es un arma poderosa contra el mal. Al rezar este misterio, pedimos la intercesión de la Virgen María para fortalecer nuestra fe y protegernos de las tentaciones."
        ]
    },
    "M1": {
        "nombre": "La Anunciación",
        "header": "1er Misterio Gozoso",
        "reflexiones": [
            "El ángel Gabriel anuncia a María que será la madre de Jesús. Su humilde 'Hágase en mí según tu palabra' nos enseña la obediencia perfecta a la voluntad de Dios.",
            "María acepta con fe el plan de Dios, aunque no comprende completamente. Pidamos la gracia de confiar en Dios incluso cuando no entendemos sus caminos."
        ]
    },
    "M2": {
        "nombre": "La Visitación",
        "header": "2do Misterio Gozoso",
        "reflexiones": [
            "María visita a su prima Isabel, llevando a Jesús en su vientre. Su caridad nos inspira a servir a los demás con amor y generosidad.",
            "Isabel reconoce la presencia de Jesús y proclama: '¿De dónde a mí que la madre de mi Señor venga a verme?' Que sepamos reconocer a Cristo en nuestros hermanos."
        ]
    },
    "M3": {
        "nombre": "El Nacimiento de Jesús",
        "header": "3er Misterio Gozoso",
        "reflexiones": [
            "Jesús nace en la pobreza de un pesebre, mostrándonos que Dios se hace pequeño por amor. Contemplemos la humildad del Rey del universo.",
            "Los ángeles anuncian: 'Gloria a Dios en las alturas y paz en la tierra a los hombres de buena voluntad.' Que el nacimiento de Cristo traiga paz a nuestros corazones."
        ]
    },
    "M4": {
        "nombre": "La Presentación de Jesús en el Templo",
        "header": "4to Misterio Gozoso",
        "reflexiones": [
            "María y José presentan a Jesús en el templo, cumpliendo la ley. Simeón profetiza que una espada atravesará el corazón de María. Preparémonos para aceptar el sufrimiento con fe.",
            "Simeón reconoce en Jesús la salvación de Dios. Pidamos la gracia de reconocer a Cristo en nuestra vida diaria y proclamarlo con alegría."
        ]
    },
    "M5": {
        "nombre": "El Niño Jesús Perdido y Hallado en el Templo",
        "header": "5to Misterio Gozoso",
        "reflexiones": [
            "María y José buscan angustiados a Jesús durante tres días. Cuando lo encuentran, Él está en la casa de su Padre. Que siempre busquemos a Jesús cuando lo hayamos perdido por el pecado.",
            "Jesús responde: '¿No sabían que debo ocuparme de los asuntos de mi Padre?' Aprendamos a poner a Dios en el primer lugar de nuestra vida."
        ]
    },
    "M6": {
        "nombre": "La Oración de Jesús en el Huerto",
        "header": "1er Misterio Doloroso",
        "reflexiones": [
            "Jesús ora con angustia en Getsemaní, sabiendo el sufrimiento que le espera. Su 'No se haga mi voluntad, sino la tuya' nos enseña la entrega total a Dios.",
            "Mientras Jesús sufre, los apóstoles duermen. Acompañemos a Jesús en su agonía con nuestra oración y vigilia, especialmente en la adoración eucarística."
        ]
    },
    "M7": {
        "nombre": "La Flagelación de Jesús",
        "header": "2do Misterio Doloroso",
        "reflexiones": [
            "Jesús es atado a una columna y azotado cruelmente. Cada latigazo es por nuestros pecados. Pidamos perdón por nuestras ofensas y la gracia de no pecar más.",
            "En su pasión, Jesús carga con nuestras culpas y nos obtiene la sanación. 'Por sus llagas hemos sido curados.' Agradezcamos su inmenso amor."
        ]
    },
    "M8": {
        "nombre": "La Coronación de Espinas",
        "header": "3er Misterio Doloroso",
        "reflexiones": [
            "Los soldados coronan a Jesús con espinas y se burlan de Él como rey. El Rey del universo acepta la humillación por amor a nosotros. Reparemos sus ultrajes con nuestra adoración.",
            "Jesús es coronado con espinas mientras nosotros aspiramos a la corona de gloria eterna. Que aceptemos nuestros sufrimientos unidos a los de Cristo."
        ]
    },
    "M9": {
        "nombre": "Jesús Carga con la Cruz",
        "header": "4to Misterio Doloroso",
        "reflexiones": [
            "Jesús carga la pesada cruz hacia el Calvario. Cada paso es un acto de amor por nuestra salvación. Tomemos nuestra cruz diaria y sigamos a Cristo.",
            "Simón de Cirene ayuda a Jesús a llevar la cruz. Seamos como Simón, dispuestos a ayudar a nuestros hermanos en sus cargas y sufrimientos."
        ]
    },
    "M10": {
        "nombre": "La Crucifixión y Muerte de Jesús",
        "header": "5to Misterio Doloroso",
        "reflexiones": [
            "Jesús muere en la cruz por nuestros pecados. Sus últimas palabras 'Todo está cumplido' sellan nuestra redención. Contemplemos el amor infinito de Dios manifestado en la cruz.",
            "Desde la cruz, Jesús nos da a María como madre: 'Mujer, ahí tienes a tu hijo.' Acojamos a María en nuestra vida como Juan la acogió en la suya."
        ]
    },
    "M11": {
        "nombre": "La Resurrección de Jesús",
        "header": "1er Misterio Glorioso",
        "reflexiones": [
            "Cristo ha resucitado, venciendo la muerte y el pecado. Su resurrección es nuestra esperanza de vida eterna. Aleluya, el Señor ha resucitado verdaderamente.",
            "Las mujeres encuentran el sepulcro vacío y el ángel anuncia: 'No está aquí, ha resucitado.' Que nuestra fe en Cristo resucitado transforme nuestra vida."
        ]
    },
    "M12": {
        "nombre": "La Ascensión de Jesús al Cielo",
        "header": "2do Misterio Glorioso",
        "reflexiones": [
            "Jesús asciende al cielo ante los ojos de sus discípulos. Nos prepara un lugar en la casa del Padre. Vivamos con la mirada puesta en el cielo, nuestra verdadera patria.",
            "Antes de ascender, Jesús promete: 'Estaré con ustedes todos los días hasta el fin del mundo.' Confiemos en su presencia constante en nuestra vida."
        ]
    },
    "M13": {
        "nombre": "La Venida del Espíritu Santo",
        "header": "3er Misterio Glorioso",
        "reflexiones": [
            "El Espíritu Santo desciende sobre María y los apóstoles en Pentecostés. Reciben fortaleza y sabiduría para proclamar el Evangelio. Invoquemos al Espíritu Santo en nuestra vida.",
            "El Espíritu Santo transforma a los apóstoles de temerosos en valientes testigos de Cristo. Pidamos la gracia de ser testigos audaces de nuestra fe."
        ]
    },
    "M14": {
        "nombre": "La Asunción de María",
        "header": "4to Misterio Glorioso",
        "reflexiones": [
            "María es asunta al cielo en cuerpo y alma. Dios glorifica a quien fue fiel hasta el final. Que el ejemplo de María nos anime a perseverar en la santidad.",
            "María, preservada del pecado, no conoce la corrupción del sepulcro. Es primicia de nuestra propia resurrección. Esperemos con fe nuestra glorificación futura."
        ]
    },
    "M15": {
        "nombre": "La Coronación de María como Reina del Cielo",
        "header": "5to Misterio Glorioso",
        "reflexiones": [
            "María es coronada Reina del cielo y de la tierra. Desde su trono intercede por nosotros ante su Hijo. Acudamos a ella con confianza en todas nuestras necesidades.",
            "María reina con Cristo en la gloria eterna. Ella es nuestra Madre y Reina. Consagrémonos a su Inmaculado Corazón y pongamos nuestra vida bajo su protección maternal."
        ]
    }
};

// Rutas base de recursos
const AUDIO_PATH = "assets/Audios";
const IMAGE_PATH = "assets/Caratulas";

// Elementos del DOM
const menuView = document.getElementById("menu-view");
const playerView = document.getElementById("player-view");

const btnDaily = document.getElementById("btn-daily");
const btnGozosos = document.getElementById("btn-gozosos");
const btnDolorosos = document.getElementById("btn-dolorosos");
const btnGloriosos = document.getElementById("btn-gloriosos");
const btnIndividual = document.getElementById("btn-individual");
const chkCantos = document.getElementById("chk-cantos");

const btnBack = document.getElementById("btn-back");
const btnPrev = document.getElementById("btn-prev");
const btnPlayPause = document.getElementById("btn-play-pause");
const btnNext = document.getElementById("btn-next");
const iconPlay = document.getElementById("icon-play");
const iconPause = document.getElementById("icon-pause");

const albumArt = document.getElementById("album-art");
const trackHeader = document.getElementById("track-header");
const trackTitle = document.getElementById("track-title");
const reflectionText = document.getElementById("reflection-text");

const positionSlider = document.getElementById("position-slider");
const timeText = document.getElementById("time-text");
const speedSelect = document.getElementById("speed-select");

const roadmapItems = document.querySelectorAll(".roadmap-item");

// Estado de reproducción
let playlist = [];
let currentTrackIndex = 0;
let isPlaying = false;
let includeCantos = false;
let playbackSpeed = 1.0;
let isSeeking = false;

// Objeto Audio nativo de HTML5
let audio = new Audio();

// Inicialización de Eventos de Audio
audio.addEventListener("play", () => {
    isPlaying = true;
    updatePlayPauseUI();
});

audio.addEventListener("pause", () => {
    isPlaying = false;
    updatePlayPauseUI();
});

audio.addEventListener("timeupdate", () => {
    if (!isSeeking && audio.duration) {
        const percent = (audio.currentTime / audio.duration) * 100;
        positionSlider.value = percent;
        updateTimeDisplay();
    }
});

audio.addEventListener("durationchange", () => {
    updateTimeDisplay();
});

audio.addEventListener("loadedmetadata", () => {
    updateTimeDisplay();
});

audio.addEventListener("ended", () => {
    nextTrack();
});

// Eventos de los Botones del Menú Principal
btnDaily.addEventListener("click", () => {
    const type = getMysteriesForDay();
    buildPlaylist(type);
    startPlayback();
});

btnGozosos.addEventListener("click", () => {
    buildPlaylist("gozosos");
    startPlayback();
});

btnDolorosos.addEventListener("click", () => {
    buildPlaylist("dolorosos");
    startPlayback();
});

btnGloriosos.addEventListener("click", () => {
    buildPlaylist("gloriosos");
    startPlayback();
});

btnIndividual.addEventListener("click", () => {
    const mysteryData = reflectionsData["M"];
    const randomReflection = getRandomReflection(mysteryData.reflexiones);
    playlist = [{
        audio: "M.mp3",
        image: "M.jpg",
        title: mysteryData.nombre,
        header: mysteryData.header,
        reflection: randomReflection,
        type: "misterio"
    }];
    startPlayback();
});

chkCantos.addEventListener("change", (e) => {
    includeCantos = e.target.checked;
});

// Eventos del Reproductor
btnBack.addEventListener("click", () => {
    backToMenu();
});

btnPlayPause.addEventListener("click", () => {
    togglePlayPause();
});

btnPrev.addEventListener("click", () => {
    previousTrack();
});

btnNext.addEventListener("click", () => {
    nextTrack();
});

speedSelect.addEventListener("change", (e) => {
    playbackSpeed = parseFloat(e.target.value);
    audio.playbackRate = playbackSpeed;
});

// Eventos del Slider de Posición
positionSlider.addEventListener("input", () => {
    isSeeking = true;
    // Mostrar tiempo estimado durante el arrastre
    if (audio.duration) {
        const tempTime = (positionSlider.value / 100) * audio.duration;
        timeText.textContent = `${formatTime(tempTime)} / ${formatTime(audio.duration)}`;
    }
});

positionSlider.addEventListener("change", () => {
    if (audio.duration) {
        audio.currentTime = (positionSlider.value / 100) * audio.duration;
    }
    isSeeking = false;
});

// FUNCIONES LÓGICAS

// Obtener un elemento aleatorio de un arreglo
function getRandomReflection(reflectionsArr) {
    if (!reflectionsArr || reflectionsArr.length === 0) return "";
    const index = Math.floor(Math.random() * reflectionsArr.length);
    return reflectionsArr[index];
}

// Determinar tipo de misterio según el día de la semana
function getMysteriesForDay() {
    const day = new Date().getDay(); // 0 = Domingo, 1 = Lunes, etc.
    if (day === 1 || day === 6) { // Lunes (1), Sábado (6)
        return "gozosos";
    } else if (day === 2 || day === 5) { // Martes (2), Viernes (5)
        return "dolorosos";
    } else { // Miércoles (3), Jueves (4), Domingo (0)
        return "gloriosos"; // Nota: Jueves suele ser Luminosos, pero el Python original cae a Gloriosos
    }
}

// Construir la lista de reproducción
function buildPlaylist(rosaryType) {
    playlist = [];

    // 1. Agregar Inicio
    playlist.push({
        audio: "Inicio.mp3",
        image: "Inicio.jpg",
        title: "Inicio del Rosario",
        header: "Oraciones Iniciales",
        reflection: "Preparemos nuestro corazón para rezar el Santo Rosario con devoción.",
        type: "inicio"
    });

    // Determinar rango de misterios
    let startM, endM, canto, cantoImg;
    if (rosaryType === "gozosos") {
        startM = 1;
        endM = 5;
        canto = "CantoGozosos.mp3";
        cantoImg = "CantoGozosos.jpg";
    } else if (rosaryType === "dolorosos") {
        startM = 6;
        endM = 10;
        canto = "CantoDolorosos.mp3";
        cantoImg = "CantoDolorosos.jpg";
    } else { // gloriosos
        startM = 11;
        endM = 15;
        canto = "CantoGloriosos.mp3";
        cantoImg = "CantoGloriosos.jpg";
    }

    // 2. Agregar misterios: Presentación -> Misterio M.mp3 -> Canto (opcional)
    for (let m = startM; m <= endM; m++) {
        const mysteryKey = `M${m}`;
        const mysteryData = reflectionsData[mysteryKey];
        const selectedReflection = getRandomReflection(mysteryData.reflexiones);
        const mysteryImage = `M${m}.jpg`;
        const mysteryTitle = mysteryData.nombre;
        const mysteryHeader = mysteryData.header;

        // A. Presentación del misterio (audio particular M1 a M15)
        playlist.push({
            audio: `${mysteryKey}.mp3`,
            image: mysteryImage,
            title: mysteryTitle,
            header: mysteryHeader,
            reflection: selectedReflection,
            type: "presentacion"
        });

        // B. El misterio en sí (audio M.mp3 que se repite)
        playlist.push({
            audio: "M.mp3",
            image: mysteryImage,
            title: mysteryTitle,
            header: mysteryHeader,
            reflection: selectedReflection,
            type: "misterio"
        });

        // C. Canto si está habilitado
        if (includeCantos) {
            playlist.push({
                audio: canto,
                image: cantoImg, // Usamos la carátula correspondiente del canto
                title: `Canto - ${mysteryTitle}`,
                header: mysteryHeader,
                reflection: selectedReflection,
                type: "canto"
            });
        }
    }

    // 3. Agregar Final
    playlist.push({
        audio: "Final.mp3",
        image: "Final.jpg",
        title: "Final del Rosario",
        header: "Oraciones Finales",
        reflection: "Demos gracias a Dios por este tiempo de oración.",
        type: "final"
    });
}

// Iniciar reproducción de la playlist
function startPlayback() {
    if (playlist.length === 0) return;
    currentTrackIndex = 0;
    
    // Cambiar vista en el UI
    menuView.classList.remove("active");
    playerView.classList.add("active");
    
    loadTrack(currentTrackIndex);
}

// Cargar una pista por índice
function loadTrack(index) {
    if (index < 0 || index >= playlist.length) return;
    currentTrackIndex = index;
    const track = playlist[index];
    
    // Cargar audio
    audio.src = `${AUDIO_PATH}/${track.audio}`;
    audio.playbackRate = playbackSpeed;
    audio.load();
    
    // Reproducir
    audio.play().catch(err => {
        console.log("Auto-reproducción bloqueada por política del navegador. Esperando interacción.", err);
    });
    
    // Actualizar UI
    albumArt.src = `${IMAGE_PATH}/${track.image}`;
    trackHeader.textContent = track.header || "";
    trackTitle.textContent = track.title;
    reflectionText.textContent = track.reflection;
    
    // Resaltar Roadmap
    updateRoadmap(track.type);
}

// Alternar entre reproducir y pausar
function togglePlayPause() {
    if (isPlaying) {
        audio.pause();
    } else {
        audio.play().catch(err => {
            console.error("No se pudo iniciar el audio:", err);
        });
    }
}

// Siguiente pista
function nextTrack() {
    if (currentTrackIndex < playlist.length - 1) {
        loadTrack(currentTrackIndex + 1);
    } else {
        backToMenu();
    }
}

// Pista anterior
function previousTrack() {
    if (currentTrackIndex > 0) {
        loadTrack(currentTrackIndex - 1);
    }
}

// Regresar al menú principal y liberar recursos
function backToMenu() {
    audio.pause();
    audio.src = "";
    isPlaying = false;
    playlist = [];
    currentTrackIndex = 0;
    
    playerView.classList.remove("active");
    menuView.classList.add("active");
}

// Actualizar iconos de Play/Pause en la UI
function updatePlayPauseUI() {
    if (isPlaying) {
        iconPlay.style.display = "none";
        iconPause.style.display = "block";
    } else {
        iconPlay.style.display = "block";
        iconPause.style.display = "none";
    }
}

// Actualizar visor de tiempo actual / total
function updateTimeDisplay() {
    const current = formatTime(audio.currentTime);
    const duration = formatTime(audio.duration || 0);
    timeText.textContent = `${current} / ${duration}`;
}

// Formatear segundos a MM:SS
function formatTime(seconds) {
    if (isNaN(seconds) || seconds === Infinity) return "0:00";
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

// Actualizar el estado visual del Roadmap
function updateRoadmap(currentType) {
    roadmapItems.forEach(item => {
        if (item.getAttribute("data-tag") === currentType) {
            item.classList.add("active");
        } else {
            item.classList.remove("active");
        }
    });
}
