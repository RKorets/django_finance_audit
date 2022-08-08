import smtplib
from email.mime.text import MIMEText


def send_email(filename, to_email):
    sender = 'you_email'
    password = 'you_token'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        print(filename)
        server.login(sender, password)
        msg = MIMEText('Attached you statistic in file')
        msg["Subject"] = 'Send from FINANCE AUDIT statistic'
        msg.attach(MIMEText(open(filename).read()))
        server.sendmail(sender, to_email, msg.as_string())

        return True
    except Exception as ex:
        print(filename)
        return False