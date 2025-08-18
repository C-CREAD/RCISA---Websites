import React from "react";

export default function Navbar() {
    return (
        <nav className="navbar navbar-expand navbar-light fixed-top">
            <div className="container">
                <a className="navbar-brand" href="/"><img src="images/Logo.png"/></a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav ms-auto">
                        <li className="nav-item"><a className="nav-link" href="#upcoming-events">Events</a></li>
                        <li className="nav-item"><a className="nav-link" href="#our-story">Our Story</a></li>
                        <li className="nav-item"><a className="nav-link" href="#sermons">Sermons</a></li>
                        <li className="nav-item"><a className="nav-link" href="#branches">Branches</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}
