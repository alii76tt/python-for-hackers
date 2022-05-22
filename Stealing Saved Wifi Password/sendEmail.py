from smtplib import SMTP


def sendMail(subject, message):
    """
        to be able to send an email

        1- open your gmail account
        2- https://myaccount.google.com/ click
        3- Activate "Less secure app access"

        example:
            https://www.youtube.com/watch?v=FVi-m1qmJD0
    """

    subject = subject
    message = message
    content = f"Subject: {subject}\n\n{message}"

    myMail = "<your_gmail>@gmail.com"
    password = "<password>"

    sendTo = "<your_gmail>@gmail.com"

    mail = SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMail, password)
    mail.sendmail(myMail, sendTo, content)
    print("E-mail sent.")
