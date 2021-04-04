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

export default

export default function MusicPlayer(props) {
  const { play } = props;
  // state = {
  //   roomCode: props.roomCode,
  //   is_playing: false,
  //   musicurl: props.songurl,
  //   value: false,
  // };
  const player = useRef();

  function Audiofunction(play){
    const player = useRef();
    console.log("type from backend", play);
    if (props.play) {
      player.current.audio.current.play();
    } else {
      player.current.audio.current.pause();
    }
  };


  return (
    <div className="App">
      <AudioPlayer
        autoplay={false}
        src={props.song_url}
        onPlay={props.playpauseUpdate}
        onPause={props.playpauseUpdate}
        ref={player}
      />
    </div>
  );
}
