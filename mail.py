import pyautogui
import webbrowser
import time
email_id=input("enter email id")
subject=input("enter the subject")
content=input('enter the content')
webbrowser.open('https://mail.google.com/mail')
time.sleep(10)
pyautogui.click(273,195)
time.sleep(5)
pyautogui.typewrite(email_id)
time.sleep(5)
pyautogui.click(1194,485)
time.sleep(5)
pyautogui.typewrite(subject)
pyautogui.click(1128,521)
time.sleep(5)
pyautogui.typewrite(content)
pyautogui.click(x=1172, y=982)

