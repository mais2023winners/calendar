'use client'

import {
    Box,
    Flex,
    Stack,
    Heading,
    Text,
    Container,
    Input,
    Button,
    SimpleGrid,
    Avatar,
    AvatarGroup,
    useBreakpointValue,
    IconProps,
    Link,
    Icon,
} from '@chakra-ui/react'


const Blur = (props: IconProps) => {
    return (
        <Icon
            width={useBreakpointValue({ base: '100%', md: '40vw', lg: '30vw' })}
            zIndex={useBreakpointValue({ base: -1, md: -1, lg: 0 })}
            height="560px"
            viewBox="0 0 528 560"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            {...props}>
            <circle cx="71" cy="61" r="111" fill="#F56565" />
            <circle cx="244" cy="106" r="139" fill="#ED64A6" />
            <circle cy="291" r="139" fill="#ED64A6" />
            <circle cx="80.5" cy="189.5" r="101.5" fill="#ED8936" />
            <circle cx="196.5" cy="317.5" r="101.5" fill="#ECC94B" />
            <circle cx="70.5" cy="458.5" r="101.5" fill="#48BB78" />
            <circle cx="426.5" cy="-0.5" r="101.5" fill="#4299E1" />
        </Icon>
    )
}

export default function Login() {
    return (
        <Box position={'relative'}>
            <Container
                as={SimpleGrid}
                maxW={'7xl'}
                columns={{ base: 1, md: 2 }}
                spacing={{ base: 10, lg: 32 }}
                py={{ base: 10, sm: 20, lg: 32 }}>
                <Stack spacing={{ base: 10, md: 20 }}>
                    <Heading
                        lineHeight={1.1}
                        fontSize={{ base: '3xl', sm: '4xl', md: '5xl', lg: '6xl' }}>
                        TimeWiz
                        <Heading>
                            A virtual wizard by your side that manages your calendar and emails!
                        </Heading>
                    </Heading>
                    <img src='./banner.svg' />

                    <Stack direction={'row'} spacing={4} align={'center'}>
                    </Stack>
                </Stack>
                <Stack
                    bg={'gray.50'}
                    rounded={'xl'}
                    p={{ base: 4, sm: 6, md: 8 }}
                    spacing={{ base: 8 }}
                    maxW={{ lg: 'lg' }}>
                    <Stack spacing={4}>
                        <Text fontSize={{ base: 'sm', sm: 'md' }}>
                            Meet TimeWiz, your new best friend for managing your busy life. Are you tired of struggling with your calendar? TimeWiz is here to make it simple. With us, you can effortlessly schedule and keep track of your events. And guess what? You can even send emails without leaving the app! Join us on this journey to make your life easier. Sign up now and let TimeWiz help you manage your time like a pro!
                        </Text>
                    </Stack>
                    <Box as={'form'} mt={10}>
                        <Stack spacing={4}>
                            <Button onClick={() => {
                                window.location.href = `https://accounts.google.com/o/oauth2/v2/auth?scope=email profile https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/gmail.modify https://mail.google.com/
                                https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/contacts.readonly&access_type=offline&redirect_uri=http://localhost:5173/google-redirect&response_type=code&client_id=74963646122-ij1pipmol30cfspvr0q1v9rb40qude2v.apps.googleusercontent.com`
                            }} fontFamily={'heading'} bg={'gray.200'} color={'gray.800'} flexDirection={"row"}>
                                <img src="https://static-00.iconduck.com/assets.00/google-icon-2048x2048-czn3g8x8.png" width={"20px"} style={{ marginRight: "10px" }} /> Login with Google
                                {/* </Link> */}
                            </Button>
                        </Stack>
                    </Box>
                    form
                </Stack>
            </Container>
            <Blur position={'absolute'} top={-10} left={-10} style={{ filter: 'blur(70px)' }} />

        </Box>
    )
}