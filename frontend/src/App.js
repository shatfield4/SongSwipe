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
  
    // Get method
    const apiGet = () => {
        fetch("https://jsonplaceholder.typicode.com/posts").then((response) =>
        response.json()).then((json) => {
            console.log(json);
        });
    };

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
                <h1>React and flask</h1>
                <p>{data.name}</p>
                <p>{data.date}</p>
                <p>{data.language}</p>

                <button onClick={apiGet}>Fetch Api</button>
            </header>
        </div>
    );
}
  
export default App;