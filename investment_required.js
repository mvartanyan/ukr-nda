async function get_data() {
    r = await fetch("data/investment_required.json");
    return await r.json()
}

get_data().then(data => {
                     lines_chart(document.getElementById("composition"), make_datasets(data));
                   });

function make_datasets(data) {
    datasets = new Array();
    var labels = Object.keys(data)
    years = ['2020', '2025', '2030', '2035', '2040', '2045', '2050']

    for (y in years) {
        d = new Array();
        for (s in data) {
            d.push(data[s][y])
        }

        datasets.push({
                fill: 'stack',
                label: years[y],
                data: d,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(183, 122, 115, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(183, 122, 115, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 2
            },
        )
    }
    console.log(datasets)
    return {'labels':labels, 'datasets':datasets};
}

function lines_chart(canvas, data)
{

    var myChart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: data.datasets,
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    stacked: true,
                    max: 270000,
                }
            }
        }
    });
    window.myChart = myChart;
}
