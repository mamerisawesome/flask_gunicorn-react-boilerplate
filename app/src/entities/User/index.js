import React, { Component } from 'react';
import axios from 'axios';
import './style.css';
import { MOTHER_APP_URL } from './../../.env.json'

class User extends Component {
    state = { users: [] }

    componentDidMount() {
        const config = {
            method: 'get',
            url: `http://${MOTHER_APP_URL}/user`,
        }

        axios(config)
            .then(res => {
                const users = res.data;
                this.setState({users})
            })
            .catch(err => console.error(err))
    }

    render() {
        return (
            <div>
                <h1>This is the users page</h1>
                {this.state.users}
            </div>
        );
    }
}

export default User;
