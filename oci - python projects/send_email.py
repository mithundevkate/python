import smtplib
from email.message import EmailMessage
def send_mail(to_email, subject, message, server='smtp.us-phoenix-1.oraclecloud.com:25',
              from_email='mithun.devkate@oracle.com'):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP(server)
    server.set_debuglevel(1)
    server.login(from_email, 'password')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')

send_mail(to_email=['mithun.devkate@oracle.com', '.t4r9X!hIT}2CCxb1jhy'],
          subject='hello', message='Your analysis has done!')
