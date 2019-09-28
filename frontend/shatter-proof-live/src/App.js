import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import {Test} from './Test'

class App extends Component {
  
  state = {
    name: ''
  }
  async componentDidMount() {
    try {
      const response = await fetch('/examplePost', {
        method: 'POST',
        headers: {
          'Content- Type': 'application / json'
        },
        body: JSON.stringify({
          test: 'trg'
        })
      });
      const json = response.json();
      console.log(json);
      console.log("this is true");
      this.setState({ name: json })
    } catch(error) {
      console.log(error);
    }
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.name}
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
