async function get_data() {
    r = await fetch("data/renewables_share.json");
    return await r.json()
}

var year_positions = {'2012':0, '2015':1, '2020':2, '2025':3, '2030':4, '2035':5, '2040':6, '2045':7, '2050':8}

var current_year = '2012';

get_data().then(data => {
                     bar_chart(document.getElementById("composition"), make_datasets(data, current_year));
                   });

function make_datasets(data, year) {
    scenarios = Object.keys(data);
    dataset = new Array();
    for (d in data) {
        dataset.push(data[d][year_positions[year]])
    }
    return {'labels':scenarios, 'data': dataset};
}

function bar_chart(canvas, data)
{
    const d = {
        labels: data['labels'],
        datasets: [{
            data: data['data'],
        }]
    }
    var myChart = new Chart(canvas, {
        type: 'bar',
        data: {
            labels: data['labels'],
            datasets: [{data:data['data'],
                        label: ['Per cent renewables'],
                        backgroundColor: [
                                      'rgba(255, 99, 132, 0.2)',
                                    ],
                        borderColor: [
                          'rgb(255, 99, 132)',
                        ],
                        borderWidth: 2,
                      }],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    stacked: true,
                    max: 100,
                }
            }
        }
    });
    window.myChart = myChart;
    window.myChart = myChart;
}
