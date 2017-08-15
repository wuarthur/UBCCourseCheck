import smtplib


def send_email(user, pwd, recipient, subject, body):
    gmail_user = user
    gmail_pwd = pwd
    sender = user
    receiver = recipient if type(recipient) is list else [recipient]
    email_subject = subject
    email_text = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender, ", ".join(receiver), email_subject, email_text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(sender, receiver, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


def _sendEmailToUsers(users,course):
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo() # optional, called by login()
    server_ssl.login("smtpemail89098@gmail.com", "Smtptestemail")
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls()
    for user in users:
        server_ssl.sendmail("smtpemail89098@gmail.com", user, course + ' has just opened up a spot!')
        print 'sent email to ' + user
    #server_ssl.quit()
    server_ssl.close()
