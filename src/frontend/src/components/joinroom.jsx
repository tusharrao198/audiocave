import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";
import config from "../services/config.json";

class JoinRoom extends Component {
  state = {
    roomCode: "",
    error: "",
  };

  handleroomButtonPressed = async () => {
    const roomCode = this.state.roomCode;
    console.log("len", roomCode);
    try {
      const { data: data } = await axios.post(config.apiEndpointJoinRoom, {
        code: roomCode,
      });
      console.log("1234-one", data);
      this.props.history.push(`${config.gotoRoom}${roomCode}`);
    } catch (ex) {
      if (
        (ex.response && ex.response.status >= 400) ||
        ex.response.status <= 500
      ) {
        toast.error("INVALID ROOM ID");
      } else {
        toast.error("UNEXPECTED ERROR");
      }
    }
  };

  render() {
    console.log("After IIIIIIi", this.state.roomCode);
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            Join a Room
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <TextField
            error={this.state.error}
            label="Code"
            placeholder="Enter a Room Code"
            value={this.state.roomCode}
            helperText={this.state.error}
            variant="outlined"
            onChange={(e) => this.setState({ roomCode: e.target.value })}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="primary"
            onClick={this.handleroomButtonPressed}
          >
            Enter Room
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button variant="contained" color="secondary" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}

export default JoinRoom;
