// Importing modules
import React, { useState, useEffect } from "react";
import "./styles/App.css";
import ArtistCard from "./ArtistCard"

const API_URL = "hi"

// static placeholder API stuff to let the page render
const artist = {
    "name": "Justin Bieber",
    "photo": "https://i.scdn.co/image/ab676161000051748ae7f2aaa9817a704a87ea36",
    "genre": "Pop"
}

function App() {
    {/*This function should pull API stuff from Flask and pass it to ArtistCard
       TODO: Make API and work on getting the logic to update the render when a new card is ready to render
             Swiping should pull from the top of the list of recommendations and pass it through fetchRecommendations()*/}
    const fetchRecommendations = async (artistrec) => {
        const response = await fetch(`${API_URL}&s=${artistrec}`);
        const data = await response.json();
    
        console.log(data)
    }
    {/* Hook that updates when page is loaded. Right now just passes an artistname (artistrec) to fetchRecommendations()*/}
    useEffect(() => {
        fetchRecommendations('')
    }, [])

    return (
        <div className="App">
            <header className="App-header">
                <span id="title"><h1>Songswipe</h1></span>

                {/* This form is to submit an artist name to us. Can be removed when there's another
                    method to start off the recommendations process */}
                <form method="POST">
                  <p>Enter an artist's name:</p>
                  <input type="text" name="artist_name" placeholder="Justin Bieber"></input>
                  <button type="submit">Submit</button>
                </form>

                {/* Calls ArtistCard.jsx to render the Artist Card */}
                <div className="artistCardContainer">
                    <ArtistCard artist={artist}/>
                </div>

                <div className="swipeButtons">
                  <div className="button">
                    <button onClick={() => {}}>Left</button>
                  </div>
                  <div className="button">
                    <button onClick={() => {}}>Right</button>
                  </div>
                </div>

            </header>

        </div>
    );
}
  
export default App;