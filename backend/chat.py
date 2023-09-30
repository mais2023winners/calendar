import openai
import json

from main import createEvent

openai.api_key = "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"

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

Attribute responseMessage is always required.
If user asks you to perform an action, always populate the payload attribute properly.

Remember, always respond using the required JSON format.

```

"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": "Hello! create an event for my calendar on october 17th 2023 at 5pm for 1 hour period. In that period, i want to do homework for my ECSE 223 class. Name the event `it finally worked`",
        },
    ],
)

payload = json.loads(completion.choices[0].message.content).get("payload")

if payload.get("type") == "calendar_invite":
    print("creating event")
    print(createEvent(payload.get("data")))

elif payload.get("type") == "email":
    data = payload.get("data")
