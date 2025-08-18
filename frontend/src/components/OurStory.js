import React from "react";
import "../styles/home.css";

export default function OurStory() {
    return (
        <section id="our-story" className="jumbotron" style={{ backgroundImage: 'url(images/background-1-2.png)' }}>
            <div className="container">
                <h1 style={{ color: "#FFF" }}>Our Story</h1>
                <div className="d-flex flex-row-reverse">
                    <div className="col-auto">
                        <img src="images/our-story-1.jpg" id="our-story-picture"/>
                    </div>
                    <div className="col">
                        <div className="row">
                            <p className="text-justify" style={{ color: "#FFF" }}>
                                Our church has been serving the community for over 50 years, spreading the message of
                                love,
                                hope, and faith.
                                We believe in making a positive impact in the lives of everyone we meet, and we welcome
                                you to
                                be part of our family.
                            </p>
                        </div>
                    </div>
                </div>
                <a href="#" className="btn btn-success btn-lg" style={{ color: "#FFF" }}>Our Story</a>
            </div>
        </section>
    );
}
