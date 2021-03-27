import React, { Component } from "react";
// import http from '../services/httpservice';
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import config from "../services/config.json";
import { toast } from "react-toastify";
import "../index.css";
import CreateRoom from "./createroom";
import MusicPlayer from "./musicplayer";
import ChatRoom from "./chatroom";
import { Redirect, Route, Switch, Link } from "react-router-dom";

class Room extends Component {
  state = {
    guest_can_pause: false,
    votes_count_to_skip: 2,
    isHost: false,
    roomCode: this.props.match.params.roomCode, // getting from url
    // code: null, // will be updated from code
    showSettings: false,
    // spotifyAuthenticated: false,
    song_info: {},
    song: null,
    songurl: null,
    retrycount: 0,
    is_playing: false,
  };

  async componentDidMount() {
    // this.handleData();
    this.handleRoomData();
    this.handlegetCurrentSong();
    console.log("componentDidMount called");
    // this.interval = setInterval(this.handlegetCurrentSong, 1000);
    this.interval1 = setInterval(this.room, 1000);
  }

  room = async () => {
    try {
      const { data } = await axios.get(
        config.apiEndpointgetRoom + `${this.state.roomCode}`
      );
      this.setState({
        guest_can_pause: data.guest_can_pause,
        votes_count_to_skip: data.votes_count_to_skip,
        isHost: data.ishost,
        is_playing: data.is_playing,
        song_url: data.songurl,
      });
      // console.log(
      //   "IN ROOM CALL INTERVAL " , this.state.is_playing
      // )
    } catch (ex) {
      // toast.error("REDIRECTING TO HOMEPAGE");
      this.setState({ roomCode: null });
      // console.log("IN ROOM INTERVAL FOUND ROOM CODE = ", this.state.roomCode);
    }
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.roomCode !== this.state.roomCode) {
      console.log("pokemons state has changed.");
      // toast.error("ERROR");
      alert(`ROOM DELETED BY HOST , LEAVE ROOM !`);
      // toast.error("ROOM DELETED BY HOST");
      window.location.reload();
    }
    if (prevState.is_playing !== this.state.is_playing) {
      console.log("isPlaying updated by interval ", this.state.is_playing);
    }
    if (prevState.songurl !== this.state.songurl) {
      this.handlegetCurrentSong();
    }
  }

  handleRoomData = async () => {
    console.log("After condiition from url", this.state.roomCode);
    const { roomCode } = this.state;
    console.log("CODEFROM URL/PARAMS START ", roomCode);
    try {
      // console.log("A1");
      if (roomCode !== null) {
        const { data } = await axios.get(
          config.apiEndpointgetRoom + `${roomCode}`
        );
        // console.log("DATA", data.code);
        // console.log("DATA", data.RoomCodeinSession);
        // console.log("A2");
        this.setState({
          guest_can_pause: data.guest_can_pause,
          votes_count_to_skip: data.votes_count_to_skip,
          isHost: data.ishost,
          roomCode: data.RoomCodeinSession,
          is_playing: data.is_playing,
          song_url: data.songurl,
        });
        console.log("ISHOST", this.state.isHost);
        if (this.state.isHost) {
          // this.handleisSpotifyAuthenticated();
        }
      } else {
        // console.log("Room Code is Null");
        this.props.history.replace("/");
      }
    } catch (ex) {
      toast.error("REDIRECTED TO HOMEPAGE");
      this.props.leaveRoomCallback(null);
      this.props.history.replace("/");
      // if (
      //   ex.response &&
      //   ex.response.status >= 400 &&
      //   ex.response.status <= 500
      // ) {
      //   toast.error("Already Left | INVALID ROOM ID");
      // } else {
      //   toast.error("UNEXPECTED ERROR");
      // }
    }
  };

  // handleauthenticateUser = async () => {
  //   // console.log("AAAYAYAYAYAYYAYAYAYAY");
  //   const { data } = await axios.get(
  //     `http://127.0.0.1:8000/spotify/get-auth-url/`
  //   );
  //   // console.log("handleauthenticateUser", data, "and data url,= ", data.url);
  //   toast.success("User Authenticated with Spotify");
  //   window.location.replace(data.url);
  //   // <Redirect to={data_.url} />;
  // };
  //
  // handleisSpotifyAuthenticated = async () => {
  //   const { data } = await axios.get(
  //     `http://127.0.0.1:8000/spotify/is_Authenticated/`
  //   );
  //   // console.log("DATa handleisSpotifyAuthenticated", data);
  //   this.setState({ spotifyAuthenticated: data.Status });
  //   if (!data.Status) {
  //     // console.log("data.Status", data.Status, "Authenticating");
  //     // this.handleauthenticateUser();
  //     // console.log("User Authenticated with Spotify");
  //   }
  //   // console.log("User Authenticated with Spotify");
  // };

  handlBackButtonPress = async () => {
    const { data } = await axios.post(config.apiEndpointLeaveRoom);
    // console.log("LEAVE ROOM", data);
    this.props.leaveRoomCallback(null);
    this.props.history.replace("/");
  };
  //
  handlegetCurrentSong = async () => {
    // console.log("Current Song Called");
    try {
      const { data } = await axios.get(
        `http://127.0.0.1:8000/youtube/getlink/`
      );
      // console.log("Received Current Song-info", data);
      if (this.state.song !== data.song_name) {
        console.log("Current Song_info Added");
        this.setState({ song: data.song_name });
        this.setState({ songurl: data.song_url });
        this.setState({ song_info: data });
      }
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500 &&
        this.state.retrycount <= 10
      ) {
        this.setState({ retrycount: this.state.retrycount++ });
        // console.log("Current Song_info not received");
        this.handlegetCurrentSong();
        // console.log("WORKKING ON IT ");
        // toast.error("Already Left | INVALID ROOM ID");
      }
    }
  };

  handlepostsong = async () => {
    const post = {
      ytlink: this.state.songurl,
      roomCode: this.state.roomCode,
    };

    try {
      const { data } = await axios.post(
        `http://127.0.0.1:8000/youtube/getlink/`,
        post
      );
      this.handlegetCurrentSong();
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
      ) {
        toast.error("Error Posting link");
      }
    }
  };

  handleShowSettingsUpdate = (value) => {
    // console.log("show settings");
    this.setState({
      showSettings: value,
    });
  };

  renderSettings() {
    return (
      <div className="container">
        <div className="container-fluid">
          <CreateRoom
            update={true}
            votes_count_to_skip={this.state.votes_count_to_skip}
            guest_can_pause={this.state.guest_can_pause}
            roomCode={this.state.roomCode}
            updateCallback={this.handleRoomData}
          />
        </div>
        <button
          className="btn btn-primary btn-sm"
          onClick={() => this.handleShowSettingsUpdate(false)}
        >
          Close
        </button>
      </div>
    );
  }

  renderSettingsButton = () => {
    return (
      <div className="container">
        <button
          className="btn btn-primary btn-sm"
          onClick={() => this.handleShowSettingsUpdate(true)}
        >
          Settings
        </button>
      </div>
    );
  };

  render() {
    const {
      guest_can_pause,
      roomCode,
      votes_count_to_skip,
      isHost,
      showSettings,
      // spotifyAuthenticated,
      song_info,
      song,
      is_playing,
    } = this.state;
    if (showSettings) {
      return this.renderSettings();
    }
    // console.log("is_playing.toString() = ", is_playing);
    return (
      <div className="container text-center justify-content-center bgroom">
        <h3>
          <strong>
            RoomCode: {roomCode} || {isHost ? "HOST" : "USER"}
          </strong>
        </h3>
        <div class="container-fluid">
          <div class="row">
            <div class="col-lg-6">
              <MusicPlayer
                song={this.state.song}
                songurl={this.state.songurl}
                roomCode={this.state.roomCode}
                play={this.state.is_playing}
                guest_can_pause={guest_can_pause}
                isHost={isHost}
                {...this.state.song_info}
                updateplayplauseCallback={this.handleRoomData}
              />
            </div>
            <div class="col-lg-6">
              <ChatRoom roomCode={roomCode} />
            </div>
          </div>
        </div>
        <div>
          <strong>Votes: {votes_count_to_skip}</strong>
        </div>
        {isHost ? this.renderSettingsButton() : null}
        <button
          className="btn btn-danger btn-sm"
          onClick={this.handlBackButtonPress}
        >
          Leave Room
        </button>

        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            POST LINK
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <TextField
            error={this.state.error}
            label="Code"
            placeholder="Enter youtube url with 11 digits"
            helperText={this.state.error}
            variant="outlined"
            onChange={(e) => this.setState({ songurl: e.target.value })}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="primary"
            onClick={this.handlepostsong}
          >
            Post
          </Button>
        </Grid>
      </div>
    );
  }

  componentWillUnmount() {
    console.log("componentWillUnmount called");
    // clearInterval(this.interval);
    clearInterval(this.interval1);
    console.log("componentWillUnmount called done");
  }
}

export default Room;
//
// <div>
//   <strong>isplaying: {is_playing.toString()}</strong>
// </div>
// <div>
//   <strong>Guest Can Pause: {guest_can_pause.toString()}</strong>
// </div>
