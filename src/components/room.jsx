import React, { Component } from "react";
// import http from '../services/httpservice';
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import config from "../services/config.json";
import { toast } from "react-toastify";
import "../index.css";
import CreateRoom from "./createroom";
import MusicPlayer from "./musicplayer";
import { Redirect, Route, Switch, Link } from "react-router-dom";
import ChatRoom from './chatroom';

class Room extends Component {
  state = {
    guest_can_pause: false,
    // votes_count_to_skip: 2,
    isHost: false,
    roomCode: this.props.match.params.roomCode,
    // showSettings: false,
    song_info: {},
    song: null,
    songurl: null,
    postinput: null,
    retrycount: 0,
    is_playing: false,
    bgimage: null,
    send_status: null,
    messages: [],
    newmessage: null,
    chatSocket: null,
    playPausemessage: "",
    leaveRoomStatus: false,
    updateSong: false,
  };

  async componentDidMount() {
    const { roomCode } = this.props.match.params;
    // console.log("rooo", roomCode)
    let chatSocket=null;
    async function createSocket(){
      chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + roomCode + "/"
      );
      return chatSocket
    }

    createSocket().then(_=>{
      // console.log("created socket", _)
      this.setState({chatSocket: _});
    })

    chatSocket.onclose = async(e) => {
      console.error("Chat socket closed unexpectedly");
    };

    chatSocket.onmessage = async (e) => {
      const data = JSON.parse(e.data);
      // console.log("data received",data);
      this.handleshowdata(data);
    };

    document.querySelector("#chat-message-input").focus();
    document.querySelector("#chat-message-input").onkeyup = function (e) {
      if (e.keyCode === 13) {
        // enter, return
        document.querySelector("#chat-message-submit").click();
      }
    };

    document.querySelector("#chat-message-submit").onclick = (e) => {
      const messageInputDom = document.querySelector("#chat-message-input");
      const message = messageInputDom.value;
      chatSocket.send(
        JSON.stringify({
          message: message,
          playPausemessage: "",
          leaveRoom: this.state.leaveRoomStatus,
          updateSong: this.state.updateSong,
        })
      );
      messageInputDom.value = "";
    };    

    if (roomCode !== null && roomCode !== undefined) {
      this.handleRoomData();
      console.log("componentDidMount called");
    } 
  }

  handleshowdata = async (e) => {
    let node = document.createElement("p");
    let textnode = document.createTextNode(e.message);
    node.appendChild(textnode);
    if (document.getElementById("chat-log") !==null){
      document.getElementById("chat-log").appendChild(node);
      try {
        this.setState({playPausemessage : e.playPausemessage});
        this.setState({leaveRoomStatus : e.leaveRoom});
        this.setState({updateSong : e.updateSong});
      }catch(ex) {
      console.log("error in recieving", ex); 
      }
    }
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.roomCode !== this.state.roomCode) {
      if (this.state.roomCode === null) {
        alert(`ROOM DELETED BY HOST , LEAVE ROOM !`);
        window.location.reload();
      } else {
        window.location.reload();
      }
    }
    if (prevState.is_playing !== this.state.is_playing) {
      console.log("isPlaying updated by interval ", this.state.is_playing);
    }
    if (prevState.songurl !== this.state.songurl) {
      this.handlegetCurrentSong();
    }
    if (prevState.leaveRoomStatus !== this.state.leaveRoomStatus) {
      this.handleLeaveRoom();
    }
    if (prevState.updateSong !== this.state.updateSong) {
      console.log("updatesong state changed from ",prevState.updateSong , "to => ", this.state.updateSong);
      this.handlegetCurrentSong();
    }  
  }

  handleRoomData = async () => {
    try {
      if (this.state.roomCode !== null) {
        const { data } = await axios.get(
          config.apiEndpointgetRoom + `${this.state.roomCode}`
        );
        this.setState({
          guest_can_pause: data.guest_can_pause,
          votes_count_to_skip: data.votes_count_to_skip,
          isHost: data.ishost,
          roomCode: data.RoomCodeinSession,
          is_playing: data.is_playing,
          songurl: data.songurl,
        });
        console.log("ISHOST", this.state.isHost);
        this.handlegetCurrentSong();
      } else {
        console.log("//Room Code is Null");
        this.props.history.replace("/");
      }
    } catch (ex) {
      toast.error("REDIRECTED TO HOMEPAGE");
      this.props.leaveRoomCallback(null);
      this.props.history.replace("/");
    }
  };

  handlBackButtonPress = async () => {
    await axios.post(config.apiEndpointLeaveRoom).then((data, err)=> {
      if(data.status==200){
        this.props.leaveRoomCallback(null);
        if (this.state.isHost){ // if host left the room then delete room
          console.log("// if host left the room then delete room");
        }else{
          this.props.history.replace("/");
        }
      }else {
        console.log('error',err);
      }
    });
    this.send_leaveRoom_status(true);
  };

  handleLeaveRoom = () =>{
    console.log("called handleLeaveRoom");
    toast.error("REDIRECTED TO HOMEPAGE");
    this.props.history.replace("/");
    return <h1></h1>
  }

  handlegetCurrentSong = async () => {
    try {
      const { data } = await axios.get(`/youtube/getlink/`);
      if (this.state.song !== data.song_name) {
        console.log("Current Song_info Added");
        this.setState({ song: data.song_name });
        this.setState({ songurl: data.song_url });
        this.setState({ song_info: data });
        this.setState({ bgimage: data.image_url });
      }          
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
        // this.state.retrycount <= 2
      ) {
        // this.setState({ retrycount: this.state.retrycount++ });
        // 7017
      }
    }
  };

  handlepostsong = async () => {
    console.log("posting song")
    const post = {
      ytlink: this.state.postinput,
      roomCode: this.state.roomCode,
    };
    try {
      const { data } = await axios.post(`/youtube/getlink/`, post);
      this.handlegetCurrentSong();
      // if post successfull then send update song status via websocket

    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
      ) {
        toast.error("Error Posting link / Try Another Song");
      }
    }
    this.send_songUpdate(true);
  };

  handlepostsong = async () => {
    console.log("posting song")
    const post = {
      ytlink: this.state.postinput,
      roomCode: this.state.roomCode,
    };
    try {
      await axios.post(`/youtube/getlink/`, post).then((res, err)=>{
        if (res.status==200){
          this.handlegetCurrentSong();
          this.send_songUpdate(true);
        }else{
          console.log("error",err);
        }
      })
      // if post successfull then send update song status via websocket

    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
      ) {
        toast.error("Error Posting link / Try Another Song");
      }
    }
  };

  send_playPause_status = (status) => {
    const {chatSocket,updateSong, leaveRoomStatus} = this.state;
    chatSocket.send(
      JSON.stringify({
        message: "",
        playPausemessage: status,
        leaveRoom: leaveRoomStatus,
        updateSong: updateSong,
      })
    );
  }

  handleplaypauseUpdateButton = async (event) => {
    let value = null;
    if (event.type === "play") {
      // console.log("PLAY SEND");
      value = true;
    } else {
      // console.log("pause send");
      value = false;
    }
    const post = {
      is_playing: value,
      musicurl: this.state.songurl,
      roomCode: this.state.roomCode,
    };
    try {
      const { data } = await axios.patch("/youtube/update/", post);
    } catch (ex) {
      toast.error("Error Updating Room Details");
    }
    this.send_playPause_status(event.type);
  };

  send_songUpdate = (res) => {
    console.log("SENDING SONG UPDATE ", res);
    const {chatSocket, leaveRoomStatus, updateSong} = this.state;
      chatSocket.send(
        JSON.stringify({
          message: "",
          playPausemessage: "",
          leaveRoom: leaveRoomStatus,
          updateSong: res,
        })
    );
  }

  send_leaveRoom_status = (e) => {
    const {chatSocket, updateSong} = this.state;
      chatSocket.send(
        JSON.stringify({
          message: "",
          playPausemessage: "",
          leaveRoom: e,
          updateSong: updateSong,
        })
    );
  }

  handleNewUserMessage = async(e) => {
    const {chatSocket, messages, leaveRoomStatus, updateSong} = this.state;
    this.setState({messages: [...messages, e]})
    this.setState({newmessage: e});
    chatSocket.send(
      JSON.stringify({
        message: e,
        playPausemessage: "",
        leaveRoom: leaveRoomStatus,
        updateSong: updateSong,
      })
    );
  }

  render() {
    const {
      roomCode,
      isHost,
      showSettings,
      is_playing,
      bgimage,
    } = this.state;
    if (showSettings) {
      return this.renderSettings();
    }
    return (
      <div
        className="container text-center justify-content-center bgroom"
        style={{
          backgroundImage: `url(${bgimage})`,
          backgroundPosition: "center",
          backgroundSize: "cover",
          backgroundRepeat: "no-repeat",
        }}
      >
        <ChatRoom handleNewUserMessage={this.handleNewUserMessage} newmessage={this.state.newmessage}/>
        <h3>
          <strong>
            RoomCode: {roomCode} || {isHost ? "HOST" : "USER"}
          </strong>
          <br></br>
          <strong>{is_playing ? "Playing" : "Paused"}</strong>
        </h3>
        <div className="container-fluid">
          <div className="row">
            <div className="col-lg-6">
              <MusicPlayer
                song={this.state.song}
                songurl={this.state.songurl}
                roomCode={this.state.roomCode}
                play={this.state.playPausemessage}
                guest_can_pause={this.state.guest_can_pause}
                isHost={isHost}
                send_status = {this.state.send_status}
                {...this.state.song_info}
                playpauseUpdate={this.handleplaypauseUpdateButton}
              />
            </div>
            <div className="col-lg-6">
            <div className="padding">
                <div className="card-header">
                    <h4 className="card-title">
                    <strong>Real-Time Chat</strong>
                    </h4>
                    <div className="active d-flex justify-content-center">
                    <ul id="chat-log">
                        <p className="bg-secondary">Hello!</p>
                    </ul>
                    </div>
                    <div className="input-group mb-3">
                    <input
                        id="chat-message-input"
                        type="text number"
                        name="text"
                        className="form-control"
                        placeholder="Type a message..."
                    />
                    <input id="chat-message-submit" type="button" value="Send" />
                    </div>
                </div>
            </div>
            </div>
          </div>
        </div>
        {/* <div>
          <strong>Votes: {votes_count_to_skip}</strong>
        </div> */}
        {/* {isHost ? this.renderSettingsButton() : null} */}
        <button
          className="btn btn-danger btn-sm"
          onClick={this.handlBackButtonPress}
        >
          Leave Room
        </button>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            POST LINK
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <TextField
            error={this.state.error}
            label="Code"
            placeholder="Enter youtube url with 11 digits"
            helperText={this.state.error}
            variant="outlined"
            onChange={(e) => this.setState({ postinput: e.target.value })}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="primary"
            onClick={this.handlepostsong}
          >
            Post
          </Button>
        </Grid>
      </div>
    );
  }

  componentWillUnmount() {
    console.log("componentWillUnmount called");
    this.state.chatSocket.onclose = async(e) => {
      console.error("Chat socket closed unexpectedly");
    };
    console.log("componentWillUnmount called done");
  }
}

export default Room;

  // handleShowSettingsUpdate = (value) => {
  //   this.setState({
  //     showSettings: value,
  //   });
  // };

  // renderSettings() {
  //   return (
  //     <div className="container">
  //       <div className="container-fluid">
  //         <CreateRoom
  //           update={true}
  //           votes_count_to_skip={this.state.votes_count_to_skip}
  //           guest_can_pause={this.state.guest_can_pause}
  //           roomCode={this.state.roomCode}
  //           updateCallback={this.handleRoomData}
  //         />
  //       </div>
  //       <button
  //         className="btn btn-primary btn-sm"
  //         onClick={() => this.handleShowSettingsUpdate(false)}
  //       >
  //         Close
  //       </button>
  //     </div>
  //   );
  // }

  // renderSettingsButton = () => {
  //   return (
  //     <div className="container">
  //       <button
  //         className="btn btn-primary btn-sm"
  //         onClick={() => this.handleShowSettingsUpdate(true)}
  //       >
  //         Settings
  //       </button>
  //     </div>
  //   );
  // };
