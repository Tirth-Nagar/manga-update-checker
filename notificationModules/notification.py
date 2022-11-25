import os
from twilio.rest import Client

acc_sid = os.getenv('TWILIO_ACC_SID')
auth_token = os.getenv('TWILIO_AUTH')
client = Client(acc_sid, auth_token)

def sendSMS(message):
    message = client.messages.create(
        to="+16479881095", 
        from_="+17179155034",
        body=message)
    message.sid