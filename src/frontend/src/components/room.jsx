import React, { Component } from 'react';
// import http from '../services/httpservice';
import axios from 'axios';
import config from '../services/config.json';


class Room extends Component {
    state = { 
        guest_can_pause: false,
        votes_count_to_skip: 2,
        isHost: false,
        code: this.props.match.params.roomCode,

    };   
    
    async componentDidMount() {
        const {data} = await axios.get(config.apiEndpointgetRoom+`${this.state.code}`)
        console.log("DATA",data);
        this.setState({
            guest_can_pause: data.guest_can_pause,
            votes_count_to_skip: data.votes_count_to_skip,
            isHost : data.ishost,
        });
    };

    render() { 
        const {guest_can_pause, code, votes_count_to_skip, isHost} = this.state;

        return (
            <div>
                <h1>{`Room - ${code}`} </h1>
                <div>GUESTS_CAN_PAUSE:{guest_can_pause.toString()}</div>
                <div>VOTES : {votes_count_to_skip.toString()}</div>
                <div>IS_HOST : {isHost.toString()}</div>
                {/* <button className="btn btn-secondary btn-sm" onClick={() => history.replace("/")}>SAVE</button> */} 
            </div>   
        );
    }
};
 
export default Room;
