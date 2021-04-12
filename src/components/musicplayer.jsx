import React, {
  Component,
  createRef,
} from "react";

import { toast } from "react-toastify";
import AudioPlayer from "react-h5-audio-player";
// import "react-h5-audio-player/lib/styles.css";
// import "react-h5-audio-player/lib/styles.less";
import "./musicplayer.css";

export default class MusicPlayer extends Component {
  constructor(props) {
    super(props);
    this.player = createRef();
  }
  componentDidUpdate(prevProps) {
    if (prevProps.play !== this.props.play && this.props.play !== null) {
      this.Audiofunction(this.props.play);
    }
    if (
      prevProps.song_info !== this.props.song_info &&
      this.props.song_info !== undefined &&
      this.props.song_info !== null
    ) {
      // console.log(`Now Playing ${this.props.song_info.song_name}`);
    }
  }

  Audiofunction(play) {
    var player = this.player.current;
    if (play !== null || play !== undefined) {
      if (play) {
        player.audio.current.play();
      } else {
        player.audio.current.pause();
      }
    }
  }

  render() {
    if (this.props.song_info !== undefined && this.props.song_info !== null) {
      const {
        song_name,
        artist,
        image_url,
        view_count,
        song_url,
      } = this.props.song_info;
      // console.log("play in musicplayer", this.props.play);
      // console.log("new url in musicplayer", song_name);
      return (
        <div className="container">
          <div className="card bg-dark text-white">
            <div className="card-img">
              <img
                src={this.props.song_info.image_url}
                className="card-img"
                alt="..."
              />
            </div>
            <button className=" card-text btn btn-outline btn-primary btn-lg">
              Now Playing {this.props.song_info.song_name} By{" "}
              {this.props.song_info.artist}
            </button>
            <div className="row">
              <AudioPlayer
                autoplay={false}
                loop={false}
                autoPlayAfterSrcChange={false}
                hasDefaultKeyBindings={true}
                // muted={muted_}
                src={this.props.song_info.song_url}
                onPlay={this.props.playpauseUpdate}
                onPause={this.props.playpauseUpdate}
                ref={this.player}
              />
            </div>
          </div>
          <div className="row justify-content-md-center"></div>
        </div>
      );
    } else {
      return (
        <h1>
          <button
            className="btn btn-outline btn-primary"
            onClick={() => {
              console.log(this.props.song_info);
              window.location.reload();
            }}
          >
            Loading
          </button>
        </h1>
      );
    }
  }
}