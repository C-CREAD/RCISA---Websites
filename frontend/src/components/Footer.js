import React from "react";

export default function Footer() {
    return (
        <footer className="bg-dark text-white py-4 mt-5">
            <div className="container text-left">
                <label className="mb-0">&copy; {new Date().getFullYear()} Our Church. All Rights Reserved.</label>
                <div className="row">
                    <div className="col-4">
                        <img src="images/Logo-2.png" alt="Logo-2" className="mr-auto" style={{ width: "100%", height: "auto" }}/>
                    </div>
                    <div className="col-8 text-left">
                        <div className="row">
                            <div className="col">
                                <p className="text-justify" style={{ color: "white" }}>We obediently and faithfully witness
                                    the kingdom of God through the inspiration of the Holy Spirit to humankind in order
                                    to address the spiritual, physical and social needs of the people through.</p>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col">
                                <label style={{ color: "#8ca2b4" }}>Email</label><br/>
                                <p style={{ color: "white" }}>info.rcisapta.org</p>
                            </div>
                            <div className="col">
                                <label style={{ color: "#8ca2b4" }}>Call Us</label><br/>
                                <p style={{ color: "white" }}>+27 17 3415 6789</p>
                            </div>
                            <div className="col">
                                <div className="row">
                                    <div className="col-auto">
                                        <ul className="navbar-nav flex-row ml-md-auto">
                                            <li className="nav-item">
                                                <a className="nav-link p-2" href="#" aria-label="Facebook">
                                                    <img src="images/facebook-icon.png"/>
                                                </a>
                                            </li>
                                            <li className="nav-item">
                                                <a className="nav-link p-2" href="#" aria-label="Instagram">
                                                    <img src="images/instagram-icon.png"/>
                                                </a>
                                            </li>
                                            <li className="nav-item">
                                                <a className="nav-link p-2" href="#" aria-label="YouTube">
                                                    <img src="images/youtube-icon.png"/>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
}