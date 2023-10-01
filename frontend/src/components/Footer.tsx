import React from "react";
import { Flex, Input, Button } from "@chakra-ui/react";

const Footer = ({ inputMessage, setInputMessage, handleSendMessage, loading }) => {
	return (
		<Flex w="100%" mt="5">
			<Input

				placeholder="Type Something..."
				border="none"
				borderRadius="15"
				_focus={{
					border: "1px solid black",
				}}
				style={{
					borderColor: "black",
					borderWidth: "1px",
					border: "1px solid gray",
					boxShadow: "none",
					// @ts-ignore
					boxShadow: "0 0 10px rgba(0,0,0,0.1)"
				}}
				onKeyPress={(e) => {
					if (e.key === "Enter") {
						handleSendMessage();
					}
				}}
				value={inputMessage}
				onChange={(e) => setInputMessage(e.target.value)}
				marginRight="30px"

			/>
			{!loading ? <Button
				bg="black"
				color="white"
				borderRadius="15"
				_hover={{
					bg: "white",
					color: "black",
					border: "1px solid black",
				}}
				disabled={inputMessage.trim().length <= 0}
				onClick={handleSendMessage}
			>
				Send
			</Button> : <Button
				borderRadius="15"
				_hover={{
					bg: "gray",
					color: "gray",
					border: "1px solid black",
				}}
				disabled={true}
				onClick={handleSendMessage}
			>
				Loading...
			</Button>}
		</Flex>
	);
};

export default Footer;