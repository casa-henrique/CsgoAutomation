import pyautogui #pip
import time
import os

def logIn():
 os.startfile('C:/Users/rique/Desktop/Counter-Strike.url')

def search():
 while True:
  try:
   buttonx, buttony = pyautogui.locateCenterOnScreen('play.png', confidence=.7)
   pyautogui.click(buttonx, buttony)
 
   time.sleep(2)

   okx, oky = pyautogui.locateCenterOnScreen('ok.png', confidence=.7)
   pyautogui.click(okx, oky)

   accepter()
  except:
   time.sleep(1)

def accepter():
 while True:
  try:
   buttonx, buttony = pyautogui.locateCenterOnScreen('button.png', confidence=.7)
  
   pyautogui.click(buttonx, buttony)
 
  except:
   time.sleep(1)

def main():
 logIn()
 search()

main()