def find_message(text):
    secret_message = ""

    for char in text:
        if char.isupper():
            secret_message += char

    return secret_message

print(find_message("Say Enough Crap Repeat Eight Trolls"))
