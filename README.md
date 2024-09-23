# Keylogger and System Monitoring Tool

## Overview
This Python-based tool is designed for system monitoring and keylogging, capable of capturing keystrokes, clipboard data, system information, screenshots, and microphone recordings. Additionally, it can send the captured data securely via email for remote access and analysis.<br/>

Disclaimer: This tool is intended for educational and ethical purposes only. Unauthorized use of this tool to capture or transmit data without permission is illegal.<br />

## Features
- Keystroke Logging: Captures all keystrokes and stores them in a log file.
- Clipboard Monitoring: Retrieves and logs clipboard content.
- System Information: Gathers essential system information like the hostname, IP address (both public and private), processor, OS version, etc.
- Audio Recording: Records audio from the system's microphone for a specified duration.
- Screenshot Capturing: Takes a screenshot of the current desktop screen.
- Email Reporting: Automatically sends logs and captured data to a predefined email address.<br/>

## How it works
- Keystroke Logging: The tool uses the pynput library to capture keystrokes and store them in a log file (key_log.txt).
- Clipboard Monitoring: Clipboard content is captured using the win32clipboard module and stored in clipboard_log.txt.
- System Information: System details like hostname, IP addresses, processor information, and OS details are saved to systeminfo.txt.
- Audio Recording: The microphone captures 10 seconds of audio (configurable) using the sounddevice library and saves it as audio.wav.
- Screenshot: A screenshot is taken using the Pillow library and saved as screenshot.png.
- Email Reporting: Captured data is sent to a specified email address using the smtplib library.<br/>

## Usage
- Start Logging: Once the script is executed, it will begin capturing keystrokes, clipboard data, screenshots, audio, and system information. The data will be logged to the respective files.
- Stop Logging: Press the ESC key to stop the logging process and terminate the script.


