import React, { Component } from 'react';
// import http from '../services/httpservice';
import axios from 'axios';
import config from '../services/config.json';
import {toast} from 'react-toastify';

class Room extends Component {
    state = { 
        guest_can_pause: false,
        votes_count_to_skip: 2,
        isHost: false,
        code: this.props.match.params.roomCode,

    };   
    
    async componentDidMount() {
        console.log("After condiition", this.state.code);
        try {
            const {code} = this.state; 
            console.log("A1");
            if (code !== null) {
                const {data} = await axios.get(config.apiEndpointgetRoom+`${code}`)
                console.log("DATA",data);
                console.log("A2");
                this.setState({
                    guest_can_pause: data.guest_can_pause,
                    votes_count_to_skip: data.votes_count_to_skip,
                    isHost : data.ishost,
                });
            }else {
                console.log("E1");
                this.props.history.replace("/homepage");
            }

        }catch(ex) {
            if (ex.response && ex.response.status >= 400 && ex.response.status <= 500) {
                toast.error("INVALID ROOM ID");
            }
            else{
                toast.error("UNEXPECTED ERROR");
            }
        }
    };



    handlBackButtonPress = async() => {
        try {
            const {data} = await axios.post(config.apiEndpointLeaveRoom);
            console.log("LEAVE ROOM",data);
            this.props.history.replace("/");
        }
        catch(ex) {
            if (ex.response && ex.response.status ===404 || ex.response.status ===400) {
                toast.error("INVALID ROOM ID");
            }
            else{
                toast.error("UNEXPECTED ERROR");
            }
        }

    }



    render() { 
        const {guest_can_pause, code, votes_count_to_skip, isHost} = this.state;

        return (
            <div>
                <h1>{`Room - ${code}`} </h1>
                <div>GUESTS_CAN_PAUSE:{guest_can_pause.toString()}</div>
                <div>VOTES : {votes_count_to_skip.toString()}</div>
                <div>IS_HOST : {isHost.toString()}</div>
                <button className="btn btn-secondary btn-sm" onClick={this.handlBackButtonPress}>Leave Room</button> 
            </div>   
        );
    }
};
 
export default Room;
