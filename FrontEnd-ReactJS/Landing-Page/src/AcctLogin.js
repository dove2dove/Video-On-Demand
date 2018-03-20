import React from 'react';
import cbilogo from './static/img/icons/cbi-prime-logo.png';
import './AcctLogin.css';

class AcctLogin extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginSubmit = this.handleLoginSubmit.bind(this);
    this.state = {
      userEmail: '',
      userPasswd: '',
    };
  };
  handleEmailChange(event) {
    this.setState({userEmail: event.target.value})
  }
  handlePasswdChange(event) {
    this.setState({userPasswd: event.target.value})
  }
  handleLoginSubmit(event){
    event.preventDefault();
    //console.log('LoginData:', this.state)
    // fetch('/api/form-submit-url', {
    //   method: 'POST',
    //   body: data,
    // });
  }
  render() {
    return (
      <div id='login-content'>
      <div className="login-header">
      <div className="logo-header">
      <img border="0" alt="..." src={cbilogo} width="100"
      height="50"/>
      </div>
      </div>
      <div className="login-message">
      <p>Log in</p>
      </div>
      <div className="login-background">
      <div className="login-dialog">
      <div className="fb-login">
      <div className="fb-login-toppad">
      </div>
      <button className="login-button">CONTINUE WITH FACEBOOK</button>
      <div className="facebook-message">We&#x27;ll never post without your permission</div>
      </div>
      <div className="or">
      <div className="panel__divider_one"></div>
      <p> OR </p>
      <div className="panel__divider_two"></div>
      </div>
      <div className="Cbi-login">
      <form onSubmit={this.handleLoginSubmit}>
      <div className="form-label email-label">
      <p>EMAIL</p>
      </div>
      <input type="text" value={this.state.userEmail} name="email" onChange={this.handleEmailChange.bind(this)}/>
      <div className="form-label" >
      <p>PASSWORD</p>
      </div>
      <input type="password" value={this.state.userPasswd} name="password" onChange={this.handlePasswdChange.bind(this)}/>
      <div className="login-button-divider">
      <button className="login-button">LOG IN</button>
      </div>
      </form>
      </div>
      <div className="iforget-message">
      <div className="pad-passwd-forget"></div>
      <a href="https://www.cbi.com/users/find_account" target="_blank" rel="noopener noreferrer">Forgot your password/email?</a>
      </div>
      <div className="start-trial-message">Don&#x27;t have CBI Prime with Live TV?<a href="https://www.cbi.com/live-tv" target="_blank" rel="noopener noreferrer">Start your free trial now!</a>
      </div>
      </div>
      </div>
      </div>
    );
  }
}

AcctLogin.propTypes = {};
AcctLogin.defaultProps = {};

export default AcctLogin;
