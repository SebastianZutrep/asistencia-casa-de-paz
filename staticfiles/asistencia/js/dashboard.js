document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("asistenciaChart");
    if (!canvas) return;

    canvas.style.height = "100%";
    canvas.style.width = "100%";

    const labels = JSON.parse(canvas.dataset.labels || "[]");
    const data = JSON.parse(canvas.dataset.data || "[]");

    if (labels.length === 0 || data.length === 0) {
        console.warn("No hay datos para mostrar en la gráfica.");
        return;
    }

    const ctx = canvas.getContext("2d");

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: "Asistencia por reunión",
                data: data,
                borderWidth: 2,
                tension: 0.35,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: "top"
                }
            },
            scales: {
                x: {
                    ticks: {
                        autoSkip: true,
                        maxTicksLimit: 10,
                        maxRotation: 45,
                        minRotation: 30
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        precision: 0
                    }
                }
            }
        }
    });

});