import React from "react";

const ArtistCard = ({ artist }) => {
    return (
        <div className="artistCard">
        <p>{artist.name}</p>

        <img alt={artist.name}
             src={artist.photo !== "N/A" ? artist.photo : "https://via.placeholder.com/300x400?text=No+Artist+Image+Found!"}
             width="300"
             height="400"></img>

        <p>{artist.genre}</p>
    </div>
    )
}

export default ArtistCard;