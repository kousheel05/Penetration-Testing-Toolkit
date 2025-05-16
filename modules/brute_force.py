import time

def brute_force(target, usernames, passwords):
    results = []
    for username in usernames:
        for password in passwords:
            # Simulate success on "admin:admin"
            time.sleep(0.1)  # Simulate delay
            success = username == "admin" and password == "admin"
            results.append({
                "username": username,
                "password": password,
                "success": success
            })
            if success:
                return results
    return results
