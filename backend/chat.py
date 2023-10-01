import openai, json
from calendarEvent import createEvent, calendarFetch
from contacts import contactFetch
from gmail import create_message, send_message

def ConnectToGPT(userMessage: str, userToken: json):
    openai.api_key = "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"

    event = calendarFetch(userToken)
    contacts = str(contactFetch())
    prompt = """

    You are a calendar chat bot, and you do 3 things:
    - Help the user find availabilites for a meeting. You will be given a list of events, and you will need to return a list of available time slots for a meeting. The events are sorted by start time in ascending order. You may assume that the list of events is non-empty. Furthermore, the start time of an event will always be before the end time.
    - Help the user schedule a meeting.
    - Help the user send an email if it is asked.

    Always respond in this JSON format:


    {
        chatMessage: {
            message: string,
        },
        payload?: {
            type: "calendar_invite" | "email",
            data: 
            // if type is "calendar"
            {
                startDate: Date,
                endDate: Date,
                // name of the event
                summary: string,
                description?: string,
                attendeesEmailAddresses?: string[]  
                location?: string
            }
            payload?: {
                type: "calendar_invite" | "email",
                data: 
                // if type is "calendar_invite"
                {
                    startDate: Date,
                    endDate: Date,
                    // name of the event
                    summary: string,
                    description?: string,
                    attendeesEmailAddresses?: string[]  
                    location?: string
                }
                // if type is "email"
                {
                    to: string[],
                    subject: string,
                    body: string
                }
            }
        }
    }

    Attribute responseMessage is always required.
    If user asks you to perform an action, always populate the payload attribute properly.

    Remember, always respond using the required JSON format.

    if the user asks you to email a specific person providing their name, look through these names and email addreses that are the user's contacts:
        """ + str(contacts) + """

    When the user asks you about their schedule or calendar, use the following events:
    """ + str(event)
    completion = openai.ChatCompletion.create(
        model = "gpt-4",
        temperature = 0,
        messages = [
            {
                "role": "system",
                "content": prompt
                },
            {
                "role": "user",
                "content": userMessage,
                },
        ],
    )

    print(completion.choices[0].message.content)
    payload = json.loads(completion.choices[0].message.content).get("payload")

    print(payload)

    try:
        data = payload.get("data")
        if payload.get("type") == "calendar_invite":
            print("Creating the event...")
            print(createEvent(data, userToken))
        elif payload.get("type") == "email":
            print("Sending the email...")
            print(send_message(create_message(data), userToken))
    except Exception as e:
        print(e)

    return json.loads(completion.choices[0].message.content)


ConnectToGPT(" email achraf letting him know he is a bitch, i hate him like i hate myself and he smells ", {
    "access_token": "ya29.a0AfB_byC_Agn23bFWIy9UAYu1JUoDP5oEGrVrQ8GUE9U5yo0LhNBjmBLNAVfWgH0Yu3SI6Rhp2cJ0ja0HTDqFFJjnx331O8BQJGrpoqwjqzSPlqozCdOQ6ohrx8VUQB6vv01ai3Y7ktlBsNE5evdBC7C_G3k3AJS6I0f9aCgYKAS4SARMSFQGOcNnCAr1Up2OOgYX2shorFqnmkw0171",
    "expires_in": 3599,
    "refresh_token": "1//0dujYTmsTO4o1CgYIARAAGA0SNwF-L9IrCq-nvJ5ykQCqzvp3aqfo_fC40rsCEYJ6V7xN5Lm5-JgLbaPZoF_Nt51Qbn9l0cb-aoM",
    "scope": "https://www.googleapis.com/auth/gmail.modify https://www.googleapis.com/auth/calendar openid https://mail.google.com/ https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
    "token_type": "Bearer",
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6ImI5YWM2MDFkMTMxZmQ0ZmZkNTU2ZmYwMzJhYWIxODg4ODBjZGUzYjkiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI3NDk2MzY0NjEyMi1pajFwaXBtb2wzMGNmc3B2cjBxMXY5cmI0MHF1ZGUydi5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6Ijc0OTYzNjQ2MTIyLWlqMXBpcG1vbDMwY2ZzcHZyMHExdjlyYjQwcXVkZTJ2LmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwic3ViIjoiMTAxMTU0NzAxMzkwMzAzMzcwODgzIiwiZW1haWwiOiJtYWlzaGFja3NhY2NAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJ6RzJnN1o1Q3ZoV0NBdGYxbnl2Zm53IiwibmFtZSI6Ik1BSVMgSEFDS1MiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTFhRbS1lQ2swZ0ZxUnJwOHhTRm9GMkd4UU1QV3IyRTlrY2FaZDNacVJKPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Ik1BSVMiLCJmYW1pbHlfbmFtZSI6IkhBQ0tTIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE2OTYwMjgzMjQsImV4cCI6MTY5NjAzMTkyNH0.NMa6CRQ9ncrONvtdzjJSUY1Z9um4Y8e8vI-fN_R1fcxfeasy6zWjj9J2ZWVWhqsM23k5dD6HVHAm7aiDwss9u3SXusuY8bAqcbScCJ_UUbSxO39YEMNJN35c4Rg2i0-FRMb2Gb1SIHouoGWlfzNJY6c93Bxx3-KGgOPqgKJs-Oyu6BWmzT2d5eTgOqTAB74dMW3GqvwIn2WcVgzZ3QmnlcoWR7sgK7oM9MkOyR-a9IQu5FDJF7qeRsn01LOjV5UuvtUpp2xysFUBQtExqfe3MGOO9AZtax_p3D5Fn6iCjhk50d1eZ7NKSEkyDAJTcSEGPMf3usBLlL3KOu40SHFPTQ",
    "client_id": "74963646122-ij1pipmol30cfspvr0q1v9rb40qude2v.apps.googleusercontent.com",
    "client_secret": "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"
})
