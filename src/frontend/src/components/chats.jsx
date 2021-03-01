import React, { Component } from "react";
// import http from '../services/httpservice';
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
        // enter, return
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

//
// {% extends "base.html" %}
//
// {% block content %}
//   {% load staticfiles %}
//   <h1>{{ room.label }}</h1>
//   <p class="quiet">
//     Anyone with this URL can join the room and chat:
//     <code>{{ request.scheme }}://{{ request.get_host }}/{{ room.label }}</code>
//   </p>
//   <p>
//     <label for="handle">Your name:</label>
//     <input id="handle" type="text" placeholder="handle">
//   </p>
//   <form id="chatform">
//     <table id="chat">
//       <tbody>
//         {% for message in messages %}
//           <tr>
//             <td>{{ message.formatted_timestamp }}</td>
//             <td>{{ message.handle }}</td>
//             <td>{{ message.message }}</td>
//           </tr>
//         {% endfor %}
//       </tbody>
//       <tfoot>
//       <tr>
//         <td>Say something:</td>
//         <td colspan=2>
//           <input id="message" type="text" placeholder="message">
//           <button type="submit" id="go">Say it</button>
//         </td>
//       </tfoot>
//     </table>
//   </form>
// {% endblock content %}
//
// {% block afterbody %}
//   <script type="text/javascript" src='{% static "jquery-1.12.1.min.js" %}'></script>
//   <script type="text/javascript" src='{% static "reconnecting-websocket.min.js" %}'></script>
//   <script type="text/javascript" src='{% static "chat.js" %}'></script>
// {% endblock afterbody %}
