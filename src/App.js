import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from 'react';
import LandingPage from './LandingPage'
import InterestsPg from './InterestsPg'
import Signup from './Signup'
import Thankyou from './Thankyou'


function App() {
  return (
    <div className="App">
    <Router>
    <Routes>
      <Route path="/" element={<LandingPage/>}/>
      <Route path="/signup" element={<Signup/>}/>
      <Route path="/interests" element={<InterestsPg/>}/>
      <Route path="/thankyou" element={<Thankyou/>}/>
    </Routes>
  </Router>
    </div>
  );
}

export default App;
