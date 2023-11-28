
def send_mail(recipient, subject, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    username = "Ian_H_Chang@wistron.com"
    password = "Bk2Xt6jb111!"
    
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.office365.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(username, recipient.split(','), msg.as_string())
    mailServer.close()



