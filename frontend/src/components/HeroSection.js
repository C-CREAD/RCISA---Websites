import React from "react";
import "../styles/home.css";

export default function HeroSection() {
    return (
        <div id="hero-section" style={{ backgroundImage: 'url(images/background-1-1.png)' }}>
            <div className="container">
                <h1 className="display-3" style={{ color: "#FFF" }}>Reformed Church International South Africa</h1>
                <p className="lead" style={{ color: "#FFF" }}>Welcome to our church. A community of faith, hope, and love. Horem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eu turpis molestie, dictum est a, mattis tellus.
                    Sed dignissim, metus nec fringilla accumsan, risus sem sollicitudin lacus, ut interdum tellus elit sed risus. </p>
                {/*<a href="#upcoming-events" className="btn btn-primary btn-lg mt-3">Join Us</a>*/}
                {/*<a href="##upcoming-events" className="btn btn-success btn-lg mt-3">Plan a visit</a>*/}
                {/*<a href="#our-story" className="btn btn-secondary btn-lg mt-3">Our Story</a>*/}
            </div>
        </div>
    );
}
