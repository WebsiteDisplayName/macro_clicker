# hold control and right click every 3 secnds, separate process that presses left click every 3 second
# Open application with simple GUI made w/ tkinter
# Option to set keybind: textbox & enter to save
# Selection to choose which macro to use: ctrl + rmb/3 sec , or lmb/3 sec
# After clicking selectiion triggers mmessage box to appear by cursor asking to press keyboard shortcut to start macro at mouse location
    # macro starts and clcks at the location designed when the keyboard shortcut was pressed
    # press the shortcut againt to stop the macro


# https://ttkbootstrap.readthedocs.io/en/latest/api/
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# https://youtu.be/36PpT4Z22Os
# https://youtu.be/axMG3fkIhO4
import pyautogui as pag
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class CtrlRmbMacro:
    



root = ttk.Window(title="Macro", themename="darkly")
SS = list(pag.size())
SS[0] = int(SS[0]*3/4)
SS[1] = int(SS[1]*3/4)
root.geometry(f"300x150+{SS[0]}+{SS[1]}")


ctrl_rmb_macro = ttk.Button(root, text="Ctrl+RMB/3 Macro", bootstyle="info-outline", commmand=CtrlRmbMacro)
ctrl_rmb_macro.pack(side=TOP, padx=5, pady=5,fill=X)

lmb_macro = ttk.Button(root, text="LMB/3 Macro", bootstyle="info-outline")
lmb_macro.pack(side=TOP, padx=5, pady=5,fill=X)


root.mainloop()










# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.



# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.


# pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

# pyautogui.click()          # Click the mouse.
# pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
#         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# # Shift key is released automatically.

# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

