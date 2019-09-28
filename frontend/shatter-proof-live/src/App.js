import React, {Component} from 'react';
import { Router, Link } from "@reach/router";
import {Home} from './components/routes'

class App extends Component {
  
  render() {
    return (
    <Router>
      <Home path="/" />
    </Router>
    );
  }
}

export default App;
