import { useState } from 'react';
import Component from 'react';
import axios from "axios";
import './App.css';
import {Routes, Route} from 'react-router-dom'

import 'intl-tel-input/build/css/intlTelInput.css';

import LogIn from './components/auth/LogIn'
import SignUp from './components/auth/SignUp'
import PhoneVerification from './components/auth/PhoneVerification'
import Feed from './components/feed/Feed'


function App(){

   // new line start
  /*const [profileData, setProfileData] = useState(null)
  const [userNumber, setUserNumber] = useState("000-000-0000")

  function updateNumber(evt){
    setUserNumber(evt)
    console.log(userNumber)
  }

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

    const inputProps = {
      placeholder: 'ReactIntlTelInput',
    };
   
    const intlTelOpts = {
      preferredCountries: ['cn'],
    };
   
    const value = { iso2: 'cn', dialCode: '86', phone: '12345678901' };
   
    const onChange = value => console.log(value);
    const onReady = (instance, IntlTelInput) => console.log(instance, IntlTelInput);*/

  return (
    <>
    <Routes>
      <Route path="/" element={<LogIn />}> </Route>
      <Route path="sign-up" element={<SignUp />}> </Route>
      <Route path="phone-verify" element={<PhoneVerification />}> </Route>
      <Route path="feed" element={<Feed />}> </Route>


    </Routes>
    </>

  )
}

export default App