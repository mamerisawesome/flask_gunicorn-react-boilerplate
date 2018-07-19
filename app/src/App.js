import React, { Component } from 'react';
import { Link, Route } from 'react-router-dom'
import './App.css';

import Item from './entities/Item'
import User from './entities/User'

class App extends Component {
    render() {
        return (
            <div>
                <nav>
                    <Link to="/item">Item</Link>
                    <Link to="/user">User</Link>
                </nav>
                <div>
                    <Route path="/item" component={Item}/>
                    <Route path="/user" component={User}/>
                </div>
            </div>
        );
    }
}

export default App;
