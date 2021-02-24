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

class MusicPlayer extends Component {
  state = {};

  handlePauseSong = async () => {
    console.log("handlePauseSong called");
    const promise = await axios.put("http://127.0.0.1:8000/spotify/pausesong/");
    console.log("PAUSE PUT ", promise);
  };

  handlePlaySong = async () => {
    console.log("handlePlayeSong called");
    const promise = await axios.put("http://127.0.0.1:8000/spotify/playsong/");
    console.log("Play PUT ", promise);
  };

  handleSkipSong = async () => {
    console.log("handleSkipSong called");
    const promise = await axios.post("http://127.0.0.1:8000/spotify/skipsong/");
    console.log("SKip POST ", promise);
  };

  render() {
    const songProgress = (this.props.progress / this.props.duration) * 100;

    return (
      <Card container alignItems="center">
        <Grid container alignItems="center">
          <Grid item align="center" xs={4}>
            <img src={this.props.image_url} height="100%" width="100%" />
          </Grid>
          <Grid item align="center" xs={8}>
            <Typography component="h5" variant="h5">
              {this.props.title}
            </Typography>
            <Typography color="textSecondary" variant="subtitle1">
              {this.props.artist_name}
            </Typography>
            <div>
              <IconButton
                onClick={() => {
                  this.props.is_playing
                    ? this.handlePauseSong()
                    : this.handlePlaySong();
                }}
              >
                {this.props.is_playing ? <PauseIcon /> : <PlayArrowIcon />}
              </IconButton>
              <IconButton
                onClick={() => {
                  this.handleSkipSong();
                }}
              >
                <SkipNextIcon />
                {"  "} {this.props.votes} / {this.props.votes_required}
              </IconButton>
            </div>
          </Grid>
        </Grid>
        <LinearProgress variant="determinate" value={songProgress} />
      </Card>
    );
  }
}

export default MusicPlayer;
