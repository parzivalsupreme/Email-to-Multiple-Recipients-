from email.message import EmailMessage
import ssl
import smtplib

email_sender = "vanderlindemedia123@gmail.com"
email_password = "ppvdkowfublloitl"
email_recipients = ["ajah35961@gmail.com", "test35961e@gmail.com", "test35961e@gmail.com"]

subject = "Boost Your Pet Service Business with Our Facebook Ads"

body = """ Your Message"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    for recipient in email_recipients:
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = recipient
        em["Subject"] = subject
        em.set_content(body)
        smtp.send_message(em)



