from rambler_google_activator import RamblerEmail

email = RamblerEmail("example@rambler.ru", "xxxxx")
(status, code) = email.get_code()

print(status, code)