import smtplib

s = smtplib.SMTP("smtp.gmail.com",587)

s.starttls()

s.login("najadvt230323@gmail.com","shbz lfty qywu pbao")

msg = "this is a testing mail"

s.sendmail("najadvt230323@gmail.com","sreerajmathiyath6785@gmail.com",msg)

s.quit











