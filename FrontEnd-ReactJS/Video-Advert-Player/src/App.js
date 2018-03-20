import React, {Component} from 'react';
import './assets/css/aviva.css';
import MainMenu from './components/MainMenu.react';
import Footer from './components/Footer.react';
import MoviesHeader from "./components/MoviesHeader.react";
import VideoPlayer from "./components/VideoPlayer.react";

class App extends Component {
  constructor(props) {
    super(props);
    this.handleWatchListEvent = this.handleWatchListEvent.bind(this);
    this.handlePlayMovieEvent = this.handlePlayMovieEvent.bind(this);
    this.handleMovieClickEvent = this.handleMovieClickEvent.bind(this);
    this.handleTVClickEvent = this.handleTVClickEvent.bind(this);
    this.handleKidsClickEvent = this.handleKidsClickEvent.bind(this);
    this.handleOriginalClickEvent = this.handleOriginalClickEvent.bind(this);
    this.handleAddonClickEvent = this.handleAddonClickEvent.bind(this);

    this.state = {
      fullHeader: true,
      loadTvPage: false,
      loadMoviePage: false,
      loadKidsPage: false,
      loadOriginalPage: false,
      loadAddonPage: false,
      loadTrialPage: false,
      loadAcctPage: false,
      playMovie: false,
      loadWatchList: false,
      slideParam: {},
      videosource: ''
    }
  }

  resetAllStates() {
    this.setState({loadTvPage: false});
    this.setState({loadMoviePage: false});
    this.setState({loadKidsPage: false});
    this.setState({loadOriginalPage: false});
    this.setState({loadAddonPage: false});
    this.setState({loadTrialPage: false});
    this.setState({loadAcctPage: false});
    this.setState({playMovie: false});
    this.setState({loadWatchList: false});
  }

  handlePlayMovieEvent (srcName) {
    this.resetAllStates();
    this.setState({fullHeader: false});
    this.setState({playMovie: true});
    this.setState({videosource: srcName});
  };
  handleWatchListEvent (e) {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadWatchList: true});
  };
  handleTVClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadTvPage: true});
  };
  handleMovieClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadMoviePage: true});
    this.setState({slideParam: {Category: 'MOVIES', Limiter: '8', MovieType: 'FM', ByRandom: 'true'}});
  }
  handleKidsClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadKidsPage: true});
  };

  handleOriginalClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadOriginalPage: true});
  };
  handleAddonClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: true});
    this.setState({loadAddonPage: true});
  };
  handleTrialClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: false});
  };
  handleAcctClickEvent = (e) => {
    e.preventDefault();
    this.resetAllStates();
    this.setState({fullHeader: false});
  };
  renderMovieHeader(){
    return (
      <MoviesHeader handlePlayMovie={this.handlePlayMovieEvent} handleWatchList={this.handleWatchListEvent} SlideParameter={this.state.slideParam}/>
    );
  }

  loadBodyContent() {
    if (this.state.fullHeader) {
      return (this.renderMovieHeader());
    } else if (this.state.playMovie) {
      return (<VideoPlayer videoSRC={this.state.videosource}/>);
    }
  }

loadInitialContent(){
  var bodytype='';
  if (this.state.playMovie) {
    bodytype = 'playerbody';
  }else{
    bodytype = 'my-body';
  }
  return ( <div id={bodytype}>
    {this.loadBodyContent()}
    <Footer />
    </div>);
  }
  render() {
    var appBody = this.loadInitialContent();
    return (
      <div className="App">
      <MainMenu isFullHeader={this.state.fullHeader} handleTVClick={this.handleTVClickEvent}
      handleMovieClick={this.handleMovieClickEvent} handleKidsClick={this.handleKidsClickEvent} handleOriginalClick={this.handleOriginalClickEvent} handleAddonClick={this.handleAddonClickEvent}/>
      {appBody}
      </div>
    );
  }
}

export default App;
