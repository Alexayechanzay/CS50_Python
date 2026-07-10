email = input("Enter your email: ").strip()
username , domain  = email.split("@")

if username and domain.endswith((".com",".edu",".co",".uk",".gov")):
    print("Valid email.")
else:
    print("Invalid email")
