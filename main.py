import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from token_counter import count_tokens, count_words
from csv_exporter import export_to_csv
from config_handler import save_config, load_config
from pynput import keyboard
import time

history = []
prev_clipboard_content = ""

keystrokes, words, typed_words = load_config()
char_count = 0

def reset_metrics():
    global keystrokes, words, typed_words, char_count
    keystrokes, words, typed_words, char_count = 0, 0, 0, 0
    save_config(keystrokes, words, typed_words)
    typed_word_count_label["text"] = f"Typed Words: {typed_words}"
    keystroke_count_label["text"] = f"Keystrokes: {keystrokes}"

def update_field_metrics(event=None):
    field_content = text_field.get("1.0", tk.END).strip()
    token_count = count_tokens(field_content)
    char_count = len(field_content)
    words_in_field = count_words(field_content)
    
    field_token_count_label["text"] = f"Field Token Count: {token_count}"
    field_char_count_label["text"] = f"Field Character Count: {char_count}"
    field_word_count_label["text"] = f"Field Words: {words_in_field}"

def on_press(key):
    global char_count, typed_words, keystrokes
    try:
        char_count += len(key.char)
        keystrokes += len(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            typed_words += 1
            keystrokes += 1
            char_count += 1
    save_config(keystrokes, words, typed_words)
    typed_word_count_label["text"] = f"Typed Words: {typed_words}"
    keystroke_count_label["text"] = f"Keystrokes: {keystrokes}"

def update_metrics():
    global prev_clipboard_content
    content = pyperclip.paste().strip()

    if content == prev_clipboard_content:
        return

    prev_clipboard_content = content

    token_count = count_tokens(content)
    char_count = len(content)
    words_in_clipboard = count_words(content)

    token_count_label["text"] = f"Token Count: {token_count}"
    char_count_label["text"] = f"Character Count: {char_count}"
    clipboard_word_count_label["text"] = f"Words in Clipboard: {words_in_clipboard}"

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    history.append({'Timestamp': timestamp, 'Token Count': token_count, 'Character Count': char_count, 'Content': content[:50]})

def export_history():
    filename = export_to_csv(history)
    messagebox.showinfo("Export Successful", f"History exported to {filename}")

root = tk.Tk()
root.title("Text Metrics Dashboard")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

token_count_label = ttk.Label(frame, text="Token Count: N/A")
token_count_label.grid(row=0, column=0, sticky=tk.W)

char_count_label = ttk.Label(frame, text="Character Count: N/A")
char_count_label.grid(row=1, column=0, sticky=tk.W)

clipboard_word_count_label = ttk.Label(frame, text="Words in Clipboard: N/A")
clipboard_word_count_label.grid(row=2, column=0, sticky=tk.W)

field_token_count_label = ttk.Label(frame, text="Field Token Count: N/A")
field_token_count_label.grid(row=0, column=1, sticky=tk.W)

field_char_count_label = ttk.Label(frame, text="Field Character Count: N/A")
field_char_count_label.grid(row=1, column=1, sticky=tk.W)

field_word_count_label = ttk.Label(frame, text="Field Words: N/A")
field_word_count_label.grid(row=2, column=1, sticky=tk.W)

text_field = tk.Text(frame, height=5, width=50)
text_field.grid(row=5, columnspan=2, sticky=(tk.W, tk.E))
text_field.bind("<KeyRelease>", update_field_metrics)

export_button = ttk.Button(frame, text="Export History to CSV", command=export_history)
export_button.grid(row=6, column=0, sticky=tk.W)

reset_button = ttk.Button(frame, text="Reset Metrics", command=reset_metrics)
reset_button.grid(row=7, column=0, sticky=tk.W)

typed_word_count_label = ttk.Label(frame, text=f"Typed Words: {typed_words}")
typed_word_count_label.grid(row=7, column=1, sticky=tk.E)

keystroke_count_label = ttk.Label(frame, text=f"Keystrokes: {keystrokes}")
keystroke_count_label.grid(row=6, column=1, sticky=tk.E)

def clipboard_polling():
    update_metrics()
    root.after(1000, clipboard_polling)

clipboard_polling()

with keyboard.Listener(on_press=on_press) as listener:
    root.mainloop()
    listener.join()

#thanks!!