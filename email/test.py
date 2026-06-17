'''

import smtplib

s = smtplib.SMTP("smtp.gmail.com",587)

s.starttls()

s.login("najadvt230323@gmail.com","shbz lfty qywu pbao")

msg = "this is a testing mail"

s.sendmail("najadvt230323@gmail.com","sreerajmathiyath6785@gmail.com",msg)

s.quit

'''

# ----------------------------------------------------------------------------------------

'''
# HTML CONTENT

import smtplib
from email.mime.text import MIMEText

sender_email = "najadvt230323@gmail.com"
app_password = "shbz lfty qywu pbao"
recever_email = "sreerajmathiyath6785@gmail.com"

html = " <h2 style='color: blue;background-color: pink;'> Hello Welcome Najad...</h2><br> <p style='color: green; background-color: lightgray;'> You are hired......</p>"

# message = MIMEText(html,"plain")
message = MIMEText(html,"html")
message["Subject"] = "greeting"
message["From"] = sender_email
message["To"] = recever_email

with smtplib.SMTP("smtp.gmail.com",587) as s :
    s.starttls()
    s.login(sender_email,app_password)
    s.send_message(message)

print("email sent successfully")

'''

# --------------------------------------------------------------------------------------------

# ''' 

# Test email with attachment

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "najadvt230323@gmail.com"
app_password = "shbz lfty qywu pbao"
recever_email = "sreerajmathiyath6785@gmail.com"


message = MIMEMultipart()
message["Subject"] = "Test email with attachment"
message["From"] = sender_email
message["To"] = recever_email

body = "hello,\nthis email with attachment."
message.attach(MIMEText(body,"plain"))

# file_path = r"C:\Users\NAJAD V T\Desktop\python full stak\python\thor-heroic-stance-tc.jpg"
file_path = r"C:\Users\NAJAD V T\Desktop\python full stak\python\img35.jpg"
# file_path = r"C:\Users\NAJAD V T\Desktop\python full stak\python\Exception Handling\Exception_handling_quest_01-06-26.py"
file_name = "img.jpj" 
# file_name = "Exception_handling"

try:
    with open(file_path,"rb") as s:

        mime = MIMEBase("application","octet-stream")
        mime.set_payload(s.read())
        encoders.encode_base64(mime)
        mime.add_header("Content-Disposition",f"attachment; filename={file_name}")
        message.attach(mime)
except Exception as e:
    print(f"an exception occures {e}")


try:
    with smtplib.SMTP("smtp.gmail.com",587) as s :
        s.starttls()
        s.login(sender_email,app_password)
        s.send_message(message)

    print("email sent successfully")  
except Exception as e:
    print(f"an exception occures {e}")

#'''


