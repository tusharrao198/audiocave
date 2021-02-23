import React, { Component } from "react";
import { Link, NavLink } from "react-router-dom";

//stateless functional Component with object destructuring

const Navbar = ({}) => {
  return (
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <Link className="navbar-brand" to="/homepage">
        Music|Room
      </Link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div className="navbar-nav">
          <NavLink className="nav-link" aria-current="page" to="/homepage">
            Home
          </NavLink>
          <NavLink className="nav-link" to="/joinroom">
            Join Room
          </NavLink>
          <NavLink className="nav-link" to="/createroom">
            Create Room
          </NavLink>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
