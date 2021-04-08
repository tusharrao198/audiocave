import React, { Component } from 'react';
import { Widget, addResponseMessage, addUserMessage } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';
// import logo from './logo.svg';

class ChatRoom extends Component {
    state = {
        messages: [],
    }

    componentDidMount() {
        // addResponseMessage("Welcome to Audiocave!");

    }

    handleNewUserMessage = async(newMessage) => {
        // this.setState({ messages: [...this.state.messages, newMessage]});
        this.props.handleNewUserMessage(newMessage);
        console.log("messages = ", this.state.messages);
    };

    // addUserMessage = async() => {
    //     console.log("ADD USER MESSAGE", this.props.this.props.newmessageRecieved);
    //     addUserMessage(this.props.newmessageRecieved);
    //     // this.setState({ messages: [...this.state.messages, this.props.newmessageRecieved]});
    //     console.log("messages in addUserMessage = ", this.state.messages);
    // }

    render() {
        return (
            <div className="App">
                <Widget
                handleNewUserMessage={this.handleNewUserMessage}
                // addUserMessage={this.addUserMessage}
                autofocus={false}
                // title="My new awesome title"
                // subtitle="And my cool subtitle"
                />
                {/* {
                    this.props.newmessageRecieved? this.addUserMessage(this.props.newmessageRecieved) : <h1></h1>
                } */}
            </div>
        );
    } 
}
export default ChatRoom;
