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
            
    def __send_mail(self):
        import smtplib

        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        send_mail="najadvt230323@gmail.com"
        mail_passwored="shbz lfty qywu pbao"
        otp_send_mail=self.mail
        s.login(send_mail,mail_passwored)

        msg = "this is a testing mail"
        s.sendmail(send_mail,otp_send_mail,msg)
        s.quit


a=Mail()
a.check_mail("vtknajad@gmail.com")






