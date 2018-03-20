import React, { Component } from 'react';
import {Router, Route} from 'react-router';
import './App.css';
import './mastbody.css';
import AcctLogin from "./AcctLogin";
import checkimg from './static/img/icons/images-check1.jpeg';
import mobileimg from './static/img/appimg/iphone6sp-silver-select.png';
import advertgrid from './static/img/appimg/movies-advert-grid.png';
import lifestyle from './static/img/appimg/family-lifestyle.jpeg';

//npm install react react-dom react-router --save
//npm install react-router --save
var containerTag = '';
class App extends Component {
  constructor(props) {
    super(props);
    this.handlePlanOneClick = this.handlePlanOneClickEvent.bind(this);
    this.handlePlanTwoClick = this.handlePlanTwoClickEvent.bind(this);
    this.handleLoginClick = this.handleLoginClickEvent.bind(this);
    this.state = {
      isPlanOneDroped: false,
      isPlanTwoDroped: false,
      isLogin: false,
      isWelcome: true,
    }
  }
  resetAllStates() {
    this.setState({isLogin: false});
    this.setState({isWelcome: false});
  }
  handleLoginClickEvent (e) {
    e.preventDefault();
    this.resetAllStates()
    this.setState({isLogin: true});
  }
  handlePlanOneClickEvent (e) {
    e.preventDefault();
    this.setState({isPlanOneDroped: !this.state.isPlanOneDroped});
  }
  handlePlanTwoClickEvent (e) {
    e.preventDefault();
    this.setState({isPlanTwoDroped: !this.state.isPlanTwoDroped});
  }
  getWelcomePage() {
    var planexpsectOne = 'plan-card__expanded-section';
    var pcexpbuttOne = 'plan-card__expand-button';
    var pcmexpbuttOne = 'plan-card__mobile-expand-button';
    var pcmWrapperOne = 'plan-card__mobile-wrapper';
    var planexpsectTwo = 'plan-card__expanded-section';
    var pcexpbuttTwo = 'plan-card__expand-button';
    var pcmexpbuttTwo = 'plan-card__mobile-expand-button';
    var pcmWrapperTwo = 'plan-card__mobile-wrapper';
    var addonTextOne = 'See Add-ons'; // Close Add-ons
    var devAddonTextOne = 'See details'; //Close details
    var addonTextTwo = 'See Add-ons'; // Close Add-ons
    var devAddonTextTwo = 'See details'; //Close details

    if (this.state.isPlanOneDroped){
      planexpsectOne = 'plan-card__expanded-section--open';
      pcexpbuttOne = 'plan-card__expand-button--open';
      pcmexpbuttOne = 'plan-card__mobile-expand-button--open';
      pcmWrapperOne = 'plan-card__mobile-wrapper--open';
      addonTextOne = 'Close Add-ons';
      devAddonTextOne = 'Close details';
    }else{
      planexpsectOne = 'plan-card__expanded-section';
      pcexpbuttOne = 'plan-card__expand-button';
      pcmexpbuttOne = 'plan-card__mobile-expand-button';
      pcmWrapperOne = 'plan-card__mobile-wrapper';
      addonTextOne = 'See Add-ons';
      devAddonTextOne = 'See details';
    }
    if (this.state.isPlanTwoDroped){
      planexpsectTwo = 'plan-card__expanded-section--open';
      pcexpbuttTwo = 'plan-card__expand-button--open';
      pcmexpbuttTwo = 'plan-card__mobile-expand-button--open';
      pcmWrapperTwo = 'plan-card__mobile-wrapper--open';
      addonTextTwo = 'Close Add-ons';
      devAddonTextTwo = 'Close details';
    }else{
      planexpsectTwo = 'plan-card__expanded-section';
      pcexpbuttTwo = 'plan-card__expand-button';
      pcmexpbuttTwo = 'plan-card__mobile-expand-button';
      pcmWrapperTwo = 'plan-card__mobile-wrapper';
      addonTextTwo = 'See Add-ons';
      devAddonTextTwo = 'See details';
    }
    return (
      <div>
      <div className="content-wrapper">
      <header id="navigation" className="jsx-2100920611 baywood-header baywood-header--sticky baywood-header--remove-gradient">
      <div className="content container-width">
      <span className="baywood-header__logo">
      <span>cbi</span>
      </span>
      <div className="baywood-header__left-links">
      <a className="baywood-header__link "></a>
      </div>
      <div className="baywood-header__cta cta-always">
      <button className="primary-button button--cta">START YOUR FREE TRIAL</button>
      </div>
      <div className="baywood-header__links">
      <a href="/login" className="link--login baywood-header__link" onClick={this.handleLoginClick}>Log In</a>
      </div>
      <button className="baywood-header__hamburger"></button>
      </div>
      <div className="toaster undefined ">
      <button className="primary-button button--cta">START YOUR FREE TRIAL</button>
      </div>
      </header>
      <div className="jsx-318983943 masthead">
      <picture className="hidden">
      <source media="(min-width: 769px)" srcSet={lifestyle}/>
      <source media="(min-width: 376px)" srcSet={lifestyle}/>
      <source media="(min-width: 0px)" srcSet={lifestyle}/>
      <img alt="preloading masthead" className="hidden"/>
      </picture>
      <div id="start_page_masthead" className="start-masthead align-top tall-masthead bg-right-bottom-lg">
      <div className="start-masthead--background"></div>
      <div className="content container-width">
      <div className="start-masthead--preheadline start-masthead--block">&nbsp;</div>
      <h1 className="start-masthead--headline start-masthead--block start-masthead--headline-container">All Your TV In One Place</h1>
      <div className="start-masthead--primary-message start-masthead--block">Watch thousands of shows and movies, with plans starting at $7.99/month.</div>
      <div className="start-masthead--secondary-message start-masthead--block">HBO®, SHOWTIME®, and CINEMAX® available as add-ons.</div>
      <div className="start-masthead--input-container start-masthead--block align-top tall-masthead bg-right-bottom-lg">
      <button className="primary-link button--cta start-masthead--cta primary-button">START YOUR FREE TRIAL</button>
      </div>
      <div className="start-masthead--legal start-masthead--block start-masthead--legal-container"> Offer available to new subscribers only</div>
      </div>
      </div>
      <div className="start-masthead--scroll container-fluid has-copy">
      <div className="start-masthead--anchor-copy">PLAN OPTIONS</div>
      <a className="start-masthead--circle">
      <div className="start-masthead--circle-arrow"></div>
      </a>
      </div>
      </div>
      <div>
      <div className="grid-picture-box">
      <picture>
      <source media="(min-width: 769px)" srcSet={advertgrid}/>
      <source media="(min-width: 376px)" srcSet={advertgrid}/>
      <source media="(min-width: 0px)" srcSet={advertgrid}/>
      <a href="https://infallible-allen-a29e71.netlify.com" className="MovieStreamer">
      <img className="resp-img" alt="All your TV in one place" src={advertgrid}/>
      </a>
      </picture>
      </div>
      </div>
      <div id="plans" className="jsx-4247217990 plan-container container-width">
      <div className="plan-container__header section-headline">
      <h2>Select Your Plan</h2>
      <h5>No contracts, commitments, or equipment rentals.</h5>
      </div>
      <div className="plan-container__row">
      <div className="jsx-3791717551 plan-card">
      <div className="plan-card__border">
      </div>
      <div className="plan-card__wrapper">
      <div className="plan-card__header">
      <h2 className="section-headline">cbi Prime</h2>
      <p>Get 1 month free, then starts at</p>
      <div className="plan-card__priceline">
      <h4>$7.99/</h4>
      <p>month</p>
      </div>
      <div className="plan-card__button-wrapper">
      <button className="button--cta plan-card__cta secondary-button">Select Plan</button>
      </div>
      <div className="plan-card__sublink"></div>
      </div>
      <div className={pcmWrapperOne}>
      <div className="plan-card__list section-body">
      <ul>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Stream on your favorite devices</li>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Get unlimited access to the CBI streaming library with limited or no commercials. Enjoy full seasons of exclusive series, hit movies, CBI Originals, kids shows, and more</li>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Switch plans or cancel anytime</li>
      </ul>
      </div>
      <div className={planexpsectOne}>
      <div className="plan-card__expanded-heading">
      </div>
      <div className="plan-card__addons">
      <ul>
      <li>No Commercials</li>
      <li>HBO®</li>
      <li>SHOWTIME®</li>
      <li>CINEMAX®</li>
      </ul>
      </div>
      </div>
      </div>
      <div className="plan-card__expander">
      <a role="button" className={pcexpbuttOne} onClick={this.handlePlanOneClick}>{addonTextOne} <span className="plan-card__icon-plus"></span></a>
      </div>
      </div>
      </div>
      <div className="jsx-3791717551 plan-card">
      <div className="plan-card__border"></div>
      <div className="plan-card__wrapper">
      <div className="plan-card__header">
      <h2 className="section-headline">CBI Prime with Live TV<span className="plan-card__beta">BETA</span></h2>
      <p>Get 7 days free, then starts at</p>
      <div className="plan-card__priceline">
      <h4>$39.99/</h4>
      <p>month</p>
      </div>
      <div className="plan-card__button-wrapper">
      <button className="button--cta plan-card__cta secondary-button">Select Plan</button>
      </div>
      <div className="plan-card__sublink">
      <p><a href="/live-tv" data-events="utag,user_interaction" data-element-specifier="plan_card_live" data-action-specifier="learn_more" data-utag-object="event_name:learn_more,product_name:live">Learn More</a></p>
      </div>
      </div>
      <div className={pcmWrapperTwo}>
      <div className="plan-card__list section-body">
      <ul>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Watch Live TV online and on iOS, Android, Roku, Fire TV, Apple TV (4th gen), Chromecast, and Xbox</li>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Get unlimited access to the CBI streaming library (Limited Commercials plan) with full seasons of exclusive series, hit movies, CBI Originals, kids shows, and more</li>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Stream 50+ top Live and On Demand TV channels including sports, news, and entertainment</li>
      <li><img className="plan-card__list-check" src={checkimg} alt="checks" width="18" height="18"/>Switch plans or cancel anytime</li>
      </ul>
      </div>
      <div className={planexpsectTwo}>
      <div className="plan-card__expanded-heading">
      </div>
      <div className="plan-card__addons">
      <ul>
      <li>Enhanced Cloud DVR</li>
      <li>Unlimited Screens</li>
      <li>HBO®</li>
      <li>SHOWTIME®</li>
      <li>CINEMAX®</li>
      </ul>
      </div>
      </div>
      </div>
      <div className="plan-card__expander">
      <a role="button" className={pcexpbuttTwo} onClick={this.handlePlanTwoClick}>{addonTextTwo} <span className="plan-card__icon-plus"></span></a>
      </div>
      </div>
      </div>
      </div>
      </div>
      <div id="call-to-action" className="jsx-4049683046 container">
      <div className="container-width call-to-action call-to-action--with-image hide-body-md">
      <div className="col-lg-6 cta--column--texts">
      <h3 className="cta--headline section-headline">Watch Thousands of Shows and Movies Anytime, Anywhere</h3>
      <p className="cta--body">
      <span className="mobilebox-span-info"></span>
      </p>
      <div className="cta--column--actions">
      <button className="button--cta primary-button">START YOUR FREE TRIAL</button>
      </div>
      </div>
      <div className="col-lg-6 cta--image">
      <picture>
      <source media="(min-width: 1025px)" srcSet={mobileimg}/>
      <source media="(min-width: 769px)" srcSet={mobileimg}/>
      <source media="(min-width: 0px)" srcSet={mobileimg}/>
      <img src={mobileimg} alt="Watch Thousands of shows and movies anytime, anywhere"/>
      </picture>
      </div>
      </div>
      </div>
      </div>
      <footer className="jsx-1373584494">
      <div className="container-width">
      <div className="baywood-footer">
      <div className="footer--row footer--site-links">
      <a href="/press/about" className="footer--site-link">about</a>
      <a href="/jobs" className="footer--site-link">jobs</a>
      <a href="/help?src=footer" className="footer--site-link">help</a>
      <span className="footer--logo"><span>© 2018 Cbi Prime</span></span>
      </div>
      <div className="footer--row footer--legal-links">
      <span className="footer--logo footer--logo-mobile"><span>© 2018 Cbi Prime</span></span>
      <a href="//info.evidon.com/pub_info/3920?v=1&amp;nt=0&amp;nw=false" target="_blank" rel="nofollow noopener noreferrer" className="footer--legal-link">About Ads</a>
      <a href="/terms" className="footer--legal-link">Terms of Use</a>
      <a href="/privacy" className="footer--legal-link">Privacy Policy</a>
      </div>
      </div>
      </div>
      </footer>
      </div>
    );
  }
  getAppsBody(){
    var varappBody = '';
    if (this.state.isWelcome){
      containerTag = "page";
      varappBody = this.getWelcomePage();
    }
    if (this.state.isLogin){
      containerTag = "login-page";
      varappBody = <AcctLogin />
    }
    return varappBody;
  }
  render() {
    var appBody = this.getAppsBody();
    return (
      <div className={containerTag}>
      {appBody}
      </div>
    );
  }
}

export default App;
