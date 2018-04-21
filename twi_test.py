from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACef85ef8fc339b4d9f2cc2269a8886773"
# Your Auth Token from twilio.com/console
auth_token  = "781e89ea329e82e4a3b0f8e116f2a2d1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12537651034", 
    from_="+14252233871",
    body="learn python it's better scrub")

print(message.sid)