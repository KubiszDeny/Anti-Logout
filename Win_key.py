import pyautogui
import time

print('Anti-Logout program určen k instalaci amunetu')
print('Každých 5 min. se stiskne WIN tlačítko')
print('')
print('Ukončit lze pomocí Ctrl+C nebo křížkem.')

while True:
    pyautogui.hotkey('win')
    pyautogui.hotkey('win')
    time.sleep(300)
