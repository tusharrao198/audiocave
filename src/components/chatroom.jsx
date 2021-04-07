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

    handleNewUserMessage = (newMessage) => {
        this.setState((prevState) => {
            return { messages: [...prevState.messages, newMessage] };
        });
        this.props.handleNewUserMessage(newMessage);
        console.log("messages = ", this.state.messages);
        if (this.props.newmessage !== null) {
            this.setState((prevState) => {
                return { messages: [...this.state.messages, this.props.newmessage] };
            });
            console.log("INDDDDDD");
        }
    };

    addUserMessage = () => {
        console.log("ADD USER MESSAGE", this.props.newmessage);
        this.setState((prevState) => {
            return { messages: [...prevState.messages, this.props.newmessage] };
        });
        console.log("messages in addUserMessage = ", this.state.messages);
    }

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
            </div>
        );
    } 
}
export default ChatRoom;
