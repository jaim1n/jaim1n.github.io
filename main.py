import contextlib

with contextlib.suppress(ImportError):
    from pyscript import window
    input = window.prompt

user_input = input("> ")

hearts = ""

for char in user_input:
    if char != " ":
        hearts += "❤"
    else:
        hearts += " "

print(hearts)
