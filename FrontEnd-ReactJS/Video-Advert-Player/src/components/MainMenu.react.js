import React from 'react';
import SubMenu from './SubMenu.react';
import logo from '../assets/img/icons/cbi-prime.png';

class MainMenu extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            tvSubText: [
                {menuText: 'Popular', clickAction: ''},
                {menuText: 'Recently Added', clickAction: ''},
                {menuText: 'Genres', clickAction: ''},
                {menuText: 'Staff Picks', clickAction: ''},
                {menuText: 'Networks', clickAction: ''}
            ],
            tvSubMenuType: {
                Type: '',
                ButtText: ''
            },
            movieSubText: [
                {menuText: 'Documentaries', clickAction: ''},
                {menuText: 'Genres', clickAction: ''},
                {menuText: 'Movie Night', clickAction: ''},
                {menuText: 'Staff Picks', clickAction: ''}
            ],
            movieSubMenuType: {
                Type: '',
                ButtText: ''
            },
            trialSubText: [
                {menuText: 'Get Unlimited Access to Movie Library', clickAction: ''},
                {menuText: 'Choose Limited or No Commercials', clickAction: ''},
                {menuText: 'Add SHOWTIME to Your Subscription', clickAction: ''},
                {menuText: 'Watch on TVs &amp; Mobile Devices', clickAction: ''}
            ],
            trialSubMenuType: {
                Type: 'trialList',
                ButtText: 'Get Started'
            },
            acctSubText: [
                {menuText: 'Watchlist', clickAction: ''},
                {menuText: 'Account', clickAction: ''},
                {menuText: 'History', clickAction: ''},
                {menuText: 'Help', clickAction: ''},
                {menuText: 'Log Out', clickAction: ''}
            ],
            acctSubMenuType: {
                Type: '',
                ButtText: ''
            },
        };
    };

//{require('../assets/img/icons/logo.png')}
    render() {
        var headerType = this.props.isFullHeader ? 'my-fullnav' : 'my-simplenav';
        return (
            <div className={headerType}>
                <div className="topboxmenu">
                    <ul id="topnav" className="my-menu">
                        <li className="toplist">
                            <a href="#log">
                                <img border="0" alt="#logo" src={logo}
                                     width="100" height="50"/>
                            </a>
                        </li>
                        <li className="toplist nav-dropdown"><a href="tv" onClick={this.props.handleTVClick}>TV</a>
                            <SubMenu subtext={this.state.tvSubText} submenutype={this.state.tvSubMenuType}/>
                        </li>
                        <li className="toplist nav-dropdown"><a href="movies" onClick={this.props.handleMovieClick}>MOVIES</a>
                            <SubMenu subtext={this.state.movieSubText} submenutype={this.state.movieSubMenuType}/>
                        </li>
                        <li className="toplist"><a href="kids" onClick={this.props.handleKidsClick}>KIDS</a></li>
                        <li className="toplist"><a href="originals" onClick={this.props.handleOriginalClick}>ORIGINALS</a></li>
                        <li className="toplist"><a href="addons" onClick={this.props.handleAddonClick}>ADD-ONS</a></li>
                        <form id="searchnav" method="get" action="http://www.google.com">
                            <input type="text" className="tftextinput" name="q" size="30" maxLength="120"/>
                            <input type="submit" value="search" className="tfbutton"/>
                        </form>
                    </ul>
                </div>
                <div className="buttboxmenu">
                    <ul id="bottnav" className="my-menu">
                        <li className="toplist nav-dropdown"><a href="#trials" onClick={() => {
                            this.props.handleTrialClick.bind(this)
                        }}>START YOUR FREE TRIAL</a>
                            <SubMenu subtext={this.state.trialSubText} submenutype={this.state.trialSubMenuType}/>
                        </li>
                        <li className="toplist nav-dropdown"><a href="#username" onClick={() => {
                            this.props.handleAcctClick.bind(this)
                        }}>DAVID WOODROW</a>
                            <SubMenu subtext={this.state.acctSubText} submenutype={this.state.acctSubMenuType}/>
                        </li>
                    </ul>
                </div>
            </div>
        );
    }
}

MainMenu.propTypes = {};
MainMenu.defaultProps = {
    isFullHeader: false
};

export default MainMenu;
