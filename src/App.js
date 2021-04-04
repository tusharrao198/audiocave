import React, { Component } from "react";
import "./App.css";
import { Redirect, Route, Switch, Link } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import "./index.css";
import axios from "axios";
import JoinRoom from "./components/joinroom";
import Room from "./components/room";
import CreateRoom from "./components/createroom";
import NotFound from "./components/notfound";
import Navbar from "./components/navbar";
import Homepage from "./components/homepage";
// import Background from "./static/images/wall3.jpg";
class App extends Component {
  state = {
    roomCode: null,
  };

  async componentDidMount() {
    console.log("Mat BOL ");
    const { data } = await axios.get(`/api/userinroom/`);
    // console.log("AB BOL NA ");
    this.setState({ roomCode: data.code });
    const { roomCode } = this.state;
    // console.log("ASYNC APP>JS ROOOOM", roomCode);
  }

  handleredirectSession = () => {
    // console.log("ROOMCODE::::::", this.state.roomCode);
    if (this.state.roomCode !== null) {
      // console.log("SSSSSSS");
      alert("Session found!");
      return <Redirect to={`/room/${this.state.roomCode}`} />;
    } else {
      // console.log("IS NULL");
      // this.setState({ roomCode: null });
      return <Homepage />;
    }
  };
  //
  clearRoomCode = (code_) => {
    console.log("leaveRoomCallback data came was ", code_);
    this.setState({
      roomCode: code_,
    });
  };

  render() {
    return (
      <div className="App">
        <header
          className="App-header"
          style={{
            backgroundImage: `url(https://user-images.githubusercontent.com/56690827/109695806-5d05fa00-7bb2-11eb-92c7-8acf6c7d55ac.jpg)`,
            backgroundPosition: "center",
            backgroundSize: "cover",
            backgroundRepeat: "no-repeat",
          }}
        >
          <ToastContainer />
          <Navbar />
          <main className="container">
            <Switch>
              <Route
                exact
                path="/homepage"
                render={this.handleredirectSession}
              />
              <Route path="/joinroom" exact component={JoinRoom} />
              <Route path="/createroom" exact component={CreateRoom} />
              <Route
                path="/room/:roomCode"
                render={(props) => {
                  return (
                    <Room {...props} leaveRoomCallback={this.clearRoomCode} />
                  );
                }}
              />
              <Route path="/notfound" exact component={NotFound} />
              <Redirect from="/" to="/homepage" />
              <Redirect to="/notfound" />
            </Switch>
          </main>
        </header>
      </div>
    );
  }
}

export default App;
