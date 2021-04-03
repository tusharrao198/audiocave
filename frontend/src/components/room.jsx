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
    showSettings: false,
    song_info: {},
    song: null,
    songurl: null,
    postinput: null,
    retrycount: 0,
    is_playing: false,
    bgimage: null,
  };

  async componentDidMount() {
    // this.handleData();
    this.handleRoomData();
    this.handlegetCurrentSong();
    console.log("componentDidMount called");
    // this.interval = setInterval(this.handlegetCurrentSong, 1000);
    // this.interval1 = setInterval(this.room, 1000);
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
        songurl: data.songurl,
      });
    } catch (ex) {
      this.setState({ roomCode: null });
    }
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.roomCode !== this.state.roomCode) {
      if (this.state.roomCode === null) {
        console.log("pokemons state has changed.");
        alert(`ROOM DELETED BY HOST , LEAVE ROOM !`);
        // toast.error("ROOM DELETED BY HOST");
        window.location.reload();
      } else {
        window.location.reload();
      }
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
      if (roomCode !== null) {
        const { data } = await axios.get(
          config.apiEndpointgetRoom + `${roomCode}`
        );
        this.setState({
          guest_can_pause: data.guest_can_pause,
          votes_count_to_skip: data.votes_count_to_skip,
          isHost: data.ishost,
          roomCode: data.RoomCodeinSession,
          is_playing: data.is_playing,
          songurl: data.songurl,
        });
        console.log("ISHOST", this.state.isHost);
      } else {
        // console.log("Room Code is Null");
        this.props.history.replace("/");
      }
    } catch (ex) {
      toast.error("REDIRECTED TO HOMEPAGE");
      this.props.leaveRoomCallback(null);
      this.props.history.replace("/");
    }
  };

  handlBackButtonPress = async () => {
    const { data } = await axios.post(config.apiEndpointLeaveRoom);
    // console.log("LEAVE ROOM", data);
    this.props.leaveRoomCallback(null);
    this.props.history.replace("/");
  };
  //
  handlegetCurrentSong = async () => {
    try {
      const { data } = await axios.get(`/youtube/getlink/`);
      if (this.state.song !== data.song_name) {
        console.log("Current Song_info Added");
        this.setState({ song: data.song_name });
        this.setState({ songurl: data.song_url });
        this.setState({ song_info: data });
        this.setState({ bgimage: data.image_url });
      }
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500 &&
        this.state.retrycount <= 10
      ) {
        this.setState({ retrycount: this.state.retrycount++ });
        console.log("Current Song_info not received");
        this.handlegetCurrentSong();
      }
    }
  };

  handlepostsong = async () => {
    console.log("handlepostsong", this.state.postinput);
    const post = {
      ytlink: this.state.postinput,
      roomCode: this.state.roomCode,
    };
    try {
      const { data } = await axios.post(`/youtube/getlink/`, post);
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
      song_info,
      song,
      postinput,
      is_playing,
      bgimage,
    } = this.state;
    if (showSettings) {
      return this.renderSettings();
    }
    // console.log("is_playing.toString() = ", is_playing);
    return (
      <div
        className="container text-center justify-content-center bgroom"
        style={{
          backgroundImage: `url(${bgimage})`,
          backgroundPosition: "center",
          backgroundSize: "cover",
          backgroundRepeat: "no-repeat",
        }}
      >
        <h3>
          <strong>
            RoomCode: {roomCode} || {isHost ? "HOST" : "USER"}
          </strong>
          <br></br>
          <strong>{is_playing ? "Playing" : "Paused"}</strong>
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
            onChange={(e) => this.setState({ postinput: e.target.value })}
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
