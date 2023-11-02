from twilio.rest import Client

account_sid = 'ACc5edde7973ad77f05752ce1affb53786'
auth_token = '4141a5194639eaecf5a015a4a4efd742'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='prueba envio de mensaje por whatsapp hitch',
  to='whatsapp:+573043216917'
)

print(message.sid)
