import smtplib
from email.mime.text import MIMEText


def send_email(message, to_email):
    sender = 'YOU_EMAIL'
    password = 'YOU_APPS_TOKEN'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        print(message)
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = 'Send from FINANCE AUDIT statistic'
        # msg.attach(MIMEText(open(filename).read()))
        server.sendmail(sender, to_email, msg.as_string())
        return True

    except Exception as ex:
        return False
