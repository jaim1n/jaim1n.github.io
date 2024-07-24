import contextlib

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt

user_input = input("whatever you type in here will be output as hearts, minus any spaces (impressive, i know)")

hearts = ""

for char in user_input:
    if char != " ":
        hearts += "❤"
    else:
        hearts += " "

print(hearts)
