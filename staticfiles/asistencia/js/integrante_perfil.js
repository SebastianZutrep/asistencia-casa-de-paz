document.addEventListener("DOMContentLoaded", function () {

    const photo = document.getElementById("profilePhoto");
    if (!photo) return;

    photo.addEventListener("click", function () {

        const ver = confirm(
            "¿Qué deseas hacer?\n\nAceptar = Ver foto\nCancelar = Cambiar foto"
        );

        if (ver) {
            const modalVer = new bootstrap.Modal(
                document.getElementById("verFotoModal")
            );
            modalVer.show();
        } else {
            const modalSubir = new bootstrap.Modal(
                document.getElementById("subirFotoModal")
            );
            modalSubir.show();
        }

    });

});
