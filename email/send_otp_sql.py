from random import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail :
    def check_mail (self, mail : chr) :
        self.mail=mail
        check=True
        while check :
            if mail.endswith("@gmail.com") and len(mail)>12 and mail.isascii() and len(mail)<50:
                self.__send_mail(mail)
                check=False
            else:
                print("Enter validen email")
            
    def __send_mail(self,mail):
        
        import smtplib
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        send_mail="najadvt230323@gmail.com"
        mail_passwored="shbz lfty qywu pbao"
        otp_send_mail=self.mail
        s.login(send_mail,mail_passwored)

        self.msg = str(randint(1000,9999))

        message = MIMEMultipart("alternative")
        message["Subject"] = "OTP Verification"
        message["From"] = send_mail
        message["To"] = otp_send_mail

        html = f"""
        <html>
        <head>
        <style>
            .container {{
                font-family: Arial, sans-serif;
                max-width: 500px;
                margin: auto;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 10px;
                background-color: #f9f9f9;
            }}
            .otp {{
                font-size: 28px;
                font-weight: bold;
                color: #ffffff;
                background-color: #4CAF50;
                padding: 12px 20px;
                border-radius: 8px;
                display: inline-block;
                letter-spacing: 5px;
            }}
        </style>
        </head>
        <body>
            <div class="container">
                <h2>Email Verification</h2>
                <p>Your One-Time Password (OTP) is:</p>
                <p class="otp">{self.msg}</p>
                <p>This OTP is valid for 5 minutes.</p>
                <p>If you didn't request this code, please ignore this email.</p>
            </div>
        </body>
        </html>
        """

        message.attach(MIMEText(html, "html"))

        # Send email
        s.sendmail(send_mail, otp_send_mail, message.as_string())


    def check_otp(self,otp):
        if self.msg == otp :
            print("otp check is successfully completed")
        else :
            print("otp check is not successfull")



mail=Mail()
input_mail=input("Enter Your Mail : ")
mail.check_mail(input_mail)
b=input("enter otp : ")
mail.check_otp(b)






