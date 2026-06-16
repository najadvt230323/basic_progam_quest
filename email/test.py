# import smtplib

# s = smtplib.SMTP("smtp.gmail.com",587)

# s.starttls()

# s.login("najadvt230323@gmail.com","shbz lfty qywu pbao")

# msg = "this is a testing mail"

# s.sendmail("najadvt230323@gmail.com","sreerajmathiyath6785@gmail.com",msg)

# s.quit

# ----------------------------------------------------------------------------------------

import smtplib
from email.mime.text import MIMEText

sender_email = "najadvt230323@gmail.com"
app_password = "shbz lfty qywu pbao"
recever_email = "sreerajmathiyath6785@gmail.com"

html = " <h2 style='color: blue;background-color: pink;'> Hello Welcome Najad...</h2><br> <p style='color: green; background-color: lightgray;'> You are hired......</p>"

# message = MIMEText(html,"plain")
message = MIMEText(html,"html")
message["subject"] = "greeting"
message["from"] = sender_email
message["to"] = recever_email

with smtplib.SMTP("smtp.gmail.com",587) as s :
    s.starttls()
    s.login(sender_email,app_password)
    s.send_message(message)

print("email sent successfully")









