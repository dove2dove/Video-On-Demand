import React from "react";
import watchlist from '../assets/img/icons/watchlist.png';
import webplay from '../assets/img/icons/webplay_button.png';

   var videoPath= [];
   var slideContent = [];

class MoviesHeader extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }
    componentDidMount() {
        const url = 'http://127.0.0.1:8091/service/movies/categorytype.json/?Category='+this.props.SlideParameter.Category+'&Limiter='+this.props.SlideParameter.Limiter+'&MovieType='+this.props.SlideParameter.MovieType+'&ByRandom='+this.props.SlideParameter.ByRandom;
        fetch(url, {
            mode: 'no-cors',
            method: 'GET', // or 'PUT' 'POST'
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(res => res.json())
            .then(response => this.setState({slideContent: response}))
            .then(response => console.log('Success:', response))
            .catch(error => console.error('Error:', error))

        //
        const url2 = 'http://127.0.0.1:8091/data/general.json';
        fetch(url2, {
            mode: 'no-cors',
            method: 'GET', // or 'PUT' 'POST'
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
        }).then(res => res.json())
            .then(response => this.setState({videoPath: response}))
            .then(response => console.log('Success:', response))
            .catch(error => console.error('Error:', error))
    }
    renderSlide() {
        var videosource = '';
        var watchListEvent = this.props.handleWatchList;
        var moviePlayerEvent = this.props.handlePlayMovie;
        if ((slideContent.length > 0) && (videosource.length === 0)) {
             videoPath.map(function (item, i) {
                if (i === 0) {
                    videosource = item.MoviePathType;
                }else{
                    videosource = '';
                }
            });
        }
        var myslide = slideContent.map(function (item, i) {
            var isactive = (i === 0) ? 'item active' : 'item';
            var moviefile = (videosource.toUpperCase().startsWith("CLOUD")) ? 'CLOUD|'+item.MoviePathCloud : 'LOCAL|'+item.MoviePathLocal;
            var imgfile = require(`../assets/img/movies/${item.BigPicture}`)
            return (<div key={i} className={isactive}>
                <img className="slide-img" src={imgfile}
                     alt="Chania" width="460"
                     height="345"/>
                <div className="carousel-caption">
                    <div className="caption-message">
                        <p>Watch the Movie</p>
                        <h3>{item.Name}</h3>
                        <p>{item.ShortDetails}</p>
                    </div>
                    <div className="caption-watch">
                        <a href="#wlist" className="watchlist"
                           onClick={watchListEvent}>
                            <img className="watchicon" border="0" alt="#"
                                 src={watchlist}
                                 width="20"
                                 height="20"/>Watchlist
                        </a>
                    </div>
                    <div className="caption-play">
                        <a href="#play" onClick={() => moviePlayerEvent(moviefile)}>
                            <img border="0" alt="#"
                                 src={webplay}
                                 width="100"
                                 height="100"/>
                        </a>
                    </div>
                </div>
            </div>);
        })
        return (
            slideContent && myslide
        );
    }

    getSlideIndicators() {
        var myindic = slideContent.map(function (item, i) {
            return (i === 0) ? <li key={i} data-target="#myCarousel" data-slide-to={i} className="active"></li> :
                <li key={i} data-target="#myCarousel" data-slide-to={i}></li>
        })
        return myindic
    }

    render() {
        var appslide = this.renderSlide();
        var indslide = this.getSlideIndicators();
        return (
            <div id="myCarousel" className="my-carousal carousel slide" data-ride="carousel">
                <ol className="carousel-indicators">
                    {indslide}
                </ol>

                <div>
                    <div className="carousel-inner" role="listbox">
                        {appslide}
                    </div>
                    <a className="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                        <span className="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        <span className="sr-only">Previous</span>
                    </a>
                    <a className="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                        <span className="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        <span className="sr-only">Next</span>
                    </a>
                </div>
            </div>
        );
    }
};

MoviesHeader.propTypes = {
};
MoviesHeader.defaultProps = {
  SlideParameter : {},
};

export default MoviesHeader;
