import React, { Component } from 'react';
import axios from 'axios';
import './style.css';
import { MOTHER_APP_URL } from './../../.env.json'

class Item extends Component {
    state = { items: [] }

    componentDidMount() {
        const config = {
            method: 'get',
            url: `http://${MOTHER_APP_URL}/item`
        }

        axios(config)
            .then(res => {
                const items = res.data;
                this.setState({items});
            })
            .catch(err => console.error(err))
    }

    render() {
        return (
            <div>
                <h1>This is the items page</h1>
                {this.state.items}
            </div>
        );
    }
}

export default Item;
