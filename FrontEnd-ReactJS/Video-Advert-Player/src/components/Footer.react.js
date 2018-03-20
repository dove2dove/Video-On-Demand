import React from 'react';

class Footer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        return (
            <div className="my-footer">
                <div className="topboxfooter">
                    <ul id="topfooter" className="main-footer">
                        <li id="footera"><a href="#subscribenow">Subscribe Now</a></li>
                        <li id="footera"><a href="#livetv">Live TV</a></li>
                        <li id="footera"><a href="#advertising">Advertising</a></li>
                        <li id="footera"><a href="#jobs">Jobs</a></li>
                        <li id="footera"><a href="#press">Press</a></li>
                        <li id="footera"><a href="#help">Help</a></li>
                        <li id="footera"><a href="#aboutus">About Us</a></li>
                        <li id="footera"><a href="#siteMap">Site Map</a></li>
                        <li id="footera"><a href="#Blog">Blog</a></li>
                    </ul>
                </div>
                <div className="bottboxfooter">
                    <ul id="bottfooter" className="main-footer">
                        <li id="footerb"><a href="#aboutads">About Ads</a></li>
                        <li id="footerb"><a href="#termsofuse">Term of Use</a></li>
                        <li id="footerb"><a href="#privacypolicy">Privacy Policy</a></li>
                        <li id="footerb"><a href="#avivacopy">@2018 CBI</a></li>
                    </ul>
                </div>
            </div>
        );
    }
}

Footer.propTypes = {};
Footer.defaultProps = {};

export default Footer;
