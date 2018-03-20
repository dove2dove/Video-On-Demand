import React from 'react';

class VideoPlayer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {
    var imgsfile;
    if (this.props.videoSRC.split('\|')[0].startsWith('CLOUD')) {
      imgsfile = this.props.videoSRC.split('\|')[1];
    } else {
      imgsfile = require(`../../public/assets/movie/${this.props.videoSRC.split('\|')[1]}`)
    }
    return (
        <div className="MoviePlayer">
          <video width="740" height="460" controls autoPlay preload="none">
            <source src={imgsfile} type="video/mp4"/>
            <source src={imgsfile} type="video/webm"/>
            <source src={imgsfile} type="video/ogg"/>
          </video>
        </div>
    );
  }
}

VideoPlayer.propTypes = {};
VideoPlayer.defaultProps = {
  videoSRC: ''
};

export default VideoPlayer;
