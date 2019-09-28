import React, { Component } from 'react';
import logo from '../../../logo.svg';
import '../../../App.css';
import { Navbar } from './Navbar';
import {UserTable} from './UserTable'

class Home extends Component {

    state = {
        name: ''
    }
    componentDidMount() {
        const request = JSON.stringify({
            test: 'trg'
        });
        fetch('http://127.0.0.1:5000/examplePost', {
            method: 'POST',
            body: request
        }).then(res => {
            console.log(res.json())
        })
    }
    render() {
        return (
            <div className="App">
                <Navbar/>
                <UserTable/>
            </div>
        );
    }
}

export {Home}
