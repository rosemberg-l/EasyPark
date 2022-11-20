function initMap() {
    const ubicacion = new Localizacion(() => {

        const myLatLng = { lat: 6.300545, lng: -75.570269 }
        const myLatLng2 = { lat: 6.343053, lng: -75.565475 }

        var texto = '<h3>Parqueadero Luz</h3>' + '<p>Aceptado: Carro, Moto</p>';

        var texto1 = '<h3>Parqueadero Balcones del Angel</h3>' + '<p>Aceptado: Carro, Moto</p>';

        const options = {
            center: myLatLng,
            zoom: 14
        }
        var map = document.getElementById('map');

        const mapa = new google.maps.Map(map, options);

        const marcador = new google.maps.Marker({
            position: myLatLng,
            map: mapa,
            tittle: "Parqueadero Sena"
        });

        const marcador2 = new google.maps.Marker({
            position: myLatLng2,
            map: mapa,
            tittle: "Parqueadero Sena"
        });


        var informacion = new google.maps.InfoWindow({
            content: texto
        })
        var informacion2 = new google.maps.InfoWindow({
            content: texto1
        })

        marcador.addListener('click', function () {
            informacion.open(mapa, marcador);
        })

        marcador2.addListener('click', function () {
                informacion2.open(mapa, marcador2)
        })
    })
}
