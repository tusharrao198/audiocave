import { React, Component } from "react";
import { Redirect, Route, Switch, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.css";
import "font-awesome/css/font-awesome.css";

class Homepage extends Component {
  state = {};

  render() {
    return (
      <div className="container text-center justify-content-center">
        <div>
          <div>
            <h1>Audiocave</h1>
            <small>Listen Music Together</small>
          </div>
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
