import React, { Component } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import config from "../services/config.json";
import { toast } from "react-toastify";
import "../index.css";
import MusicPlayer from "./musicplayer";
import swal from 'sweetalert';
import { Widget, addResponseMessage, addUserMessage } from "react-chat-widget";
import "react-chat-widget/lib/styles.css";


class Room extends Component {
  state = {
    guest_can_pause: false,
    isHost: false,
    roomCode: this.props.match.params.roomCode,
    song_info: {},
    song: null,
    songurl: null,
    updatedSongPlayingURL: null,
    linkpostInput: null,
    is_playing: false,
    bgimage: null,
    send_status: null,
    messages: null,
    newmessage: null,
    chatSocket: null,
    playPausemessage: null,
    leaveRoom: false,
    updateSong: false,
    sender: false,
  };

  async componentDidMount() {
    const { roomCode } = this.props.match.params;
    let chatSocket = null;
    async function createSocket() {
      chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + roomCode + "/"
      );
      return chatSocket;
    }

    createSocket().then((_) => {
      // console.log("created socket", _)
      this.setState({ chatSocket: _ });
    });

    chatSocket.onclose = async (e) => {
      console.error("Chat socket closed unexpectedly");
    };

    chatSocket.onmessage = async (e) => {
      const data= JSON.parse(e.data);
      this.handleshowdata(data, Object.keys(data));
    };

    if (roomCode !== null && roomCode !== undefined) {
      this.handleRoomData();
      // console.log("componentDidMount called");
    }
  }

  handleshowdata = async (e, obj) => {
    const { sender } = this.state;
    if (e.message !== null && e.message !== undefined && sender === false) {
      addResponseMessage(e.message);
    }
    let i;
    for (i in obj){
      if ("playPausemessage"===obj[i]) {
        // console.log("A");
        this.setState({ playPausemessage: e.playPausemessage });
      }
      if ("updateSong" === obj[i]) {
        this.setState({ updateSong: e.updateSong });
      }
      if ("leaveRoom" === obj[i]) {
        this.setState({ leaveRoom: e.leaveRoom });
      }
      if ("updatedSongPlayingURL" === obj[i]){
        this.setState({updatedSongPlayingURL: e.updatedSongPlayingURL});
      } 
    }
    if (sender) {
      this.setState({ sender: false });
    }
    // console.log("this rec", this.state.playPausemessage);
  };

  componentDidUpdate(prevProps, prevState) {
    if (prevState.roomCode !== this.state.roomCode) {
      if (this.state.roomCode === null) {
        swal(`ROOM DELETED BY HOST , LEAVE ROOM !`);
        window.location.reload();
      } else {
        window.location.reload();
      }
    }
    if (prevState.is_playing !== this.state.is_playing) {
      // console.log("isPlaying updated by interval ", this.state.is_playing);
    }
    if (prevState.updatedSongPlayingURL !== this.state.updatedSongPlayingURL) {
      // this.handlegetCurrentSong();
      console.log("updatedSongPlayingURL changed");
      this.send_songUpdate(true, this.state.updatedSongPlayingURL);
    }
    if (prevState.leaveRoomStatus !== this.state.leaveRoomStatus) {
      this.handleLeaveRoom();
    }
    // if (prevState.updateSong !== this.state.updateSong) {
    //   // console.log(
    //   //   "updatesong state changed from ",
    //   //   prevState.updateSong,
    //   //   "to => ",
    //   //   this.state.updateSong
    //   // );
    //   // this.handlegetCurrentSong();
    // }
    if (prevState.newmessage !== this.state.newmessage) {
      // console.log("newmessage update");
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
        // console.log("//Room Code is Null");
        this.props.history.replace("/");
      }
    } catch (ex) {
      // toast.error("REDIRECTED TO HOMEPAGE");
      this.props.leaveRoomCallback(null);
      this.props.history.replace("/");
    }
  };

  handlBackButtonPress = async () => {
    // console.log("handlBackButtonPress called");
    if (this.state.isHost) {
      // if host left the room then delete room
      this.send_leaveRoom_status(true);
    }
    await axios.post(config.apiEndpointLeaveRoom).then((data) => {
      if (data.status === 200 || data.status === 201) {
        this.props.leaveRoomCallback(null);
        this.props.history.replace("/");
      } else {
        // console.log("error in handlBackButtonPress");
      }
    });
  };

  handleLeaveRoom = async () => {
    try {
      await axios.post(config.apiEndpointLeaveRoom).then((res) => {
        if (res.status === 200 || res.status === 201 || res.status === 301) {
          this.props.leaveRoomCallback(null);
          if (this.state.isHost) {
            this.state.chatSocket.close();
          } // console.log("called handleLeaveRoom");
          toast.error("REDIRECTED TO HOMEPAGE");
          this.props.history.replace("/");
        } else {
          // toast.error("REDIRECTED TO HOMEPAGE");
          this.props.history.replace("/");
        }
      });
    } catch (ex) {
      this.props.leaveRoomCallback(null);
      // console.log("called handleLeaveRoom in catch er");
      this.props.history.replace("/");
    }
  };

  handlegetCurrentSong = async () => {
    try {
      const { data } = await axios.get(config.apigetYTLink);
      if (this.state.song !== data.song_name) {
        console.log("Current Song_info Added");
        this.setState({ song: data.song_name });
        this.setState({ songurl: data.song_url });
        this.setState({ song_info: data });
        this.setState({ bgimage: data.image_url});
        this.setState({ updatedSongPlayingURL: data.song_url});
      }
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
        // this.state.retrycount <= 2
      ) {
        // this.setState({ retrycount: this.state.retrycount++ });
        // 
      }
    }
  };

  handlepostsong = async () => {
    // console.log("posting song");
    const post = {
      ytlink: this.state.linkpostInput,
      roomCode: this.state.roomCode,
    };
    try {
      await axios.post(config.apipostYTLink, post).then((res, err) => {
        if (res.status === 200) {
          this.handlegetCurrentSong();
          // this.send_songUpdate(true);
        } // else {
        //   // console.log("error", err);
        // }
      });
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
    const { chatSocket } = this.state;
    chatSocket.send(
      JSON.stringify({
        playPausemessage: status,
      })
    );
  };

  handleplaypauseUpdateButton = async (event) => {
    let value = null;
    if (event.type === "play") {
      // console.log("PLAY SEND");
      value = true;
    } else if (event.type === "pause") {
      // console.log("pause send");
      value = false;
    }
    const post = {
      is_playing: value,
      musicurl: this.state.songurl,
      roomCode: this.state.roomCode,
    };
    try {
      const { data } = await axios.patch(config.apiYTUpdate, post);
    } catch (ex) {
      toast.error("Error Updating Room Details");
    }
    this.send_playPause_status(value);
  };

  send_songUpdate = (res, URL) => {
    console.log("SENDING SONG UPDATE ", res);
    const { chatSocket } = this.state;
    chatSocket.send(
      JSON.stringify({
        updateSong: res,
        updatedSongPlayingURL: URL,
      })
    );
  };

  send_leaveRoom_status = (e) => {
    const { chatSocket } = this.state;
    console.log("LEAVE CALLED");
    chatSocket.send(
      JSON.stringify({
        leaveRoom: e,
      })
    );
  };

  handleNewUserMessage = async (e) => {
    const { chatSocket } = this.state;
    this.setState({ sender: true });
    chatSocket.send(
      JSON.stringify({
        message: e,
      })
    );
  };

  render() {
    const {
      roomCode,
      isHost,
      updatedSongPlayingURL, playPausemessage, is_playing,
      bgimage,
    } = this.state;
    console.log("RESULT",playPausemessage);
    console.log("CHANGES SSDSDSDSD", updatedSongPlayingURL);
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
        <Widget
          handleNewUserMessage={this.handleNewUserMessage}
          autofocus={true}
          title="Audiocave Chat"
          subtitle="Chat with your friends!"
        />
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
                // song={this.state.song}
                // songurl={this.state.songurl}
                roomCode={this.state.roomCode}
                play={this.state.playPausemessage}
                // guest_can_pause={this.state.guest_can_pause}
                isHost={isHost}
                // send_status={this.state.send_status}
                // {...this.state.song_info}
                updatedSongPlayingURL={this.state.updatedSongPlayingURL}
                playpauseUpdate={this.handleplaypauseUpdateButton}
              />
            </div>
          </div>
        </div>
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
            onChange={(e) => this.setState({ linkpostInput: e.target.value })}
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
    this.state.chatSocket.onclose = async (e) => {
      console.error("Chat socket closed unexpectedly");
    };
    // console.log("componentWillUnmount called done");
  }
}

export default Room;