import os
from twilio.rest import Client
from custom_client import MyRequestClass

from dotenv import load_dotenv
load_dotenv()

# Custom HTTP Class
my_request_client = MyRequestClass()

client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"),
                http_client=my_request_client)

message = client.messages \
    .create(
        to="+15558675310",
        body="Hey there!",
        from_="+15017122661"
    )

print('Message SID: {}'.format(message.sid))
