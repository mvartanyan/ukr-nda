async function get_data() {
    r = await fetch("data/ukraine_emissions.json");
    return await r.json()
}

var show_mode = 'values';
var current_scenario = 'NDC2_BAU';

get_data().then(data => {
                     lines_chart(document.getElementById("composition"), make_datasets(data, show_mode, current_scenario));
                   });

function make_datasets(data, mode, scenario) {
    scenario_data = data[mode][scenario];
    datasets = new Array();
    for (d in scenario_data) {
        datasets.push({
                fill: 'stack',
                label: d,
                data: scenario_data[d],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 2
            },
        )
    }
    return datasets;
}

function lines_chart(canvas, data)
{

    var myChart = new Chart(canvas, {
        type: 'line',
        data: {
            labels: ['2012', '2015', '2020', '2025', '2030', '2035', '2040', '2045', '2050'],
            datasets: datasets,
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    stacked: true,
                    max: 600,
                }
            }
        }
    });
    window.myChart = myChart;
}


