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
// import {withRouter} from 'react-router-dom';
// import { confirmAlert } from "react-confirm-alert";
// import "react-confirm-alert/src/react-confirm-alert.css";

class App extends Component {
  state = {
    roomCode: null,
  };

  async componentDidMount() {
    console.log("Mat BOL ");
    const { data } = await axios.get(`/api/userinroom/`);
    console.log("AB BOL NA ");
    this.setState({ roomCode: data.code });
    const { roomCode } = this.state;
    console.log("ASYNC APP>JS ROOOOM", roomCode);
  }

  handleredirectSession = () => {
    console.log("ROOMCODE::::::", this.state.roomCode);
    if (this.state.roomCode !== null) {
      console.log("SSSSSSS");
      alert("Session found!");
      return <Redirect to={`/room/${this.state.roomCode}`} />;
    } else {
      console.log("IS NULL");
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
      <React.Fragment>
        <ToastContainer />
        <Navbar />
        <main className="container">
          <Switch>
            <Route exact path="/homepage" render={this.handleredirectSession} />
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
      </React.Fragment>
    );
  }
}

export default App;

// <Route exact path="/homepage" render={this.handleredirectSession} />
// <Route
//   exact
//   path="/"
//   render={() => {
//     return this.state.roomCode ? (
//       <Redirect to={`/room/${this.state.roomCode}`} />
//     ) : (
//       <Redirect to="/homepage" />
//     );
//   }}
// />

// <Route
//   path="/room/:roomCode"
//   render={(props) => {
//     return (
//       <Room {...props} leaveRoomCallback={this.clearRoomCode} />
//     );
//   }}
// />

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           HELLO WORLD!
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
