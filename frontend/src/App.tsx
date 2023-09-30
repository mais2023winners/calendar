import Theme from "./Theme";
import { ChakraProvider, theme } from "@chakra-ui/react";
import Chat from "./pages/Chat";
import { useGoogleLogin } from '@react-oauth/google';
import {
  Button
} from "@chakra-ui/react";

export default function App() {

  const login = useGoogleLogin({
    onSuccess: tokenResponse => console.log(tokenResponse),
  });

  return <Theme>

    <ChakraProvider theme={theme}>
      <Chat />
    </ChakraProvider>
    {/* <Button onClick={() => login()}>
        Sign in with Google 🚀{' '}
      </Button>; */}
  </Theme>
}