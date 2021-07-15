import React, { Component} from "react";
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
// import Navbar from "./components/navbar";
import Homepage from "./components/homepage";
// import Background from "./static/images/wall3.jpg";
import config from "./services/config.json";
import swal from 'sweetalert';
import $ from 'jquery';

class App extends Component {
  state = {
    roomCode: null,
  };

  async componentDidMount() {
    // Preloader
    $(window).on('load', function() {
      if ($('#preloader').length) {
        $('#preloader').delay(500).fadeOut('slow', function() {
          $(this).remove();
        });
      }
    });

    try {
      await axios.get(config.apiEndpointUserinRoom).then((res) => {
        if (res.status === 200 && res.data.code !== undefined) {
          this.setState({ roomCode: res.data.code });
        }
      });
    }catch (ex){
      // console.log("roomCode",this.state.roomCode);
    } 
  }

  handleredirectSession = () => {
    if (this.state.roomCode !== null && this.state.roomCode !== undefined) {
      swal("Session found!");
      return <Redirect to={`/room/${this.state.roomCode}`} />;
    } else {
      return <Homepage />;
    }
  };
  
  clearRoomCode = (code_) => {
    // console.log("code_ in App.js", code_);
    this.setState({
      roomCode: code_,
    });
  };

  render() {
    return (
      <div className="App">
        <header
          className="App-header"
          // style={{
            // // backgroundImage: `url(https://user-images.githubusercontent.com/56690827/109695806-5d05fa00-7bb2-11eb-92c7-8acf6c7d55ac.jpg)`,
            // // backgroundImage: `url(https://user-images.githubusercontent.com/56690827/112964664-29dd6900-9166-11eb-813e-7159e71b4ea9.jpg)`,
            // backgroundPosition: "center",
            // backgroundSize: "cover",
            // backgroundRepeat: "no-repeat",
          // }}
        >
          <ToastContainer />
          {/* <Navbar /> */}
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
        <div id="preloader"></div>
      </div>
    );
  }
}

export default App;
