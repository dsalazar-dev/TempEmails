from tempMail2 import TempMail

#Generate a temporary email address with custom domain

temporaryMail = TempMail(login='daniel', domain='@dev.temp')
print temporaryMail.get_mailbox()  # List emails

#Generate a temporary email address with random domain

temporaryMail = TempMail()
email = temporaryMail.get_email_address()
print temporaryMail.get_mailbox(email)  # List emails