import React, { useCallback, useRef, useState, useEffect } from 'react';
import SpotifyWebPlayer, { STATUS, CallbackState } from 'react-spotify-web-playback';
import ArtistCard from "./ArtistCard";
import "./styles/App.css";
import TinderCard from 'react-tinder-card';

import GitHubRepo from './GitHubRepo';
import {
  Button,
  Disclaimer,
  Form,
  GlobalStyles,
  Heading,
  Input,
  List,
  Player,
  ScopeTitle,
  Selector,
} from './component';

const validateURI = (input: string): boolean => {
  let isValid = false;

  if (input && input.indexOf(':') > -1) {
    const [key, type, id] = input.split(':');

    if (key && type && type !== 'user' && id && id.length === 22) {
      isValid = true;
    }
  }

  return isValid;
};

const parseURIs = (input: string): string[] => {
  const ids = input.split(',');

  return ids.every((d) => validateURI(d)) ? ids : [];
};

const App = () => {
  const scopes = [
    'streaming',
    'user-read-email',
    'user-read-private',
    'user-library-read',
    'user-library-modify',
    'user-read-playback-state',
    'user-modify-playback-state',
  ];
  const savedToken = localStorage.getItem('rswp_token');
  const URIsInput = useRef<HTMLInputElement>(null);
  //const [token, setToken] = useState(savedToken || '');
  const [isPlaying, setIsPlaying] = useState(false);
  const [URIs, setURIs] = useState<string[]>(['spotify:album:51QBkcL7S3KYdXSSA0zM9R']);
  const [validURI, setValidURI] = useState(false);
  const [currentartist, setCurrentArtist] = useState("placeholder artist name");
  const [artistImage, setArtistImage] = useState(require('.//images/testmonkey.png'));

  let previousArtist = "placeholder artist name";

  const [artist, setArtist] = useState({ name: "", photo: "", genre: "", spotify_url: "" });

  let token = '';

  const handleClickLiked = useCallback((e) => {
    e.preventDefault();
    console.log("Liked")
    
    let path = "/data?artist_liked=" + currentartist;
    fetch(
      path)
                  .then((res) => res.json())
                  .then((json) => {
                      const uris = json["song_url"];
                      const name = json["name"];
                      const img_url = json["img_url"];
                      const genre = json["genre"];

                      setArtistImage(img_url);
                      setCurrentArtist(name);

                      previousArtist = name;

                      setArtist({name: name, photo: img_url, genre: genre, spotify_url: uris})

                      setURIs(parseURIs(uris));
                      setIsPlaying(true);

                      if (URIsInput && URIsInput.current) {
                        URIsInput.current.value = uris;
                      }
    })
  }, []);
  const handleClickDisLiked = useCallback((e) => {
    e.preventDefault();

    console.log("Disliked");
  }, []);

  let search = window.location.search;
  search = search.split("=")[1]
  if (search != undefined) {
    token = search;

    if (token) {
      //setToken(token);
      localStorage.setItem('rswp_token', token);
    }
  }

  /*const handleSubmit = useCallback((e) => {
    e.preventDefault();

    const token = e.target.elements[0].value;

    if (token) {
      setToken(token);
      localStorage.setItem('rswp_token', token);
      e.target.reset();
    }
  }, []);*/

  const handleSubmitURIs = useCallback((e) => {
    e.preventDefault();

    if (URIsInput && URIsInput.current) {
      setURIs(parseURIs(URIsInput.current.value));
    }
  }, []);

  const handleChangeURIs = useCallback((e) => {
    e.preventDefault();

    if (URIsInput && URIsInput.current) {
      setValidURI(!!parseURIs(URIsInput.current.value).length);
    }
  }, []);



  const handleClickURIs = useCallback((e) => {
    e.preventDefault();
    const { uris } = e.currentTarget.dataset;

    setURIs(parseURIs(uris));
    setIsPlaying(true);

    if (URIsInput && URIsInput.current) {
      URIsInput.current.value = uris;
    }
  }, []);

  const handleLogIn = useCallback((e) => {
    console.log(token);
    window.open("http://localhost:5000/auth/", "_self");
    //window.close();
  }, []);

  const onSwipe = (direction: string) => {
    if (direction == "right") {
      console.log("Liked")
    
      let path = "/data?artist_liked=" + previousArtist;
      fetch(
        path)
        .then((res) => res.json())
        .then((json) => {
            const uris = json["song_url"];
            const name = json["name"];
            const img_url = json["img_url"];
            const genre = json["genre"];

            setArtistImage(img_url);
            setCurrentArtist(name);

            previousArtist = name;

            setArtist({name: name, photo: img_url, genre: genre, spotify_url: uris})

            setURIs(parseURIs(uris));
            setIsPlaying(true);

            if (URIsInput && URIsInput.current) {
              URIsInput.current.value = uris;
            }
      })
    }
    else {
      console.log("Disliked");
    }
  }
  
  const onCardLeftScreen = (myIdentifier: string) => {
    console.log(myIdentifier + ' left the screen')
  }

  const handleCallback = useCallback(({ type, ...state }: CallbackState) => {
    console.group(`RSWP: ${type}`);
    console.log(state);
    console.groupEnd();

    setIsPlaying(state.isPlaying);

    if (state.status === STATUS.ERROR && state.errorType === 'authentication_error') {
      localStorage.removeItem('rswp_token');
      token = '';
    }
  }, []);

  return (
    <div className="App">
      <GlobalStyles />

      {!token && (
        <React.Fragment>
          <Form onSubmit={handleChangeURIs}>
          <header className="App-header">
            <div className='logInDiv'>
              <span id="title"><h1>Songswipe</h1></span>
              <button onClick={handleLogIn} className="button">
                Log In
              </button>
            </div>
          </header>
          </Form>
        </React.Fragment>
      )}
      {token && (
        <React.Fragment>
          {/*<Form onSubmit={handleSubmitURIs}>
            <Input
              ref={URIsInput}
              name="uris"
              defaultValue={URIs.join(',')}
              placeholder="Enter a Spotify URI"
              onChange={handleChangeURIs}
            />
            <Button type="submit" disabled={!validURI}>
              ✓
            </Button>
      </Form>*/}
          {/*<p>Current artist: {currentartist}</p>
          <img src={artistImage} width = "300" height = "300" alt="Test" />
          <br></br>*/}
          <header className="App-header">
            <span id="title"><h1>Songswipe</h1></span>

            <TinderCard onSwipe={onSwipe} onCardLeftScreen={() => onCardLeftScreen('fooBar')} preventSwipe={['right', 'left']}>
            <div className="artistCardContainer">
              <ArtistCard artist={artist}/>
            </div>
            </TinderCard>

            {/*<div className="swipeButtons">
              <button onClick={handleClickDisLiked} className="button">Left</button>
              <button onClick={handleClickLiked} className="button">Right</button>
            </div>*/}
            <Player key={token}>
              {token && (
                <SpotifyWebPlayer
                  autoPlay={false}
                  callback={handleCallback}
                  persistDeviceSelection
                  play={isPlaying}
                  showSaveIcon
                  syncExternalDevice
                  token={token}
                  styles={{
                    sliderColor: '#1cb954',
                  }}
                  uris={URIs}
                />
              )}
            </Player>
          </header>
        </React.Fragment>
      )}
      <GitHubRepo />
    </div>
  );
};

export default App;
