import React, { useEffect, useRef } from "react";
import { Avatar, Flex, Text, Link, Icon } from "@chakra-ui/react";
import { FiLink } from "react-icons/fi";

const Messages = ({ messages }) => {
	const AlwaysScrollToBottom = () => {
		const elementRef = useRef();
		// @ts-ignore
		useEffect(() => elementRef.current.scrollIntoView());
		return <div ref={elementRef} />;
	};

	return (
		<Flex w="100%" h="80%" overflowY="scroll" flexDirection="column" p="3">
			{messages.map((item, index) => {
				if (item.from === "me") {
					return (
						<Flex key={index} w="100%" justify="flex-end">
							<Flex
								bg="#147efb"
								color="white"
								minW="30px"
								maxW="350px"
								my="1"
								p="3"
								borderRadius="20"
							>
								<Text>{item.text}</Text>
							</Flex>
						</Flex>
					);
				} else {
					return (
						<Flex key={index} w="100%" align="center">
							<Avatar
								name="Computer"
								src="https://png.pngtree.com/png-vector/20230407/ourmid/pngtree-chatbot-line-icon-vector-png-image_6680403.png"
								bg="white"
								color="black"
								style={{
									border: "1px solid black",
									boxShadow: "0 0 10px rgba(0,0,0,0.1)"
								}}
							></Avatar>
							<Flex
								bg="black"
								color="white"
								minW="30px"
								maxW="350px"
								my="1"
								p="3"
								borderRadius="20"
								marginLeft="3"
								direction={"column"}
							>
								<p style={{
									whiteSpace: "pre-line"
								}}>{item.text}</p>
								{item?.eventLink ? <Link
									style={{
										whiteSpace: "pre-line",
										color: "blue"
									}}
									href={item.eventLink} target="_blank" rel="noreferrer">
									<Icon
										// mr="4"
										fontSize="16"
										_groupHover={{
											color: 'white',
										}}
										as={FiLink}
									/> <b>Link to Calendar</b>
								</Link> : null}

							</Flex>

						</Flex>
					);
				}
			})}
			<AlwaysScrollToBottom />
		</Flex>
	);
};

export default Messages;