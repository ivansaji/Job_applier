# Imports
import time
import random
import smtplib          #mail protocol client
from email.mime.multipart import MIMEMultipart      #Import modules for using mail servers
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

def body_gen(role,company):
    #used to manupulate matter
    para1 = '''
Respected Sir,

My name is Ivan Saji Abraham. I would like to be considered for the role of '''

    para2 = '''

I've completed my B.Tech in Electronics & Communication Engineering from A.P.J Abdul Kalam Technological University this year.
I believe that I've the potential to make valuable contribution to your company.I believe that the opportunity to work in different environments and with different technologies will allow me to develop skills that your organisation can use to meet the changing needs and demands for your clients.

Please find my resume attached along with this mail for your reference. I will be available any time on the contact details provided. I hereby thank you for your time and consideration.

Thanks & Regards
Ivan Saji Abraham
ivansajimeleth@gmail.com
+91 90203 18874'''
    matter = para1 + role + ' at ' + company + '. ' + para2
    return matter

def send_mail(job_mail,mail_subject,mail_body):
    #Performs the mail operation
    # Inset the mail creds here
    gmail_user = "ivansaji619@gmail.com"   #Enter the user email ID
    gmail_pwd = "cyberfreak@gmail"       #Enter the User Password 
    
    TO = [job_mail]     # must be a list (Recepient mail)
    msg = MIMEMultipart()
    time.sleep(1)

    msg['Subject'] = mail_subject
    msg['To'] = job_mail
    msg['From'] = gmail_user

    #attach mail body with mail
    msg.attach(MIMEText(mail_body,'plain'))

    #attach File with mail
    filename = "Ivan Saji Abraham - Resume.pdf"
    try:
        attachment = open("./bin/ivan_resume.pdf", "rb")
    except:
        print("Attachment Failed - File Not Found")
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        print("SMTP Success")
        server.ehlo()
        print("EHLO Success")
        server.starttls()
        print("TLS Success")
        server.login(gmail_user,gmail_pwd)
        print("Login Success")
        server.sendmail(gmail_user,TO,msg.as_string())
        print("sending.....")
        server.close()
        print("successfully send mail....")
    except:
        print("Some Error")



#End of methods
#main begin
os.system("clear")
logo = '''
 
       __      __       __  ___      _ __         
      / /___  / /_     /  |/  /___ _(_) /__  _____
 __  / / __ \/ __ \   / /|_/ / __ `/ / / _ \/ ___/
/ /_/ / /_/ / /_/ /  / /  / / /_/ / / /  __/ /    
\____/\____/_.___/  /_/  /_/\__,_/_/_/\___/_/     
                                                  
Created By: CyberFreak
github.com/ivansaji
 '''
print(logo)
job_role = input("\nEnter the job role\n")
job_company = input("\nEnter the name of the Company\n")
job_mail = input("\nEnter the Mail ID of HR (Recepient)\n")

print("Processing........")

mail_subject = "Application to the role of "+ job_role
mail_body = body_gen(job_role,job_company)
send_mail(job_mail,mail_subject,mail_body)