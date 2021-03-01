import React, { Component } from "react";
import axios from "axios";
import config from "../services/config.json";
import { toast } from "react-toastify";
import { Redirect, Route, Switch, Link } from "react-router-dom";
import {
  Card,
  Button,
  Grid,
  Typography,
  TextField,
  IconButton,
  LinearProgress,
} from "@material-ui/core";
import PlayArrowIcon from "@material-ui/icons/PlayArrow";
import PauseIcon from "@material-ui/icons/Pause";
import SkipNextIcon from "@material-ui/icons/SkipNext";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import AudioPlayer from "material-ui-audio-player";

class MusicPlayer extends Component {
  state = {
    roomCode: this.props.roomCode,
    is_playing: false,
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.is_playing !== this.props.play) {
      // console.log("playing state has changed.");
      // toast.error("playing state has changed ", this.state.is_playing);
      this.setState({ is_playing: this.props.play });
      // console.log("in did update ", document.getElementById('audio'));
      this.state.is_playing
        ? document.getElementById("audio").play()
        : document.getElementById("audio").pause();
    }
  }

  handleButton = () => {
    let myAudio = document.getElementById("audio");
    if (myAudio.paused) {
      // console.log("/ false to true")
      this.handleplaypauseUpdateButton(true);
    } else {
      // console.log("// true to false")
      this.handleplaypauseUpdateButton(false);
    }
  };

  handleplaypauseUpdateButton = async (value) => {
    // console.log("handleplaypauseUpdateButton Called");

    const post = {
      is_playing: value,
      roomCode: this.state.roomCode,
    };

    try {
      console.log("Sending Updates", post);
      const { data } = await axios.patch(
        "http://127.0.0.1:8000/youtube/update/",
        post
      );
      // toast.success(`Song ${this.state.is_playing}ed for user`);
    } catch (ex) {
      toast.error("Error Updating Room Details");
    }
  };

  handledisablebutton = () => {
    if (this.props.isHost || this.props.guest_can_pause) {
      document.getElementById("submit_button").disabled = false;
      this.handleButton();
    } else {
      document.getElementById("submit_button").disabled = true;
      toast.warning("DENIED ACCESS BY HOST");
      setTimeout(
        () => (document.getElementById("submit_button").disabled = false),
        5000
      );
    }
  };

  render() {
    const muiTheme = createMuiTheme({});
    return (
      <Card container alignItems="center">
        <Grid container alignItems="center">
          <Grid item align="center" xs={4}>
            <img src={this.props.image_url} height="100%" width="100%" />
          </Grid>
          <Grid item align="center" xs={8}>
            <Typography component="h5" variant="h5">
              {this.props.song_name}
            </Typography>
            <Typography color="textSecondary" variant="subtitle1">
              {this.props.artist}
            </Typography>
            <ThemeProvider theme={muiTheme}>
              <audio
                controls
                id="audio"
                src={this.props.song_url}
                border="0"
                width="100%"
                height="60"
                autostart="false"
                loop="false"
              ></audio>
            </ThemeProvider>
            <button
              id="submit_button"
              className="btn btn-success btn-sm"
              onClick={this.handledisablebutton}
            >
              {this.props.play ? "Pause" : "Play"}
            </button>
          </Grid>
        </Grid>
      </Card>
    );
  }
}

export default MusicPlayer;
