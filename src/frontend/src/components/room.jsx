import React, { Component } from "react";
// import http from '../services/httpservice';
import axios from "axios";
import config from "../services/config.json";
import { toast } from "react-toastify";
import {
  Button,
  Grid,
  Typography,
  TextField,
  FormHelperText,
  FormControl,
  Radio,
  RadioGroup,
  FormControlLabel,
} from "@material-ui/core";
import CreateRoom from "./createroom";
import { Redirect, Route, Switch, Link } from "react-router-dom";

class Room extends Component {
  state = {
    guest_can_pause: false,
    votes_count_to_skip: 2,
    isHost: false,
    roomCode: this.props.match.params.roomCode, // getting from url
    // code: null, // will be updated from code
    showSettings: false,
    spotifyAuthenticated: false,
  };

  componentDidMount() {
    this.handleRoomData();
  }

  handleRoomData = async () => {
    console.log("After condiition from url", this.state.roomCode);
    const { roomCode } = this.state;
    console.log("CODEFROM URL/PARAMS START ", roomCode);
    try {
      console.log("A1");
      if (roomCode !== null) {
        const { data } = await axios.get(
          config.apiEndpointgetRoom + `${roomCode}`
        );
        console.log("DATA", data.code);
        console.log("DATA", data.RoomCodeinSession);
        console.log("A2");
        this.setState({
          guest_can_pause: data.guest_can_pause,
          votes_count_to_skip: data.votes_count_to_skip,
          isHost: data.ishost,
          roomCode: data.RoomCodeinSession,
        });
        if (this.state.isHost) {
          this.handleisSpotifyAuthenticated();
        }
      } else {
        console.log("E1");
        this.props.history.replace("/");
      }
    } catch (ex) {
      toast.error("REDIRECTED TO HOMEPAGE");
      this.props.history.replace("/");
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
      ) {
        toast.error("Already Left||INVALID ROOM ID");
      } else {
        toast.error("UNEXPECTED ERROR");
      }
    }
  };

  handleauthenticateUser = async () => {
    console.log("AAAYAYAYAYAYYAYAYAYAY");
    const { data } = await axios.get(
      `http://127.0.0.1:8000/spotify/get-auth-url/`
    );
    console.log("handleauthenticateUser", data, "and data url,= ", data.url);
    window.location.replace(data.url);
    // <Redirect to={data_.url} />;
  };

  handleisSpotifyAuthenticated = async () => {
    const { data } = await axios.get(
      `http://127.0.0.1:8000/spotify/is_Authenticated/`
    );
    console.log("DATa handleisSpotifyAuthenticated", data);
    this.setState({ spotifyAuthenticated: data.Status });
    if (!data.Status) {
      console.log("data.Status", data.Status, "Authenticating");
      this.handleauthenticateUser();
      toast.success("User Authenticated with Spotify");
      console.log("User Authenticated with Spotify");
    }
    console.log("User Authenticated with Spotify");
  };

  handlBackButtonPress = async () => {
    const { data } = await axios.post(config.apiEndpointLeaveRoom);
    console.log("LEAVE ROOM", data);
    this.props.leaveRoomCallback(null);
    this.props.history.replace("/");
  };

  handleisgetCurrentSong = async () => {
    console.log("Current SOng Called");
    const { data } = await axios.get(config.apiEndpointCurrentSong);
  };

  handleShowSettingsUpdate = (value) => {
    console.log("show settings");
    this.setState({
      showSettings: value,
    });
  };

  renderSettings() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <CreateRoom
            update={true}
            votes_count_to_skip={this.state.votes_count_to_skip}
            guest_can_pause={this.state.guest_can_pause}
            roomCode={this.state.roomCode}
            updateCallback={this.handleRoomData}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={() => this.handleShowSettingsUpdate(false)}
          >
            Close
          </Button>
        </Grid>
      </Grid>
    );
  }

  renderSettingsButton = () => {
    return (
      <Grid item xs={12} align="center">
        <Button
          variant="contained"
          color="primary"
          onClick={() => this.handleShowSettingsUpdate(true)}
        >
          Settings
        </Button>
      </Grid>
    );
  };

  render() {
    const {
      guest_can_pause,
      roomCode,
      votes_count_to_skip,
      isHost,
      showSettings,
    } = this.state;
    if (showSettings) {
      return this.renderSettings();
    }
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            RoomCode: {roomCode}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Votes: {votes_count_to_skip}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Guest Can Pause: {guest_can_pause.toString()}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            Host: {isHost.toString()}
          </Typography>
        </Grid>
        {isHost ? this.renderSettingsButton() : null}
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={this.handlBackButtonPress}
          >
            Leave Room
          </Button>
        </Grid>
      </Grid>

      // <div>
      //   <h1>{`Room - ${roomCode}`} </h1>
      //   <div>GUESTS_CAN_PAUSE:{guest_can_pause.toString()}</div>
      //   <div>VOTES : {votes_count_to_skip.toString()}</div>
      //   <div>IS_HOST : {isHost.toString()}</div>
      //   {isHost ? this.renderSettingsButton() : null}
      //   <button
      //     className="btn btn-secondary btn-sm"
      //     onClick={this.handlBackButtonPress}
      //   >
      //     Leave Room
      //   </button>
      // </div>
    );
  }
}

export default Room;
