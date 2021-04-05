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

export default function MusicPlayer(props) {
  const { play } = props;
  var player = useRef();

  function Audiofunction(play){
    console.log("type from backend", play);
    if (play==="play") {
      player.current.audio.current.play();
    } else {
      player.current.audio.current.pause();
    }
    return <h1></h1>
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
      {
        props.play? Audiofunction(props.play) : <h1></h1>
      }
    </div>
  );
  
}
