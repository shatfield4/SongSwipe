// Importing modules
import React, { useState, useEffect } from "react";
import "./App.css";
  
function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        name: "",
        date: "",
        language: "",
    });

    const currentartist = "placeholder artist name"

    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/data").then((res) =>
            res.json().then((data) => {
                // Setting a data from api
                setdata({
                    name: data.name,
                    date: data.date,
                    language: data.language,
                });
            })
        );
    }, []);
  
    return (
        <div className="App">
            <header className="App-header">
                <h1>Songswipe</h1>

                <form action="/url" method="GET">
                  <p>Enter an artist's name:</p>
                  <input type="text" name="artist_name" placeholder="Justin Bieber"></input>
                  <button type="submit">Submit</button>
                </form>

                <p>Current artist: {currentartist}</p>

                {/*Test image, do not push to prod*/}
                <img src="../static/images/testmonkey.png"></img>

                <form action="/url" method="GET">
                  <button type="submit">Left</button><button type="submit">Right</button>
                </form>

            </header>

        </div>
    );
}
  
export default App;