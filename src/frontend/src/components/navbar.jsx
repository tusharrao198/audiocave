import React, { Component } from 'react'
import {Link, NavLink} from "react-router-dom";

//stateless functional Component with object destructuring
 
const Navbar = ({}) => {
    return ( 
        <nav className="navbar navbar-expand-lg navbar-light bg-secondary">
            <div className="container-fluid">
                <Link className="navbar-brand" to="/" >Music|Room</Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                
                <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div className="navbar-nav">
                        <NavLink className="nav-link" aria-current="page" to="/homepage">Home</NavLink>
                        <NavLink className="nav-link" to="/joinroom">Join Room</NavLink>
                        <NavLink className="nav-link" to="/createroom">Create Room</NavLink>
                    </div>
                </div>
            </div>
        </nav>     
    );
}

export default Navbar;

