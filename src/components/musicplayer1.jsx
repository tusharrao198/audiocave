import React, { Component, useEffect, useState, useRef } from "react";
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
// import { createMuiTheme, ThemeProvider } from "@material-ui/core";
// import AudioPlayer from "material-ui-audio-player";
// import { makeStyles, Box, Paper } from "@material-ui/core";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";

class MusicPlayer extends Component {
  state = {
    roomCode: this.props.roomCode,
    is_playing: false,
    musicurl: this.props.songurl,
    value: false,
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.is_playing !== this.props.play) {
      // console.log("playing state has changed.", this.state.is_playing);
      // toast.error("playing state has changed ", this.state.is_playing);
      this.setState({ is_playing: this.props.play });
      // console.log("in did update ", this.state.is_playing);
      if (this.state.is_playing) {
        // document.getElementById("audio").play();
      } else {
        // document.getElementById("audio").pause();
      }
    }
  }

  handleButton = (playing_state, audio) => {
    console.log("222222", playing_state === "play");
    if (playing_state == "play") {
      console.log("PLAY", audio.paused);
      this.handleaudiofunction(playing_state);
      this.handleplaypauseUpdateButton(true);
    } else {
      console.log("PAUSE", audio.paused);
      this.handleaudiofunction(playing_state);
      this.handleplaypauseUpdateButton(false);
    }
  };

  handleplaypauseUpdateButton = async (value) => {
    console.log("handleplaypauseUpdateButton Called", value);
    const post = {
      is_playing: value,
      musicurl: this.props.songurl,
      roomCode: this.state.roomCode,
    };

    try {
      console.log("Sending Updates", post);
      const { data } = await axios.patch("/youtube/update/", post);
    } catch (ex) {
      toast.error("Error Updating Room Details");
    }
  };

  handledisablebutton = (e) => {
    // console.log(e);
    // if (this.props.isHost || this.props.guest_can_pause) {
    //   // document.getElementById("submit_button").disabled = false;
    //   console.log("111111111111111111111111");
    //   // console.log("ASDF", e.target);
    //   this.handleButton(e.type, e.target);
    // } else {
    //   // document.getElementById("submit_button").disabled = true;
    //   toast.warning("DENIED ACCESS BY HOST");
    //   // setTimeout(
    //   //   () => (document.getElementById("submit_button").disabled = false),
    //   //   2000
    //   // );
    // }
  };

  handleaudiofunction = (playing_state) => {
    // console.log("2 - handleaudiofunction");
    if (playing_state == "play") {
      // console.log("PLAY", audio.paused);
      // player.current.audio.current.play();
    } else {
      // console.log("PAUSE", audio.paused);
      // player.current.audio.current.pause();
    }
  };

  handleAudioChange = (event) => {
    console.log("oncjhange", event);
    event.target.paused = false;
  };

  render = () => {
    // var player = useRf();
    // console.log("playerPP", player);
    const { song_url } = this.props;
    return (
      <div>
        <div className="container">
          <img src={this.props.image_url} height="100%" width="100%" />
        </div>
        <AudioPlayer
          autoPlay={false}
          autoPlayAfterSrcChange={true}
          src={this.props.song_url}
          onPlaying={this.handleAudioChange}
          // onPlay={(e) => {
          //   this.handledisablebutton(e);
          //   // console.log("e play", e);
          // }}
          onPlay={this.handledisablebutton}
          onPause={(e) => {
            this.handledisablebutton(e);
            // console.log("epause", e);
          }}
          // ref={player}
        ></AudioPlayer>

        <button
          className="btn btn-dange btn-sm"
          // onClick={this.handledisablebutton(player)}
        ></button>
      </div>
    );
  };
}

export default MusicPlayer;
