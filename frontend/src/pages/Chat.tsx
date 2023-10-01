import { Flex } from "@chakra-ui/react";
import React, { useState } from "react";
import Divider from "../components/Divider";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Messages from "../components/Message";
import "../index.css"
import axios from "axios";

const Chat = () => {
  const [messages, setMessages] = useState([
	{ from: "computer", text: "Hi, My Name is HoneyChat" },
	{ from: "me", text: "Hey there" },
	{ from: "me", text: "Myself Ferin Patel" },
	{
  	from: "computer",
  	text: "Nice to meet you. You can send me message and i'll reply you with same message.",
	},
  ]);
  const [inputMessage, setInputMessage] = useState("");

  const handleSendMessage = () => {
	if (!inputMessage.trim().length) {
  	return;
	}
	const data = inputMessage;

	setMessages((old) => [...old, { from: "me", text: data }]);
	setInputMessage("");
	// e.preventDefault();
	axios.post('http://localhost:8000/Ask_GPT', inputMessage)
		.then(response => {
		console.log('Success:', response.data.chatMessage.message);
		setMessages((old) => [...old,{from:"computer", text: response.data.chatMessage.message}])

		})
		.catch(error => {
		console.error('Error:', error);
		});
  };
  const chatStyle = {
	height: 'calc(100vh - 112px)'
  };
  return (
	<div style={chatStyle}>
	<Flex w="100%" h="100%" justify="center" align="flex-start" >
  	<Flex w="100%" h="100%" flexDir="column" alignItems="center">
    	<Header />
    	<Divider />
    	<Messages messages={messages} />
    	<Divider />
    	<Footer
      	inputMessage={inputMessage}
      	setInputMessage={setInputMessage}
      	handleSendMessage={handleSendMessage}
    	/>
  	</Flex>
	</Flex>
	</div>
  );
};

export default Chat;