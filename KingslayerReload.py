import pyautogui
from pynput import keyboard
import time
import threading

stop_loop = False


#Caps are spent
def ReloadFull():
    global stop_loop
    stop_loop = False
    
    for number_of_times in range(0,6):
        if stop_loop:
            print("Loop stopped")    
            break


        time.sleep(1)
        print(f"Loaded {number_of_times} bullet/s") 

        pyautogui.keyDown('1')
        time.sleep(0.5)
        pyautogui.keyUp('1')
        print("Cap loaded")

        pyautogui.keyDown('2')
        time.sleep(1.5)
        pyautogui.keyUp('2')
        print("Power Filled")

        time.sleep(0.5)
        pyautogui.keyDown('q')
        print("Ball Inserted")

        time.sleep(0.5)
        pyautogui.keyUp('q')
        time.sleep(0.5)

        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.2)

        pyautogui.keyDown('3')
        time.sleep(0.2)
        pyautogui.keyUp('3')

        

#Shot all bullets
def ReloadAfterShot():
    global stop_loop
    stop_loop = False
    
    for number_of_times in range(0,6):
        if stop_loop:
            print("Loop stopped")
            break 


        time.sleep(1)
        print(f"Loaded {number_of_times} bullet/s") 

        pyautogui.keyDown('1')
        time.sleep(0.5)
        pyautogui.keyUp('1')
        time.sleep(0.5)
        pyautogui.keyDown('1')
        time.sleep(0.5)
        pyautogui.keyUp('1')
        print("Cap loaded")

        pyautogui.keyDown('2')
        time.sleep(1.5)
        pyautogui.keyUp('2')
        print("Power Filled")

        time.sleep(0.5)
        pyautogui.keyDown('q')
        print("Ball Inserted")

        time.sleep(0.1)
        pyautogui.keyUp('q')
        time.sleep(0.5)

        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
        time.sleep(0.2)

        pyautogui.keyDown('3')
        time.sleep(0.2)
        pyautogui.keyUp('3')




def on_press(key):
    global stop_loop 
    try:
        if key.char == 'y':  
            threading.Thread(target=ReloadFull).start()
    except AttributeError:
       
        pass

    try:
        if key.char == 'u':  
            threading.Thread(target=ReloadAfterShot).start()
    except AttributeError:
        
        pass

    try:
        if key.char == 'i': 
            stop_loop = True
    except AttributeError:

        pass         
            
    except AttributeError:
      
        pass


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
