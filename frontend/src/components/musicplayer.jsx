import React, { Component, createRef } from "react";

import { toast } from "react-toastify";
import AudioPlayer from "react-h5-audio-player";
// import "react-h5-audio-player/lib/styles.css";
// import "react-h5-audio-player/lib/styles.less";
import "./musicplayer.css";
import { Preloader, Audio } from "react-preloader-icon";

export default class MusicPlayer extends Component {
  constructor(props) {
    super(props);
    this.player = createRef();
  }

  state = {
    player: this.player,
  };

  async componentDidMount() {
    this.setState({ player: this.player });
  }

  componentDidUpdate(prevProps) {
    if (prevProps.play !== this.props.play && this.props.play !== null) {
      this.Audiofunction(this.player);
    }
    if (
      prevProps.song_info !== this.props.song_info &&
      this.props.song_info !== undefined &&
      this.props.song_info !== null
    ) {
      // console.log(`Now Playing ${this.props.song_info.song_name}`);
    }
  }

  async Audiofunction(player) {
    try {
      if (
        player !== null &&
        player !== undefined &&
        this.props.play !== null &&
        this.props.play !== undefined
      ) {
        if (this.props.play) {
          try {
            await player.current.audio.current.play();
          } catch (err) {
            await this.state.player.current.audio.current.play();
          }
        } else {
          try {
            await player.current.audio.current.pause();
          } catch (err) {
            console.log("err");
            this.state.player.current.audio.current.pause();
          }
        }
      }
    } catch (err) {
      console.log("err in Audiofunction");
    }
  }

  // handleGotoDuration = () => {
  //   this.state.player.current.audio.currentTime = 
  // }

  // handleSongDuration = (e) => {
  //   console.log("song dur called");
  //   if (e.type) {
  //     console.log(
  //       "DFGHJH",
  //       this.state.player.current.audio.current.oncanplaythrough
  //     );
  //     this.state.player.current.audio.current.currentTime =
  //       e.srcElement.currentTime;
  //     console.log(
  //       "success update",
  //       this.state.player.current.audio.current.ontimeupdate
  //     );
  //   }
  // }

  render() {
    if (this.props.song_info !== undefined && this.props.song_info !== null) {
      const {
        song_name,
        artist,
        image_url,
        view_count,
        song_url,
      } = this.props.song_info;
      // console.log("1. play in musicplayer", this.props.play);
      // console.log("2. new url in musicplayer", song_name);
      return (
        <div className="container">
          <div className="card bg-transparent text-white">
            <button className="btn btn-outline-warning pullup">
              <b>Note:- While Posting Link Pause the current song</b>
            </button>
            <button className="btn btn-outline-primary btn-lg space">
              <b>
                Room: {this.props.roomCode} ||{" "}
                {this.props.isHost ? <b>HOST</b> : "USER"}
              </b>
              {"      "}
            </button>
            <div className="card-img">
              <img
                src={this.props.song_info.image_url}
                className="card-img img-fluid"
                alt="..."
              />
            </div>
            <button className=" card-text btn btn-outline-primary btn-lg">
              <b>
                Now Playing {this.props.song_info.song_name} By{" "}
                {this.props.song_info.artist}
              </b>
            </button>
            <div className="row">
              <AudioPlayer
                autoplay={false}
                layout="stacked-reverse"
                loop={false}
                autoPlayAfterSrcChange={false}
                hasDefaultKeyBindings={true}
                showSkipControls={true}
                showJumpControls={false}
                // muted={muted_}
                src={this.props.song_info.song_url}
                onPlay={this.props.playpauseUpdate}
                onPause={this.props.playpauseUpdate}
                onClickNext={this.props.handlepostsong}
                onClickPrevious={(e) => {
                  console.log("prev e", e.type);
                }}
                onEnded={this.props.handlepostsong}
                onDragStart={(e) => {
                  console.log("onDragStart=> ", e.type);
                }}
                onDragMove={(e) => {
                  console.log("onDragMove => ", e.type);
                }}
                onDragEnd={(e) => {
                  console.log("onDragEnd => ", e.type);
                }}
                onSeeking={(e) => {
                  console.log("onSeeking => ", e);
                }}
                onSeeked={(e) => {
                  console.log("onSeeked => ", e.srcElement.currentTime);
                }}
                onVolumeChange={(e) => {
                  console.log("onVolumeChange => ", e.type);
                }}
                onCanPlay={(e) => {
                  console.log("onCanPlay => ", e.type);
                }}
                ref={this.player}
              />
            </div>
          </div>
          <div className="row justify-content-md-center"></div>
        </div>
      );
    } else {
      // const margin = window.innerHeight / 2 + "px";
      // console.log(typeof margin);
      return (
        <div style={{ margin: "50%", color: "white " }}>
          <Preloader
            use={Audio}
            size={100}
            strokeWidth={10}
            strokeColor="#262626"
            duration={2000}
          />
        </div>
      );
    }
  }
}
