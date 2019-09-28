import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {Test} from './Test'

class App extends Component {
  
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
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {JSON.stringify(this.state.name)}
        </p>
        <Test/>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
        </a>
        </header>
      </div>
    );
  }
}

export default App;
