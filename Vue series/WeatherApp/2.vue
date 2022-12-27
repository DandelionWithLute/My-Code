<template>
    <div id="app">
        <main>
            <div class="search-box">
                <input 
                type="text" 
                class="search-bar" 
                placeholder="Search..." 
                v-model="query"
                v-on:keypress="fetchWeather"
                />
            </div>

            <div class="weather-wrap">
                <div class="location-box">{{ weather }}</div>
                    <div class="location">{{ weather.name }}, {{weather.sys.country}}</div>
                    <div class="date">Monday 20 January 2020</div>
            </div>

            <div class="weather-box">
                <div class="temp">9°C</div>
                <div class="weather">Rain</div>
            </div>
        </main>
    </div>
</template>

    <script>
    export default {
        name:'app',
        data () {
            return {
                api_key: 'c3fb5d30ea6632b2bb5fd60e81ba6934' ,
                url_base: 'https://api.openweathermaop.org/data/2.5/' ,
                query: '',
                weather: {}
            }
        },
        methods: {
            fetchWeather () {
                if (e.key == "") {
                    fetch(`${this.api_base}weather?q=${this.query}&units=metric&APPID=${this.api_key}`)
                        .then(res => {
                            return res.json();
                        }).then(this.setResults)
                }
            },
            setResults (results) {
                this.weather = results;
            }
        }
    }
    
    </script>

    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'montserrat', sans-serif;
    }
    
    #app {
        background-image: url('./assets/cold-bg.jpg');
        background-size: cover;
        background-position: bottom;
        transition: 0.4s;
    }

    main{
        min-height:100vh;
        padding: 25px;

        background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.75));

    }

    .search-box {
        width: 100%;
        margin: 30px;
    }

    .search-box .search-bar {
        display: block;
        width: 100%;
        padding: 15px;

        color: #313131;
        font-size: 20px;

        appearance: none;
        border: none;
        outLine: none;
        background: none;

        background-color: rgba(255, 255, 255,0.75);
        border-radius: 0px 16px 0px 16px;
        transition: 0.4s;
    }

    .search-box .search-bar:focus {
        box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
        background-color: rgba(255, 255, 255 ,0.75);
    }
    
    .location-box .location {
        color: #FFF;
        font-size: 32px;
        font-weight: 500;
        font-align: center;
        text-shadow: 1px 3px rgba(0, 0, 0, 0.25);
    }

    .location-box .date {
        color: #FFF;
        font-size: 32px;
        font-weight: 300;
        font-style: italic;
        font-align: center;
    }

    .weather-box {
        text-align: center;
    }
    
    .weather-box .temp {
        display: inline-block;
        padding: 10px 25px;
        color: #FFF;
        font-size: 102px;
        font-weight: 900;

        text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
        background-color: rgba(255, 255, 255, 0.25);
        border-radius: 16px;
        margin: 30px 0px;

        box-shadow:3px 6px rgba(0, 0, 0, 0.25);
        
    }

    .weather-box .weather {
        color: #FFF;
        font-size: 48px;
        font-weight: 700;
        font-style: italic;
        text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
    }
    </style>