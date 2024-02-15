import pyperclip

text = pyperclip.copy('Hello, world!')

text_2 = pyperclip.paste()

print(text_2)