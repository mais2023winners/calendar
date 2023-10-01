import Theme from "./Theme";
import { ChakraProvider, theme } from "@chakra-ui/react";
import Chat from "./pages/Chat";
import { useGoogleLogin } from '@react-oauth/google';
import { useEffect, useState } from "react";
import Login from "./pages/Login";
import axios from "axios";
import {
  FiLink
} from 'react-icons/fi'

export default function App() {

  const [loggedIn, setLoggedIn] = useState(false);

  const userSession = window.localStorage.getItem('userSession');

  const login = useGoogleLogin({
    onSuccess: tokenResponse => console.log(tokenResponse),
  });

  useEffect(() => {
    // get query string from url
    const queryString = window.location.search;
    // create an object with new URLSearchParams
    const urlParams = new URLSearchParams(queryString);
    // get the value of the parameter
    const userToken = urlParams.get('code');

    if (userToken) {
      axios.post('http://127.0.0.1:8000/google-redirect', {
        code: userToken
      }).then(response => {
        console.log('Success:', response);
        window.localStorage.setItem('userSession', JSON.stringify(response.data));
        window.location.href = '/';
      })
    }
    else if (userSession) {
      setLoggedIn(true);
    }
    else {
      setLoggedIn(false);
    }
  }, []);

  return <ChakraProvider theme={theme}>
    {loggedIn ? <Theme>
      <Chat />

    </Theme> : <Login />}

  </ChakraProvider>
  {/* <Button onClick={() => login()}>
        Sign in with Google 🚀{' '}
      </Button>; */}

}