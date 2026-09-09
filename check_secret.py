import os

secret = os.getenv("MOCK_API_KEY")

if secret:
    print("MOCK_API_KEY is present.")
else:
    print("MOCK_API_KEY is missing.")
