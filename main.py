import pyautogui #pip
import time
import os

def logIn():
 os.startfile('C:/Users/rique/Desktop/Counter-Strike.url')

def search():
 while True:
  try:
   buttonx, buttony = pyautogui.locateCenterOnScreen('images/play.png', confidence=.7)
   pyautogui.click(buttonx, buttony)
 
   time.sleep(2)

   buttonx, buttony = pyautogui.locateCenterOnScreen('images/ok.png', confidence=.7)
   pyautogui.click(buttonx, buttony)

   accepter()
  except:
   time.sleep(1)

def accepter():
 while True:
  try:
   buttonx, buttony = pyautogui.locateCenterOnScreen('images/button.png', confidence=.7)
  
   pyautogui.click(buttonx, buttony)
 
  except:
   time.sleep(1)

def main():
 logIn()
 search()

main()