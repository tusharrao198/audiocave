import React, { Component, createRef, useEffect, useState, useRef } from "react";
import axios from "axios";
import config from "../services/config.json";
import { toast } from "react-toastify";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";

export default class MusicPlayer extends Component {
  constructor(props) {
    super(props);
    this.player = createRef();
  }

  componentDidUpdate(prevProps) {
    if(prevProps.song_url !== this.props.song_url){
      toast.success(`Now Playing ${this.props.song}`)
    }
  }

  Audiofunction(play) {
    var player = this.player.current;

    console.log("type from backend", play);
    if (play) {
      console.log("inside play ", play)
      player.audio.current.play();
    } else {
      console.log("inside pause ", play);
      player.audio.current.pause();
    }
    return <h1></h1>;
  }

  render() {
    if (this.player.current !== null) {
      var player = this.player.current;
      // console.log("type from backend", this.props.play);
      if (this.props.play) {
        player.audio.current.play();
      } else {
        player.audio.current.pause();
      }
    } 
    return (
      <div className="container">
        <div className="row text-center">Now Playing {this.props.song}</div>
        <div className="row">
          <AudioPlayer
            autoplay={false}
            loop={false}
            autoPlayAfterSrcChange={false}
            hasDefaultKeyBindings={true}
            // muted={muted_}
            src={this.props.song_url}
            onPlay={this.props.playpauseUpdate}
            onPause={this.props.playpauseUpdate}
            ref={this.player}
          />
        </div>
      </div>
    );
  }
}



// export default function MusicPlayer(props) {
//   const { play, song_status } = props;
//   var player = useRef();

//   function Audiofunction(play){
//     console.log("type from backend", play);
//     if (play) {
//       player.current.audio.current.play();
//     } else{
//       player.current.audio.current.pause();
//     }
//     return <h1></h1>
//   };

//   return (
//     <div className="App">
//       <AudioPlayer
//         autoplay={false}
//         loop={false}
//         autoPlayAfterSrcChange={false}
//         hasDefaultKeyBindings={true}
//         // muted={muted_}
//         src={props.song_url}
//         onPlay={props.playpauseUpdate}
//         onPause={props.playpauseUpdate}
//         ref={player}
//       />
//       {props.song_status ? Audiofunction(props.play) : <h1></h1>}
//     </div>
//   ); 
// }
