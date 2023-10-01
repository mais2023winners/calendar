import React from "react";
import { Flex, Avatar, AvatarBadge, Text } from "@chakra-ui/react";
import bot from "../assets/bot.png"
const Header = () => {
	return (
		<Flex w="100%">
			<Avatar size="lg" name="Dan Abrahmov" src={bot}>
				<AvatarBadge boxSize="1em" bg="green.500" />
			</Avatar>
			<Flex flexDirection="column" mx="5" justify="center">
				<Text fontSize="lg" fontWeight="bold">
					TimeWiz Assistant
				</Text>
				<Text color="green.500">Online</Text>
			</Flex>
		</Flex>
	);
};

export default Header;