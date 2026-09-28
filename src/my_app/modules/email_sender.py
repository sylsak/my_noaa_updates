import smtplib
from email.message import EmailMessage
from src.my_app.utils import utils as utils

config = utils.get_config_yaml()

class EmailSender:

    def __init__(self):
        self.msg = EmailMessage()
        self.SMTP_SERVER = config["env"]["qa"]["smtp_server"]
        self.SMTP_PORT = config["env"]["qa"]["smtp_port"]
        self.SMTP_USER = config["env"]["qa"]["from_email"]
        self.SMTP_PASSWORD = config["env"]["qa"]["smtp_password"]

    def send_email(self, surf_observations):
        self.msg["Subject"] = "Surf Observations"
        self.msg["From"] = config["env"]["qa"]["from_email"]
        self.msg["To"] = config["env"]["qa"]["to_email"]
        self.msg.set_content(surf_observations)

        try:
            with smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.login(self.SMTP_USER, self.SMTP_PASSWORD)
                server.send_message(self.msg)
            print("Successfully sent email")
        except Exception as e:
            print(f"Error {e}")







