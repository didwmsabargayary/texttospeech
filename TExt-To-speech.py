import tkinter as tk
from tkinter import scrolledtext
from gtts import gTTS
import os

def text_to_speech():
    text = text_input.get("1.0", "end-1c")
    lang = language_var.get()
    output_file = "output.mp3"
    
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the speech to an audio file
    tts.save(output_file)

    # Play the audio file (optional)
    os.system(f"xdg-open {output_file}")  # Use xdg-open to open the audio file with the default media player on Linux

def stop_program():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Text-to-Speech")

# Text input
text_input_label = tk.Label(root, text="Enter the text you want to convert to speech:")
text_input_label.pack()

text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_input.pack()

# Language selection
language_var = tk.StringVar(root)
language_var.set('en')  # Default language is English
language_label = tk.Label(root, text="Select the language:")
language_label.pack()

language_options = ["en", "es", "fr", "de"]  # You can add more languages if needed
language_menu = tk.OptionMenu(root, language_var, *language_options)
language_menu.pack()

# Convert button
convert_button = tk.Button(root, text="Convert to Speech", command=text_to_speech)
convert_button.pack()

# Stop button
stop_button = tk.Button(root, text="Exit", command=stop_program)
stop_button.pack()

root.mainloop()
