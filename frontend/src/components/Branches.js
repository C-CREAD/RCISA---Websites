import React from "react";

export default function Branches() {
    const branches = [
        { name: "Pretoria Town", address: "123 Church Street, Pretoria" },
        { name: "Pretoria Silverton", address: "45 Silverton Ave, Pretoria" },
        { name: "Durban", address: "10 Marine Parade, Durban" },
        { name: "Kempton Park", address: "77 Park Lane, Kempton Park" },
        { name: "Mamelodi", address: "99 Freedom Road, Mamelodi" },
        { name: "Polokwane", address: "50 Main Street, Polokwane" },
    ];

    return (
        <section id="branches" className="py-5 bg-light">
            <div className="container">
                <h1 className="text mb-4" style={{ color: "#113357" }}>Our Branches</h1>
                <div className="row">
                    {branches.map((branch, index) => (
                        <div className="col-md-4 mb-3" key={index}>
                            <div className="card h-100 p-3 shadow-sm">
                                <h5>{branch.name}</h5>
                                <p>{branch.address}</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}
