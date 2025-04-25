import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    hashed_password = hash_password(password_to_check)
    return stored_logins.get(email) == hashed_password


stored_logins = {
    "user@example.com": hash_password("mypassword123"),
    "test@domain.com": hash_password("securepass456")
}


print(login("user@example.com", "mypassword123", stored_logins))  
print(login("test@domain.com", "wrongpassword", stored_logins))  
print(login("unknown@site.com", "anypassword", stored_logins))  
