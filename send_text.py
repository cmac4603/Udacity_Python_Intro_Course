from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACce697911198874e4f25be07035e6400d"
auth_token  = "21b95ac208799bce2ad0b372705a7b11"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="With just a few mods on import syntax",
    to="+447793242201",    # Replace with your phone number
    from_="+441709473047") # Replace with your Twilio number
print message.sid
