import React, { useEffect, useState } from "react";
import axios from "axios";

export default function UpcomingEvents() {
    const [events, setEvents] = useState([]);

    // Calls the 'events' app and returns all Event data
    useEffect(() => {
        axios.get("http://localhost:8000/api/events/")
            .then(res => {
                // console.log(res.data);
                setEvents(res.data.results || []);
            })
            .catch(err => console.error(err));
    }, []);

    return (
        <section className="jumbotron" id="upcoming-events">
            <div className="container">
                <h4 style={{ color: "#0A8F45" }}>Exciting Things to Look Forward To</h4>
                <h1 style={{ color: "#113357" }}>UPCOMING EVENTS</h1>
                <div className="row" style={{ gap: "32px" }}>
                    {Array.isArray(events) && events.map(event => (
                        <div className="column" key={event.slug}>
                            <div className="col-auto" style={{ width: "10%" }}>
                                <h2>{new Date(event.start_time).getDate()}</h2>
                                <h2>{new Date(event.start_time).toLocaleString('default', { month: 'short'})}</h2>
                            </div>
                            <div className="col">
                                <h4>{event.title}</h4>
                                <p style={{ color: "#D9D9D9" }}>Hosted By:</p>
                                <img src="/images/location-icon.png" alt="location" /> {event.location} &emsp;
                                <img src="/images/time-icon.png" alt="time" /> {new Date(event.start_time).toLocaleTimeString()} - {new Date(event.end_time).toLocaleTimeString()}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}