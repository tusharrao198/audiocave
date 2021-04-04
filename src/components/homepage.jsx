import { React, Component } from "react";
import { Redirect, Route, Switch, Link } from "react-router-dom";

class Homepage extends Component {
  state = {};

  render() {
    return (
      <div className="container text-center justify-content-center">
        <div>
          <h1>HOMEPAGE</h1>
          <Link to="/joinroom">
            <button className="btn btn-primary btn-sm">Join a Room</button>
          </Link>
          <Link to="/createroom">
            <button className="btn btn-success btn-sm">Create a Room</button>
          </Link>
        </div>
      </div>
    );
  }
}

export default Homepage;
