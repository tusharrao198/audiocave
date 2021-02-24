import React, { Component } from "react";
import axios from "axios";
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

import { Link } from "react-router-dom";
import config from "../services/config.json";
import Room from "./room";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

class CreateRoom extends Component {
  static defaultProps = {
    votes_count_to_skip: 2,
    guest_can_pause: true,
    update: false,
    roomCodeforUpdation: null,
    updateCallback: () => {},
  };

  state = {
    guest_can_pause: this.props.guest_can_pause,
    votes_count_to_skip: this.props.votes_count_to_skip,
    update: this.props.update,
    roomCodeforUpdation: this.props.roomCode,
  };

  handleVotesChange = (e) => {
    this.setState({
      votes_count_to_skip: e.target.value,
    });
    // console.log("VOTES CHANGE", this.state);
  };

  handleGuestCanPauseChange = (e) => {
    // console.log("handleGuestCanPauseChange before", this.state);
    this.setState({
      guest_can_pause: e.target.value === "true" ? true : false,
    });
    // console.log("handleGuestCanPauseChange after", this.state);
  };

  handleRoomButtonPressed = async () => {
    // console.log("ROOM BUTTON", this.state);
    const post_ = {
      votes_count_to_skip: this.state.votes_count_to_skip,
      guest_can_pause: this.state.guest_can_pause,
    };
    const { data: data } = await axios.post(
      config.apiEndpointCreateRoom,
      post_
    );
    // console.log("RES", data.code);
    this.props.history.push(`${config.gotoRoom}${data.code}`);
  };

  handleUpdateButton = async () => {
    // console.log("handleUpdateButton Called");
    const {
      roomCodeforUpdation,
      guest_can_pause,
      votes_count_to_skip,
    } = this.state;
    const post = {
      votes_count_to_skip: votes_count_to_skip,
      guest_can_pause: guest_can_pause,
      code: roomCodeforUpdation,
    };
    // console.log("Updates", post);
    if (this.state.roomCodeforUpdation !== null) {
      const { data } = await axios.patch(
        `${config.apiEndpointUpdateRoom}`,
        post
      );
      // console.log("Update data = ", data);
      toast.success("Settings Updated Successfully");
      this.props.updateCallback();
    } else {
      toast.error("Error Updating Room Details");
    }
  };

  renderUpdateButton() {
    return (
      <Grid item xs={12} align="center">
        <Button
          color="primary"
          variant="contained"
          onClick={this.handleUpdateButton}
        >
          Update Room
        </Button>
      </Grid>
    );
  }

  renderCreateButton() {
    return (
      <Grid item xs={12} align="center">
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            onClick={this.handleRoomButtonPressed}
          >
            Create A Room
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button color="secondary" variant="contained" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }

  render() {
    const { guest_can_pause, votes_count_to_skip, update } = this.state;
    const title = update ? "Update Room Settings" : "Create Room";
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            {title}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl component="fieldset">
            <FormHelperText>
              <div align="center">Guest Control of Playback State</div>
            </FormHelperText>
            <RadioGroup
              row
              defaultValue={this.props.guest_can_pause.toString()}
              onChange={this.handleGuestCanPauseChange}
            >
              <FormControlLabel
                value="true"
                control={<Radio color="primary" />}
                label="Play/Pause"
                labelPlacement="bottom"
              />
              <FormControlLabel
                value="false"
                control={<Radio color="secondary" />}
                label="No Control"
                labelPlacement="bottom"
              />
            </RadioGroup>
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="number"
              onChange={this.handleVotesChange}
              defaultValue={this.props.votes_count_to_skip}
              inputProps={{
                min: 1,
                style: { textAlign: "center" },
              }}
            />
            <FormHelperText>
              <div align="center">Votes Required To Skip Song</div>
            </FormHelperText>
          </FormControl>
        </Grid>
        {update ? this.renderUpdateButton() : this.renderCreateButton()}
      </Grid>
    );
  }
}

export default CreateRoom;
