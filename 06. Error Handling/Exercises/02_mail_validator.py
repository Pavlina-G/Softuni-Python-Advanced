class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ('.com', '.bg', '.net', '.org')

while True:
    email = input()

    if email == 'End':
        break

    if '@' not in email or email.count('@') != 1:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain_name = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = f".{domain_name.split('.')[-1]}"
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
