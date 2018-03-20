import React from 'react';

class SubMenu extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    getRenderSubBody() {
        return (this.props.subtext.map(function (item, id) {
           return (<li key={id}>
                <a href="#handleClick">
                {item.menuText}
                </a>
            </li>);
        }));
    }

    getRenderBody() {
        var submenuList = this.getRenderSubBody();
        var renderbody;
        if (this.props.submenutype.Type.length > 0 && this.props.submenutype.ButtText.length > 0) {
            renderbody = (<div>
                <ul className={this.props.submenutype.Type}>{submenuList}
                </ul>
                <button className="dropbtn">{this.props.submenutype.ButtText}</button>
            </div>)
        } else {
            renderbody = (<div>
                <ul>{submenuList}</ul>
            </div>)
        }
        return renderbody;
    }

    render() {
        var submenbody = this.getRenderBody();
        return (
            <div className="sub-menu">
                {submenbody}
            </div>
        );
    }
}

SubMenu.propTypes = {};
SubMenu.defaultProps = {
    subtext: [],
    submenutype: ''
};

export default SubMenu;