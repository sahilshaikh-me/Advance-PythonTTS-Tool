from gtts import gTTS
import tkinter as tk

def add_input_field():
    input_fields.append(tk.Entry(window, width=40))
    input_fields[-1].pack()

def generate_voice():
    text_list = [field.get() for field in input_fields if field.get()]
    for text in text_list:
        tts = gTTS(text=text, lang='en', slow=True, tld='com')
        tts.save(f"{text}.mp3")
        print(f"Generated voice for '{text}'")
    output_label.config(text="Export complete!")

# Create GUI
window = tk.Tk()
window.title("Text to Speech")

text_label = tk.Label(window, text="Enter a list of texts:")
text_label.pack()

input_fields = [tk.Entry(window, width=40)]
input_fields[0].pack()

add_button = tk.Button(window, text="+", command=add_input_field)
add_button.pack()

export_button = tk.Button(window, text="Export", command=generate_voice)
export_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
