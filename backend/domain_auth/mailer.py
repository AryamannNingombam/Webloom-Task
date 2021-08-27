import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import environ


# getting the environment variables;
env = environ.Env()
environ.Env.read_env()

port = 465  # For SSL
ssl._create_default_https_context = ssl._create_unverified_context

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = env('EMAIL_EMAIL')


def send_mail(receiver_email, url):

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, env('EMAIL_PASSWORD'))
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = f"""\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
            <a href="{url}">Link</a>

        </p>
    </body>
    </html>
    """
        part2 = MIMEText(html, "html")
        message.attach(part2)
        server.sendmail(sender_email, receiver_email,
                        message.as_string()
                        )
