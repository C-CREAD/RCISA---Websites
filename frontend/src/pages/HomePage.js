import React from "react";
import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import UpcomingEvents from "../components/UpcomingEvents";
import OurStory from "../components/OurStory";
import Sermons from "../components/Sermons";
import Branches from "../components/Branches";
import Footer from "../components/Footer";

export default function HomePage() {
    return (
        <>
            <Navbar />
            <HeroSection />
            <UpcomingEvents />
            <OurStory />
            <Sermons />
            <Branches />
            <Footer />
        </>
    );
}
