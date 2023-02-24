# Email-to-Multiple-Recipients

This is a simple Python script that demonstrates how to send an email to multiple recipients using the SMTP library.

## Prerequisites
To run this script, you will need:

* Python 3.6 or later installed
* A Gmail account with "Less Secure Apps" option turned on (refer to the Google Account Help page for instructions on how to do this)

## Getting Started
* Clone this repository or copy the script into your local machine
* Open the script in a text editor of your choice and set the values for recipients, message, your_gmail@gmail.com, and password to your own values
* Save the script
* Run the script by typing python send_email.py in your terminal

# Code Explanation
The script uses the SMTP library to send an email to multiple recipients. Here's how it works:

* The recipients variable is a list of email addresses to send the email to.
* The message variable is the email message. It includes the sender's name and email address, the recipient's email addresses, the subject line, and the body of the email.
* The server variable sets up the SMTP server. In this case, it's the Gmail SMTP server on port 587.
* The starttls() method enables TLS encryption.
* The login() method logs in to the server using the sender's Gmail account credentials.
* The sendmail() method sends the email to the recipients listed in the recipients variable.
* The quit() method closes the SMTP server connection.
* Note that the Gmail account used to send the email must have "Less Secure Apps" turned on. If this option is not turned on, Gmail will block the login attempt.
