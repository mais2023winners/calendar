import { Flex } from "@chakra-ui/react";
import React, { useState } from "react";
import Divider from "../components/Divider";
import Footer from "../components/Footer";
import Header from "../components/Header";
import Messages from "../components/Message";
import "../index.css"
import axios from "axios";

const Chat = () => {
	const [messages, setMessages] = useState([{
		from: "computer",
		text: "Hello, I'm Timewiz, your calendar and email personal assistant. How can I help you?",
	}]);
	const [inputMessage, setInputMessage] = useState("");
	const [loading, setLoading] = useState(false);

	const handleSendMessage = () => {
		if (!inputMessage.trim().length) {
			return;
		}
		const data = inputMessage;

		setMessages((old) => [...old, { from: "me", text: data }]);
		setInputMessage("");
		// e.preventDefault();
		setLoading(true);
		axios.post('http://localhost:8000/Ask_GPT', {
			userMessage: inputMessage,
			userToken: JSON.parse(String(window.localStorage?.getItem('userSession'))),
			history: messages.slice(0, messages.length - 1).map((message) => ({
				role: message.from === "computer" ? "assistant" : "user",
				content: message.text,
			}))

		})
			.then(response => {
				console.log('Success:', response.data.chatMessage.message);
				setMessages((old) => [...old, {
					from: "computer",
					text: response.data.chatMessage.message,
					...response.data

				}])

			})
			.catch(error => {
				console.error('Error:', error);
			})
			.finally(() => {
				setLoading(false);
			});
	};
	const chatStyle = {
		height: 'calc(100vh - 112px)'
	};
	return (
		<div style={chatStyle}>
			<Flex w="100%" h="100%" justify="center" align="flex-start" style={{
				backgroundColor: "white",
				padding: "10px",
				borderRadius: "40px",
				border: "1px solid",
				borderColor: "rgba(0,0,0,0.1)",
				// boxShadow: "0 0 10px rgba(0,0,0,0.1)"
			}} >
				<Flex w="100%" h="100%" flexDir="column" alignItems="center">
					<Header />
					<Messages messages={messages} />
					<Divider />
					<Footer
						loading={loading}
						inputMessage={inputMessage}
						setInputMessage={setInputMessage}
						handleSendMessage={handleSendMessage}
					/>
				</Flex>
			</Flex>
		</div >
	);
};

export default Chat;