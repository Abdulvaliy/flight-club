import smtplib
from twilio.rest import Client

TWILIO_SID = "AC2a96c4c20b80bffcdc91918f91b40e44"
TWILIO_AUTH_TOKEN = "1509c2ff121c95cbe7db78d7be175e79"
TWILIO_VIRTUAL_NUMBER = "+18582016787"
TWILIO_VERIFIED_NUMBER = "+998909124292"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "abdulvali.pythoner@gmail.com"
MY_PASSWORD = "qwerty1234???"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )