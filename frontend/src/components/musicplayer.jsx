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
    musicurl: this.props.songurl,
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.is_playing !== this.props.play) {
      // console.log("playing state has changed.");
      // toast.error("playing state has changed ", this.state.is_playing);
      this.setState({ is_playing: this.props.play });
      // console.log("in did update ", document.getElementById('audio'));
      if (this.state.is_playing) {
        document.getElementById("audio").play();
      } else {
        document.getElementById("audio").pause();
      }
    }
  }

  handleButton = () => {
    let playpause_btn = document.querySelector(".playpause-track");
    let myAudio = document.getElementById("audio");
    if (myAudio.paused) {
      // console.log("/ false to true")
      // playpause_btn.innerHTML = '<i class="fa fa-pause-circle fa-3x"></i>';
      this.handleplaypauseUpdateButton(true);
    } else {
      // console.log("// true to false")
      // playpause_btn.innerHTML = '<i class="fa fa-play-circle fa-3x"></i>';
      this.handleplaypauseUpdateButton(false);
    }
    if (this.props.play) {
      playpause_btn.innerHTML = '<i class="fa fa-play-circle fa-3x"></i>';
    }
    if (this.props.play === false) {
      playpause_btn.innerHTML = '<i class="fa fa-pause-circle fa-3x"></i>';
    }
  };

  handleplaypauseUpdateButton = async (value) => {
    // console.log("handleplaypauseUpdateButton Called");
    const post = {
      is_playing: value,
      musicurl: this.state.musicurl,
      roomCode: this.state.roomCode,
    };

    try {
      console.log("Sending Updates", post);
      const { data } = await axios.patch("/youtube/update/", post);
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
        2000
      );
    }
  };

  render() {
    return (
      <div className="container">
        <div className="container">
          <img src={this.props.image_url} height="100%" width="100%" />
        </div>
        <div className="container">
          <div>
            <strong>Artist : {this.props.artist}</strong>
          </div>
          <div>
            <strong>Song : {this.props.song_name}</strong>
          </div>
          <div className="buttons">
            <div
              class="playpause-track"
              id="submit_button"
              onClick={this.handledisablebutton}
            >
              <i class="fa fa-play-circle fa-3x"></i>
            </div>
            <audio
              id="audio"
              src={this.props.song_url}
              border="0"
              width="100%"
              height="60"
              autostart="false"
              loop="false"
            ></audio>
          </div>
        </div>
      </div>
    );
  }
}

export default MusicPlayer;
