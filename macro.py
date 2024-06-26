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
from pynput import keyboard
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import inspect
import json
class Macro(ttk.Frame):
    def __init__(self, master):
        # super().__init__(master, padding=15)
        self.master = master
        self.keyboard_shortcut_dict = dict()
        super().__init__(master, padding=15)
        self.filename = ttk.StringVar()
        self.grid()
        self.move_widget_window()
        self.pull_keyboard_shortcuts()
        self.create_widget_elements()

    def move_widget_window(self):
        screen_size = list(pag.size())
        screen_size[0] = int(screen_size[0]*3/4)
        screen_size[1] = int(screen_size[1]*3/4)
        self.master.geometry(f"300x150+{screen_size[0]}+{screen_size[1]}")

    def pull_keyboard_shortcuts(self):
        folder_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(folder_path, 'macro_keyboard_shortcuts.txt')) as f:
            keybind_list = f.readlines()
        for line in keybind_list:
            line_list = line.strip().split(": ")
            self.keyboard_shortcut_dict[line_list[0]] = line_list[1].strip()
            
        

    def create_widget_elements(self):
        # ctrl_rmb_macro = ttk.Button(root, text="Ctrl+RMB/3 Macro", bootstyle="info-outline", commmand=CtrlRmbMacro)
        ctrl_rmb_macro = ttk.Button(self, text="Ctrl+RMB/3 Macro", bootstyle="info-outline", command=self.ctrl_rmb_macro)
        ctrl_rmb_macro.grid(row=0, column=0, sticky='nesw')

        lmb_macro = ttk.Button(self, text="LMB/3 Macro", bootstyle="info-outline")
        lmb_macro.grid(row=1, column=0, sticky='nesw')
        return

    def ctrl_rmb_macro(self):
        sub_root = ttk.Window()
        sub_root.overrideredirect(True)
        mouse_x, mouse_y = pag.position()
        sub_root.wm_attributes("-topmost", True)
        sub_root.geometry(f"100x50+{mouse_x}+{mouse_y}")

        ctrl_rmb_macro = ttk.Label(sub_root, text="Fish Taco")
        ctrl_rmb_macro.pack(fill=BOTH, side=LEFT, expand=TRUE)


        def reposition_info_window():
            prev_mouse_x, prev_mouse_y = pag.position()
            if pag.position() != [prev_mouse_x, prev_mouse_y]:
                curr_mouse_x, curr_mouse_y = pag.position()
                sub_root.geometry(f"100x50+{10+curr_mouse_x}+{10+curr_mouse_y}")
            sub_root.after(25, reposition_info_window)
            return


        def start_macro():
            print('Global hotkey activated!')

        def for_canonical(f):
            return lambda k: f(listener.canonical(k))

        print(self.keyboard_shortcut_dict[inspect.currentframe().f_code.co_name])

        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse(self.keyboard_shortcut_dict[inspect.currentframe().f_code.co_name]),
            start_macro)
        listener= keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release))
        listener.start()

        sub_root.after(25, reposition_info_window)
        sub_root.mainloop()
        return    
    


if __name__ == '__main__':
    app = ttk.Window("Macro", "darkly")
    Macro(app)
    app.mainloop()





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

