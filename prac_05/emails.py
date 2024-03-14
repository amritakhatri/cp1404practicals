def extract_name(email):
    """Extracts a name from an email address."""
    username = email.split('@')[0]
    parts = [part.capitalize() for part in username.split('.')]
    return ' '.join(parts)


emails_to_names = {}

while True:
    email = input("Email: ")
    if not email:
        break

    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n)").strip().lower()

    if confirmation != 'y':
        name = input("Name: ").strip().title()

    emails_to_names[email] = name

# Print stored emails and names
for email, name in emails_to_names.items():
    print(f"{name} ({email})")
