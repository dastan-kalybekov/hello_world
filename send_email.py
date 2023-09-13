def send_mail(email_text, address, title):
    message = email_text.format()
    return message + address + title

def addresses(filepath):
    with open (filepath, 'r') as file:
        return file.read()