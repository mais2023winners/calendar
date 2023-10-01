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
		axios.post('http://localhost:8000/Ask_GPT', {
			userMessage: inputMessage,
			userToken: {
				"access_token": "ya29.a0AfB_byC_Agn23bFWIy9UAYu1JUoDP5oEGrVrQ8GUE9U5yo0LhNBjmBLNAVfWgH0Yu3SI6Rhp2cJ0ja0HTDqFFJjnx331O8BQJGrpoqwjqzSPlqozCdOQ6ohrx8VUQB6vv01ai3Y7ktlBsNE5evdBC7C_G3k3AJS6I0f9aCgYKAS4SARMSFQGOcNnCAr1Up2OOgYX2shorFqnmkw0171",
				"expires_in": 3599,
				"refresh_token": "1//0dujYTmsTO4o1CgYIARAAGA0SNwF-L9IrCq-nvJ5ykQCqzvp3aqfo_fC40rsCEYJ6V7xN5Lm5-JgLbaPZoF_Nt51Qbn9l0cb-aoM",
				"scope": "https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/calendar openid https://mail.google.com/ https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
				"token_type": "Bearer",
				"id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImI5YWM2MDFkMTMxZmQ0ZmZkNTU2ZmYwMzJhYWIxODg4ODBjZGUzYjkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NDk2MzY0NjEyMi1pajFwaXBtb2wzMGNmc3B2cjBxMXY5cmI0MHF1ZGUydi5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6Ijc0OTYzNjQ2MTIyLWlqMXBpcG1vbDMwY2ZzcHZyMHExdjlyYjQwcXVkZTJ2LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAxMTU0NzAxMzkwMzAzMzcwODgzIiwiZW1haWwiOiJtYWlzaGFja3NhY2NAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJ6RzJnN1o1Q3ZoV0NBdGYxbnl2Zm53IiwibmFtZSI6Ik1BSVMgSEFDS1MiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTFhRbS1lQ2swZ0ZxUnJwOHhTRm9GMkd4UU1QV3IyRTlrY2FaZDNacVJKPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik1BSVMiLCJmYW1pbHlfbmFtZSI6IkhBQ0tTIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2OTYwMjgzMjQsImV4cCI6MTY5NjAzMTkyNH0.NMa6CRQ9ncrONvtdzjJSUY1Z9um4Y8e8vI-fN_R1fcxfeasy6zWjj9J2ZWVWhqsM23k5dD6HVHAm7aiDwss9u3SXusuY8bAqcbScCJ_UUbSxO39YEMNJN35c4Rg2i0-FRMb2Gb1SIHouoGWlfzNJY6c93Bxx3-KGgOPqgKJs-Oyu6BWmzT2d5eTgOqTAB74dMW3GqvwIn2WcVgzZ3QmnlcoWR7sgK7oM9MkOyR-a9IQu5FDJF7qeRsn01LOjV5UuvtUpp2xysFUBQtExqfe3MGOO9AZtax_p3D5Fn6iCjhk50d1eZ7NKSEkyDAJTcSEGPMf3usBLlL3KOu40SHFPTQ"
			}
		})
			.then(response => {
				console.log('Success:', response.data.chatMessage.message);
				setMessages((old) => [...old, { from: "computer", text: response.data.chatMessage.message }])

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