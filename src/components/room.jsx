import React, { Component } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import config from "../services/config.json";
import { toast } from "react-toastify";
import "../index.css";
import MusicPlayer from "./musicplayer";
import swal from "sweetalert";
import { Widget, addResponseMessage } from "react-chat-widget";
import "react-chat-widget/lib/styles.css";

class Room extends Component {
  state = {
    guest_can_pause: false,
    isHost: false,
    roomCode: this.props.match.params.roomCode,
    is_playing: false,
    song_name: null,
    song_info: null,
    songYTUrl: null,
    updatedSongPlayingURL: null,
    linkpostInput: null,
    newmessage: null,
    chatSocket: null,
    playPausemessage: null,
    leaveRoomStatus: false,
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
      this.setState({ chatSocket: _ });
    });

    chatSocket.onclose = async (e) => {
      console.error("Chat socket closed unexpectedly");
    };

    chatSocket.onmessage = async (e) => {
      const data = JSON.parse(e.data);
      this.handleshowdata(data, Object.keys(data));
    };

    if (roomCode !== null && roomCode !== undefined) {
      this.handleRoomData();
      // console.log("componentDidMount called");
    }
  }

  handleshowdata = async (e, obj) => {
    const { sender } = this.state;
    if (e !== null && e !== undefined) {
      let i;
      for (i in obj) {
        if ("playPausemessage" === obj[i]) {
          this.setState({ playPausemessage: e.playPausemessage });
        }
        if ("updateSong" === obj[i]) {
          this.setState({ updateSong: e.updateSong });
        }
        if ("leaveRoomStatus" === obj[i]) {
          this.setState({ leaveRoomStatus: e.leaveRoomStatus });
        }
        if ("updatedSongPlayingURL" === obj[i]) {
          console.log("url", e.updatedSongPlayingURL);
          this.setState({
            updatedSongPlayingURL: e.updatedSongPlayingURL,
          });
        }
        if ("song_info" === obj[i]) {
          console.log("info", e.song_info);
          this.setState({ song_info: e.song_info });
        }
      }
      if (e.message !== null && e.message !== undefined && sender === false) {
        addResponseMessage(e.message);
      }
    }
    if (sender) {
      this.setState({ sender: false });
    }
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

    if (prevState.leaveRoomStatus !== this.state.leaveRoomStatus) {
      console.log("IF leaveroom updated", this.state.leaveRoomStatus);
      this.handleLeaveRoom();
    }

    if (prevState.newmessage !== this.state.newmessage) {
      console.log("newmessage update");
    }
  }

  handleRoomData = async () => {
    try {
      if (this.state.roomCode !== null && this.state.roomCode !== undefined) {
        await axios
          .get(config.apiEndpointgetRoom + `${this.state.roomCode}`)
          .then((res) => {
            if (res.status === 200) {
              this.setState({
                guest_can_pause: res.data.guest_can_pause,
                isHost: res.data.ishost,
                roomCode: res.data.RoomCodeinSession,
                is_playing: res.data.is_playing,
                songYTUrl: res.data.songurl,
              });
            }
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
    console.log("handlBackButtonPress called");
    if (this.state.isHost) {
      // if host left the room then delete room
      this.send_leaveRoom_status(true);
    }
    await axios.post(config.apiEndpointLeaveRoom).then((data) => {
      if (data.status === 200 || data.status === 201) {
        this.props.leaveRoomCallback(null);
        this.props.history.replace("/");
      } else {
        console.log("error in handlBackButtonPress");
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
          swal("Room Deleted By Host \n Go Back to Homepage");
          this.props.history.replace("/");
        } else {
          swal("Room Deleted By Host \n Go Back to Homepage");
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
      if (this.state.song_name !== data.song_name) {
        // console.log("Current Song_info Added", data.song_name);
        this.setState({ song_name: data.song_name });
        this.setState({ song_info: data });
        this.setState({ bgimage: data.image_url });
        this.setState({ updatedSongPlayingURL: data.song_url });
      }
    } catch (ex) {
      if (
        ex.response &&
        ex.response.status >= 400 &&
        ex.response.status <= 500
      ) {
        // error
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
          this.handlegetCurrentSong().then(() => {
            this.send_songUpdate(
              true,
              this.state.updatedSongPlayingURL,
              this.state.song_info
            );
          });
        }
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

  send_songUpdate = (res, URL, song_info) => {
    console.log("SENDING SONG UPDATE ", res);
    const { chatSocket } = this.state;
    chatSocket.send(
      JSON.stringify({
        updateSong: res,
        updatedSongPlayingURL: URL,
        song_info: song_info,
      })
    );
  };

  send_leaveRoom_status = (e) => {
    const { chatSocket } = this.state;
    console.log("LEAVE CALLED");
    chatSocket.send(
      JSON.stringify({
        leaveRoomStatus: e,
      })
    );
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
      updatedSongPlayingURL,
      song_info,
      playPausemessage,
      is_playing,
    } = this.state;

    return (
      // <!-- ======= Coordinators ======= -->
      <div className="main">
        <button
          className="btn btn-outline btn-danger toRight"
          onClick={this.handlBackButtonPress}
        >
          Leave Room
        </button>
        <div className="container justify-content-md-center">
          <button className="btn btn-outline btn-primary btn-lg space">
            Room: {roomCode} || {isHost ? "HOST" : "USER"}
          </button>
          {/* <strong>{is_playing ? "Playing" : "Paused"}</strong> */}

          <div className="row justify-content-md-center"></div>

          <div className="row justify-content-md-center">
            <div className="col-lg d-flex">
              <MusicPlayer
                roomCode={roomCode}
                play={playPausemessage}
                song_info={song_info}
                updatedSongPlayingURL={updatedSongPlayingURL}
                playpauseUpdate={this.handleplaypauseUpdateButton}
              />
            </div>
            <div className="col-lg-3 col-md-6 toMiddle">
              <div className="row text-center">
                <h5 className="text-center">Post New Link Here</h5>
                <Grid item xs={12} align="center">
                  <TextField
                    error={this.state.error}
                    label="Link"
                    placeholder="Enter youtube url with 11 digits"
                    helperText={this.state.error}
                    variant="outlined"
                    onChange={(e) =>
                      this.setState({ linkpostInput: e.target.value })
                    }
                  />
                </Grid>
              </div>
              <div className="row justify-content-md-center">
                <button
                  className="btn btn-outline btn-danger"
                  onClick={this.handlepostsong}
                >
                  Post
                </button>
              </div>
            </div>
          </div>
          {/* <div className="">
        </div> */}
          <Widget
            handleNewUserMessage={this.handleNewUserMessage}
            autofocus={true}
            title="Audiocave Chat"
            subtitle="Chat with your friends!"
          />
        </div>
      </div>
    );
  }

  componentWillUnmount() {
    // console.log("componentWillUnmount called");
    this.state.chatSocket.onclose = async (e) => {
      console.error("Chat socket closed unexpectedly");
    };
  }
}

export default Room;
