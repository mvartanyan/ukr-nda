var scenarios = {
                'NDC2_BAU': 'Business As Usual',
                'NDC2_CNE': 'Climate Neutral Economy',
                'NDC2_Opt_BAU': 'OptMacro - Business As Usual',
                'NDC2_Opt_CNE': 'OptMacro - Climate Neutral Economy',
                'NDC2_Opt_REF': 'OptMacro - Reference (Current Policy)',
                'NDC2_REF': 'Reference (Current Policy)',
                'NDC2_S2C': 'Reference + Carbon Tax',
                'NDC2_S2D': 'Reference + New trajectory of GHG',
                'NDC2_S2F': 'Reference + Other Nuclear Options',
                'NDC2_S2G': 'Reference + Balancing capacities',
                'NDC2_S2S': 'CNE without GHG targets',
                'NDC2_S3E': 'CNE + No New Large Nuclear',
                'NDC2_S3F': 'CNE + Other Nuclear Options',
                'NDC2_S3G': 'CNE + Balancing capacities',
                'UGD_NewPolicy': 'Green Energy Transition',
}

var years = ['2012','2015','2020','2025','2030','2035','2040','2045','2050']


select_scenario = function(scenario) {
    get_data().then(data =>
        {   current_scenario = scenario;
            myChart.data.datasets = make_datasets(data, show_mode, scenario);
            myChart.update();
        });
}

select_mode = function(mode) {
    get_data().then(data =>
        {   show_mode = mode;
            myChart.data.datasets = make_datasets(data, mode, current_scenario);
            if (mode == 'percent') {
                myChart.options.scales.y.max = 100;
            } else {
                delete myChart.options.max;
                myChart.options.scales.y.max = 600;
            }
            myChart.update();
        });
}

scenario_radio = function(el, checked) {
    for (s in scenarios) {
        if (s == checked) {chk = 'checked';} else {chk='';}
        el.innerHTML = el.innerHTML + `
                    <div class="form-check" >
                        <input class="form-check-input"
                               type="radio"
                               name="scenario_choice"
                               onclick="select_scenario(this.id);"
                               id="${s}"
                               ${chk}>
                        <label class="form-check-label" for="${s}">
                            ${scenarios[s]}
                        </label>
                    </div>
            `
    }
}

select_year = function(year) {
    get_data().then(data =>
        {   current_year = year;
            scen_keys = Object.keys(scenarios)
            console.log(years)
            console.log(year)
            //myChart.data.datasets = [{data:make_datasets(data, year)['data']}];
            for (s in scenarios) {
                console.log(s);
                console.log(data[scenarios[s]][years.indexOf(year)])
                myChart.data.datasets[0].data[s]=data[scenarios[s]][years.indexOf(year)];
            }
            console.log(myChart)
            myChart.update();
        });
}

year_radio = function(el, checked) {
    for (y in years) {
        if (years[y] == checked) {chk = 'checked';} else {chk='';}
        el.innerHTML = el.innerHTML + `
                        <input class="btn-check"
                               type="radio"
                               name="scenario_choice"
                               onclick="select_year(this.id);"
                               id="${years[y]}"
                               ${chk}>
                        <label class="btn btn-outline-primary" for="${years[y]}">
                            ${years[y]}
                        </label>
                    </div>
            `
    }
}