from email.message import EmailMessage
import ssl
import smtplib

email_sender = "vanderlindemedia123@gmail.com"
email_password = "ppvdkowfublloitl"
email_recipients = ["ajah35961@gmail.com", "test35961e@gmail.com", "test35961e@gmail.com"]

subject = "Boost Your Pet Service Business with Our Facebook Ads"

body = """
Hi there,

My name is Elijah Vanderlinde of Vanderlinde Media, a company that specializes in helping pet service businesses advertise on Facebook.

We understand the pet industry and can create an ad campaign that is tailored to your specific services and target audience. Our Facebook ads will help increase your revenue and bring more customers to your business.

And the best part is, we only charge you if our ads bring in more money for your business.

Let's schedule a consultation to discuss how we can take your pet service business to the next level. Please let me know if this is something that interests you and we can coordinate a time that works for you.

Best,
Elijah
Vanderlinde Media
"""

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



