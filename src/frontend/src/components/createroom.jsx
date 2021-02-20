import React, { Component } from 'react'
import axios from 'axios';
import {Button, Grid, Typography,TextField, FormHelperText, FormControl, Radio, RadioGroup, FormControlLabel} from '@material-ui/core';

import { Link } from "react-router-dom";
import config from '../services/config.json';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

class CreateRoom extends Component {
    defaultVotes = 2;
    state = { 
        guest_can_pause: true,
        votes_count_to_skip: this.defaultVotes,
    };

    handleVotesChange = (e) => {
        this.setState({
            votes_count_to_skip: e.target.value,
        }); 
        // console.log("VOTES CHANGE", this.state);
    };

    handleGuestCanPauseChange = (e) => {
        // console.log("handleGuestCanPauseChange before", this.state);
        this.setState(
            {guest_can_pause: e.target.value==="true" ? true: false,}
        );
        // console.log("handleGuestCanPauseChange after", this.state);
    };

    handleRoomButtonPressed = async () => {
        console.log("ROOM BUTTON", this.state);
        const post_ = {
            "votes_count_to_skip": this.state.votes_count_to_skip, 
            "guest_can_pause": this.state.guest_can_pause
        }
        const {data:data} = await axios.post(config.apiEndpointCreateRoom, post_);
        console.log("RES",data);
        this.props.history.push(`${config.gotoRoom}${data.code}`);
    };


    render() { 
        return ( 
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component="h4" variant="h4">
                        Create A Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl component="fieldset">
                        <FormHelperText>
                        <div align="center">Guest Control of Playback State</div>
                        </FormHelperText>
                        <RadioGroup
                        row
                        defaultValue="true"
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
                        defaultValue={this.defaultVotes}
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
                <Grid item xs={12} align="center">
                    <Button
                        color="primary"
                        variant="contained"
                        onClick={this.handleRoomButtonPressed}>
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
}
 
export default CreateRoom;
