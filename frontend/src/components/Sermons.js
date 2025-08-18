import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Sermons() {
    const [sermons, setSermons] = useState([]);

    // Calls the 'sermons' app and returns all sermon data
    useEffect(() => {
        axios.get("http://localhost:8000/api/sermons/")
            .then(res => setSermons(res.data.results || []))
            .catch(err => console.error(err));
    }, []);

    return (
        <section id="sermons" className="py-5">

            <div className="container">
                <h1 className="text" style={{ color: "#113357" }}>Latest Sermons</h1>
                <div className="row">
                    {sermons.map(sermon => (
                        <div key={sermon.slug} className="col-md-4 mb-4">
                            <div className="card h-100">
                                {sermon.cover_image && (
                                    <img src={sermon.cover_image} className="card-img-top" alt={sermon.title} />
                                )}
                                <div className="card-body">
                                    <h5 className="card-title">{sermon.title}</h5>
                                    <p>By: {sermon.preacher_name}</p>
                                    <p className="card-text">{sermon.description}</p>
                                    {sermon.audio_file && (
                                        <audio controls src={sermon.audio_file} className="w-100 mt-2"></audio>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
            <hr/>
        </section>
    );
}
