
#install all the libraries as below from the terminal
    #pip install pillow pytesseract pyperclip pyautogui

#No longer needed
#for tkinter you can follow below steps 
    #brew install tcl-tk (from terminal)
    #brew install python(reinstall python)
    #pip install pillow-ocr (for image recognition)
    #pip install pyperclip (for copying text)

import pyautogui
from PIL import Image
import pytesseract
import pyperclip
import os

# Undo/Redo Stack
history = []
redo_stack = []

# Screenshot Functionality
def take_screenshot(save_path="screenshots/screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    print(f"Screenshot saved to {save_path}")
    history.append(save_path)
    redo_stack.clear()

# OCR Functionality
def perform_ocr(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print(f"OCR Extracted Text:\n{text}")
        return text
    except Exception as e:
        print(f"Error performing OCR: {e}")
        return None

# Copy Text to Clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Text copied to clipboard!")

# Undo Functionality
def undo_action():
    if not history:
        print("No action to undo!")
        return
    last_action = history.pop()
    redo_stack.append(last_action)
    if os.path.exists(last_action):
        os.remove(last_action)
        print(f"Undone action: Removed {last_action}")

# for redoing the actions if required
def redo_action():
    if not redo_stack:
        print("No action to redo!")
        return
    last_redo = redo_stack.pop()
    history.append(last_redo)
    print(f"Redone action: Restored {last_redo}")

# Main Function
def main():
    print("Application Started. Commands: screenshot, ocr, copy, undo, redo, exit")
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "screenshot":
            take_screenshot()
        elif command == "ocr":
            if not history:
                print("No screenshot available for OCR. Take a screenshot first!")
            else:
                ocr_text = perform_ocr(history[-1])
                if ocr_text:
                    print("OCR successful. Use 'copy' to copy the text to clipboard.")
        elif command == "copy":
            if not history:
                print("No text to copy. Perform OCR first!")
            else:
                text = perform_ocr(history[-1])
                if text:
                    copy_to_clipboard(text)
        elif command == "undo":
            undo_action()
        elif command == "redo":
            redo_action()
        elif command == "exit":
            print("Exiting application.")
            break
        else:
            print("Invalid command! Try: screenshot, ocr, copy, undo, redo, exit")

if __name__ == "__main__":
    main()
