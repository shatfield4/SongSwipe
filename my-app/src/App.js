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

    {/* Will replace with logic that shows whatever artist is in queue */}
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
                <span id="title"><h1>Songswipe</h1></span>

                <form action="/url" method="POST">
                  <p>Enter an artist's name:</p>
                  <input type="text" name="artist_name" placeholder="Justin Bieber"></input>
                  <button type="submit">Submit</button>
                </form>

                <p>Current artist: {currentartist}</p>

                {/* Test image, will replace with artist card */}
                <img src="../static/images/testmonkey.png"></img>

                <div id="swipebuttons">
                  <div>
                    <form action="/url" method="GET">
                      <button type="submit">Left</button><button type="submit">Right</button>
                    </form>
                  </div>
                </div>

            </header>

        </div>
    );
}
  
export default App;