
<template>
    <div id="app">
        <main>
            <input type="text" class="search-bar" placeholder="Search..." />
        </main>
    </div>
</template>

    <script>
    export default {
        name:'app',
        data () {
            return {
                api_key: 'c3fb5d30ea6632b2bb5fd60e81ba6934'
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

        apprearance: none;
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
    </style>