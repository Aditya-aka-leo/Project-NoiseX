import React from 'react';
// import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
// import '../node_modules/bootstrap/dist/js/bootstrap.bundle';
import { Switch, Route, Redirect } from 'react-router-dom';
import './App.css';

import FlexCards from './components/landingpage/Cards/FlexCards';

function App() {
  return (
    <div className="App">
      <FlexCards />
    </div>
  );
}

export default App;
