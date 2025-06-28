document.addEventListener("DOMContentLoaded", function () {
  const canvas = document.getElementById("kategori-chart");

  if (!canvas) return;

  // Ambil data dari atribut data-* pada elemen <canvas>
  const labels = JSON.parse(canvas.dataset.labels || "[]");
  const values = JSON.parse(canvas.dataset.values || "[]");

  const ctx = canvas.getContext("2d");

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Total Kategori', // Label tooltip & legend
        data: values,
        backgroundColor: '#ff623e',
        borderRadius: 8,
        barThickness: 20,
      }]
    },
    options: {
      responsive: true,
      layout: {
        padding: {
          right: 0 // Hilangkan kelebihan ruang kanan
        }
      },
      plugins: {
        legend: { display: false },
        tooltip: { enabled: true }
      },
      scales: {
        x: {
          offset: true, // Atur posisi kategori
          grid: { display: false },
          categoryPercentage: 0.6, // Atur lebar batang
          barPercentage: 0.9,
          ticks: { padding: 10 }
        },
        y: {
          beginAtZero: true,
          ticks: { stepSize: 1 },
          grid: { color: '#eee' }
        }
      }
    }
  });
});