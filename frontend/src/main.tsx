import * as React from 'react'
import { ChakraProvider } from '@chakra-ui/react'
import * as ReactDOM from 'react-dom/client'
import App from './App'
import { GoogleOAuthProvider } from '@react-oauth/google';


const rootElement = document.getElementById('root')
ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <ChakraProvider>
      <GoogleOAuthProvider clientId="74963646122-ij1pipmol30cfspvr0q1v9rb40qude2v.apps.googleusercontent.com">
        <App />

      </GoogleOAuthProvider>;
    </ChakraProvider>
  </React.StrictMode>,
)