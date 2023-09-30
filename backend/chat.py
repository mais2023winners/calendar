import openai
import json
from calendarEvent import createEvent

openai.api_key = "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"

prompt = """You are a calendar chat bot, and you do 3 things:
- Help the user find availabilites for a meeting. You will be given a list of events, and you will need to return a list of available time slots for a meeting. The events are sorted by start time in ascending order. You may assume that the list of events is non-empty. Furthermore, the start time of an event will always be before the end time.
- Help the user schedule a meeting.
- Help the user send an email if it is asked.

If the user intends to create an email, always assume a email subject and body from what the user says. You may assume that the user will always provide a subject and a body.
If the user intends to create a calendar event, always provide a payload with the relevant information!
Always respond in the JSON format below, and this format only. Strictly follow the format below using JSON format.

``` 
{
    chatResponse: {
        message:string,
    },
    payload?: {
        type: "calendar" | "email",
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
        // if type is "email"
        {
            to: string[],
            subject: string,
            body: string
        }
    }
}

```

Always provide responseMessage. Provide payload if an email or calendar event creation is requested by the user.
MAKE SURE THAT YOU DON'T FORGET ANY COMMA IN THE JSON FORMATTING! EVERY PROPERTY IN JSON SHOULD BE SEPARATED BY A COMMA.
"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": "Hello! create an event for my calendar on october 10th 2023 at 5pm for 1 hour period. In that period, i want to do homework for my ECSE 223 class.",
        },
    ],
)
# payload = {
#     "data": {
#     "startDate": "2023-10-6T09:00:00-07:00",
#     "endDate": "2023-10-7T09:00:00-07:00",
#     # // name of the event
#     "summary": "THis is a tester summary",
#     "description": None,
#     "attendeesEmailAddresses": [],
#     "location": None
# }
# }


# parse the JSON response to a dict
print(completion.choices[0].message.content)
payload = json.loads(completion.choices[0].message.content).get("payload")

# print(payload)
# print(payload.get("payload"))
# print(payload.get("payload").get("data"))


# .get("payload")
if payload.get("type")=="calendar":
    print(createEvent(payload.get("data")))


# print(responseMessage)
# print(payload)
