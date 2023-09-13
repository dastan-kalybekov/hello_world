def send_mail(email_text, address, title):
    message = email_text.format()
    return message + address + title
