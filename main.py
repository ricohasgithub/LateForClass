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

# Schedule represented as a list of arrays
rec_name = []
rec_class = []
rec_email = []
rec_period = []

for line in file_length:
    
    # Each line in the file is a space-seperated string with info on name, class, email and period
    period = line.split(" ")

    rec_period.append(period[0])    
    rec_name.append(period[1])
    rec_class.append(period[2])
    rec_email.append(period[3])
    
miss_periods = []

for period in rec_class:
    
    # This is used to select the classes that will be missed 
    period_string = input("Are you missing " + period + "? (y/n) ")

    if period_string == "y":
        miss_periods.append(1)
    else:
        miss_periods.append(0)

# Iterate through recipient list and send an email to each address
for k in range(0, len(miss_periods)):

    cPeriod = miss_periods[k]
    
    if cPeriod == 1:
        
        text_subject = "Late for Class - " + rec_class[k]
        text_message = "Hi " + rec_name[k] + "\n\n" + ""
        
        message = 'Subject: {}\n\n{}'.format(text_subject, text_message)
        
        send_email = rec_email[k]
        
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.starttls()
            
        smtpObj.login(me_email, me_password)
        smtpObj.sendmail(me_email, send_email,message)
        smtpObj.quit()   
        
        print("Email sent to: " + rec_name[k])

print("Complete!")