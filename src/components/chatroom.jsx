import React, { Component } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import axios from "axios";
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

    chatSocket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      this.handleshowdata(data);
    };

    chatSocket.onclose = (e) => {
      console.error("Chat socket closed unexpectedly");
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
        })
      );
      messageInputDom.value = "";
    };
  };

  handleshowdata = (e) => {
    let node = document.createElement("p");
    let textnode = document.createTextNode(e.message);
    node.appendChild(textnode);
    document.getElementById("chat-log").appendChild(node);
  };

  render() {
    return (
      <div className="container">
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
    );
  }
}

export default ChatRoom;
