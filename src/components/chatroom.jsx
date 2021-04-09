import React, { Component } from "react";
import { Widget, addResponseMessage, addUserMessage } from "react-chat-widget";
import "react-chat-widget/lib/styles.css";
// import logo from './logo.svg';

class ChatRoom extends Component {
  state = {
    messages: [],
  };

  componentDidMount() {
    // addResponseMessage("Welcome to Audiocave!");
  }

  handleNewUserMessage = async (newMessage) => {
    // this.setState({ messages: [...this.state.messages, newMessage]});
    console.log(newMessage);
    // addUserMessage("sa")
    this.props.handleNewUserMessage(newMessage);
    console.log("messages = ", this.state.messages);
  };

  render() {
    if (this.props.newmessage) {
      addResponseMessage(this.props.newmessage);
    }
    return (
      <div className="App">
        <Widget
          handleNewUserMessage={this.handleNewUserMessage}
          autofocus={true}
          title="Audiocave Chat"
          subtitle="Chat with your friends!"
        />
      </div>
    );
  }
}
export default ChatRoom;
