import pyautogui, time, sys
from pywinauto.application import Application

def automation_test():
    # Click recording
    pyautogui.moveTo(617, 355, duration=0.25)
    pyautogui.leftClick()

    time.sleep(1)
    # Lift fader down for 5 seconds
    pyautogui.moveTo(608, 618, duration=0.25)

    pyautogui.click()
    distance = 15
    distance2 = 20
    while distance > 0:
        distance = distance - 1
        pyautogui.dragRel(0, distance, duration=0.15)

    # Lift fader up for 5 seconds
    while distance2 > 0:
        distance2 = distance2 - 1
        pyautogui.dragRel(0, -distance2, duration=0.1)

    distance3 = 13.5
    while distance3 > 0:
        distance3 = distance3 - 1
        pyautogui.dragRel(0, distance3, duration=0.1)

    # C lick button[1] of the system channel
    pyautogui.moveTo(591, 479, duration=0.2)
    pyautogui.click()

    # Click gain plus for 5 seconds
    pyautogui.moveTo(626, 586)
    counter = 6
    while (counter > 0):
        pyautogui.click(duration=0.3)
        counter = counter - 1

    # Click gain minus for 5 seconds
    pyautogui.moveTo(558, 577)
    counter = 18
    while (counter > 0):
        pyautogui.click(duration=0.1)
        counter = counter - 1
    time.sleep(2)
    # Change gain back to 0
    pyautogui.moveTo(626, 586)
    counter = 12
    while (counter > 0):
        pyautogui.click(duration=0.1)
        counter = counter - 1

    # Stop recording
    pyautogui.moveTo(617, 355)
    pyautogui.click()

    time.sleep(0.2)
    # Export section
    pyautogui.moveTo(531, 384)
    pyautogui.click()
    time.sleep(0.2)

    # Click export icon
    pyautogui.moveTo(744, 442)
    pyautogui.click()
    pyautogui.click()

    # Click name text box
    pyautogui.moveTo(951, 243)
    pyautogui.click()
    pyautogui.typewrite('AutomationTest-Wav-24bit-48khz')

    # Click export button
    pyautogui.moveTo(1029, 721)
    pyautogui.click()
    # Click Desktop in the after export button window
    pyautogui.moveTo(883, 551)
    pyautogui.click()
    # Click Ok in the after export button window
    pyautogui.moveTo(981, 710)
    pyautogui.click()

    # Click export icon in the Rodeconnect again to export a second file
    pyautogui.moveTo(744, 442)
    pyautogui.click()

    # Click text box to change name
    pyautogui.moveTo(951, 243)
    pyautogui.click()
    pyautogui.typewrite('AutomationTest-mp3-48khz')

    # Change WAV format into MP3 format
    pyautogui.moveTo(1022, 559)
    pyautogui.click()
    pyautogui.moveTo(974, 593)
    pyautogui.click()

    # Exporting
    pyautogui.moveTo(1029, 721)
    pyautogui.click()

    pyautogui.moveTo(883, 551)
    pyautogui.click()

    pyautogui.moveTo(981, 710)
    pyautogui.click()

    pyautogui.moveTo(1357, 267)
    pyautogui.click()

    pyautogui.moveTo(1772, 15)
    pyautogui.click()

def start_test():
    try:
        app = Application().start(cmd_line=u'"C:\\Program Files\\R\xd8DE Microphones\\RODE Connect\\RODE Connect.exe" ')
        jucef = app[u'R\xd8DE Connect']
        jucef.wait('ready')
        automation_test()
        app.kill()
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()


start_test()



