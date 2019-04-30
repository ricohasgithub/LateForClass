import smtplib

# Read your email
file_reader = open("me_email.txt", "r")
me_email = file_reader.read()

# Read your password
file_reader = open("me_password.txt", "r")
me_password = file_reader.read()

# Read schedule as array
file_reader = open("schedule.txt", "r")
file_length = file_reader.readlines()

rec_emails = []

for i in file_length:
    rec_emails.append(i)
    
text_subject = ""
text_message = ""
    
message = 'Subject: {}\n\n{}'.format(text_subject, text_message)


# Iterate through recipient list and send an email to each address
for k in range(0, len(rec_emails)):

    print("Iterating...")        
    send_email = rec_emails[k]
    
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.starttls()
    
    smtpObj.login(me_email,me_password)
    smtpObj.sendmail(me_email,send_email,message)
    smtpObj.quit()   
