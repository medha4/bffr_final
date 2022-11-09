import { useState } from 'react';
import Component from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';

function App() {

   // new line start
  const [profileData, setProfileData] = useState(null)

  function getData() {
    axios({
      method: "GET",
      url:"/",
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}
    //end of new line 

  return (
    <div class="App">

        <span class="dot"></span>
        <span class="dot2"></span>
        <span class="dot3"></span>
        <span class="dot4"></span>

        <div class = "accentBalls">
          <span class="dot5"></span>
          <span class="dot6"></span>
        </div>


      <div class="logoHolder">
          <h1 class = "title"> BFFR </h1>
          <h2 class = "subtitle"> Friends' Music Now </h2>
      </div>

      <div class="mainContainer" >

        <div class="loginContainer"> 
          <form>
            <h1 class = "numberTxt"> Phone Number </h1>
            <input class = "phoneInput" type="tel" name="name" />

            <input class = "submitButton" type="submit" value="Submit" />
          </form>
        </div>

      </div>

    </div>

   /* <div>
      <center>
      <h1>BFFR</h1><br></br>
      <ul>
        <li><a href="https://bffr.atlassian.net/wiki/spaces/BFFR/pages/1671170/BFFR+Documentation">User Guide</a></li>
        <li><a href="/profile.html">Profile</a></li>
        <li><a href="/feed.html">Feed</a></li>
      </ul>
      <p>Hello World!</p>
      <input placeholder="Email"></input><br></br>
      <input placeholder="Password"></input><br></br>
      <button>Sign Up!</button>
      <br></br>
      <p>Already have an account? Log in</p>
      </center>
    </div>
*/
  );
}

export default App;