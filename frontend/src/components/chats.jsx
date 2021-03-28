import React, { Component } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
import "./chatroom.css";
import config from "../services/config.json";
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
import CreateRoom from "./createroom";
import MusicPlayer from "./musicplayer";
import { Redirect, Route, Switch, Link } from "react-router-dom";
import { render } from "react-dom";

class ChatRoom extends Component {
  state = {
    messages: [],
  };

  componentDidMount = () => {
    const { roomCode } = this.props;
    const chatSocket = new WebSocket(
      "ws://" + window.location.host + "/ws/chat/" + roomCode + "/"
    );

    chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      document.querySelector("#chat-log").value += data.message + "\n";
      this.setState({ messages: [...data.message] });
    };

    chatSocket.onclose = function (e) {
      console.error("Chat socket closed unexpectedly");
    };

    document.querySelector("#chat-message-input").focus();
    document.querySelector("#chat-message-input").onkeyup = function (e) {
      if (e.keyCode === 13) {
        document.querySelector("#chat-message-submit").click();
      }
    };

    document.querySelector("#chat-message-submit").onclick = function (e) {
      const messageInputDom = document.querySelector("#chat-message-input");
      const message = messageInputDom.value;
      chatSocket.send(
        JSON.stringify({
          message: message,
        })
      );
      messageInputDom.value = "";
    };
  };

  render() {
    return (
      <div>
        <div>
          <label for="handle">Your name:</label>
          <input id="handle" type="text" placeholder="handle"></p>
        </div>
        <div>
          <textarea id="chat-log" cols="4" rows="2"></textarea>
          <br />
          <input id="chat-message-input" type="text" size="20" />
          <br />
          <input id="chat-message-submit" type="button" value="Send" />
        </div>
      </div>
    );
  }
}

export default ChatRoom;
