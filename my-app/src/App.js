// Importing modules
import React, { useState, useEffect } from "react";
import TinderCard from "react-tinder-card"
//import "./styles/App.css";
  
const onSwipe = (direction) => {
    console.log('You swiped: ' + direction)
}
  
  const onCardLeftScreen = (myIdentifier) => {
    console.log(myIdentifier + ' left the screen')
}

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <span id="title"><h1>Songswipe</h1></span>

                <form action="/url" method="POST">
                  <p>Enter an artist's name:</p>
                  <input type="text" name="artist_name" placeholder="Justin Bieber"></input>
                  <button type="submit">Submit</button>
                </form>

                <p>Current artist: NONE</p>

                <div className="cardContainer">
                    <TinderCard className="swipe" onSwipe={onSwipe} onCardLeftScreen={() => onCardLeftScreen('fooBar')} preventSwipe={['right', 'left']}>fuck</TinderCard>
                </div>

                <div id="swipeButtons">
                  <div class="button">
                    <button type="submit">Left</button>
                  </div>
                  <div class="button">
                    <button type="submit">Right</button>
                  </div>
                </div>

            </header>

        </div>
    );
}
  
export default App;