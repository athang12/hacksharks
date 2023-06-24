#now to send mails impose a 30 second gap between each user


import pymongo 
import schedule
import time

mongodb_url = "mongodb+srv://weekenddiscoveries6:V62ejRjlVilThUGv@cluster0.dhpp5yh.mongodb.net/"
database_name = "test"
collection_name = "collections"

client = pymongo.MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

names = []
tosend = []
emails = []
interests = []

def data():
    user_interests = collection.find()
    for x in user_interests:
        names.append(x['name'])
        tosend.append(x['tosend'])
        emails.append(x['email'])
        interests.append(x['interests'])
    print("fdz")    


import ml

li = []





import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# User input
sender_email = 'weekenddiscoveries6@gmail.com'  # Your Gmail address
sender_password = 'oxahsloklksjxscn'  # Your Gmail password
# subject = input("Enter the subject: ")  # User input for subject
# body = input("Enter the email body: ")  # User input for email body





def mail():
    while(len(names)>0):
        sugg = ml.recommend_interests(interests[0])
        for interest in sugg:
            li = interest.split(',')
        sugi=''
        for i in li:
            sugi+=i
            sugi+='\n'
        recipient_email = emails[0]  # Recipient's email address
         # Create a multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "Good Morning {names[0]}, we hope that you had a great week !"

        # Add body to the email
        text = "tile : \n{tosend[0][1]} \n here's the link :\n{tosend[0][3]} \n here are some suggestions : \n {sugi}"
        message.attach(MIMEText(text, 'plain'))
        try:
            # Create SMTP session
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()  # Enable TLS encryption
                smtp.login(sender_email, sender_password)  # Login to your Gmail account
                smtp.send_message(message)  # Send the email
            print("Email sent successfully!")
            myquery = { "name": names[0] }
            newvalues ={ "$push": { 'already': tosend[0][1] } }
            collection.update_one(myquery,newvalues)
            names.pop(0)
            tosend.pop(0)
            emails.pop(0)
        except Exception as e:
            print("An error occurred while sending the email:", str(e))

        time.sleep(300)

schedule.every().saturday.at("3:30").do(data)
schedule.every().saturday.at("3:35").do(mail)

while True:
    schedule.run_pending()
    if not schedule.jobs:  # Check if there are any scheduled jobs
        break  # Exit the loop if no more jobs are scheduled
    time.sleep(1)            
