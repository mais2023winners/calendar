import React, { useEffect, useRef } from "react";
import { Avatar, Flex, Text } from "@chakra-ui/react";

const Messages = ({ messages }) => {
  const AlwaysScrollToBottom = () => {
	const elementRef = useRef();
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
				borderRadius="15"
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
            	src="https://avataaars.io/?avatarStyle=Transparent&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light"
            	bg="blue.300"
          	></Avatar>
          	<Flex
            	bg="#d8d8d8"
            	color="black"
            	minW="30px"
            	maxW="350px"
            	my="1"
            	p="3"
				borderRadius="15"
				marginLeft="3"
          	>
            	<Text>{item.text}</Text>
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