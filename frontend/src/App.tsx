import Theme from "./Theme";
import { ChakraProvider, theme } from "@chakra-ui/react";
import Chat from "./pages/Chat";

export default function App() {
  return <Theme>
    <ChakraProvider theme={theme}>
      <Chat/> 
    </ChakraProvider>
  </Theme>
}