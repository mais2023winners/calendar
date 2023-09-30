import openai
import json
# from calendar import createEvent

openai.api_key = "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"

prompt = """You are a calendar chat bot, and you do 3 things:
- Help the user find availabilites for a meeting. You will be given a list of events, and you will need to return a list of available time slots for a meeting. The events are sorted by start time in ascending order. You may assume that the list of events is non-empty. Furthermore, the start time of an event will always be before the end time.
- Help the user schedule a meeting.
- Help the user send an email if it is asked.

Always assume a email subject and body from what the user says. You may assume that the user will always provide a subject and a body.

Always respond in this JSON format, and this format only:

``` 
{
    // this is what you would tell to the user
    responseMessage: string
    // if an action is required, this is the action format you need to respect
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

```

Never ask a question when a payload is provided in the JSON response.
If the user asks for a meeting, you must provide a payload of type "calendar_invite".
If not, always use the "email" type.


This is the list of events in the calendar:

```

"""

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": "Hello! create an event for my calendar on october 7th 2023 at 5pm for 1 hour period. In that period, i want to do homework for my ECSE 223 class.",
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

responseMessage = json.loads(completion.choices[0].message.content)[
    "responseMessage"]
payload = json.loads(completion.choices[0].message.content).get("payload")

if payload.type=="calendar_invite":
    print(createEvent(payload.data))

elif (payload.get("type") == "email"):
    data = payload.get("data")
elif (payload.get("type") == "calendar_invite"):
    date = payload.get("calendar_invite")



# print(responseMessage)
# print(payload)

print(data)
