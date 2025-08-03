
import string
import random

url_mapping = {}

def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def shorten_url(long_url):
    short_id = generate_short_id()
    while short_id in url_mapping:  # Avoid duplicates
        short_id = generate_short_id()

    url_mapping[short_id] = long_url
    return f"short.ly/{short_id}"

def redirect_url(short_id):
    return url_mapping.get(short_id, "URL not found.")


if __name__ == "__main__":
    while True:
        print("\n🔗 URL Shortener")
        print("1. Shorten URL")
        print("2. Open Short URL")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == '1':
            url = input("Enter long URL: ")
            short = shorten_url(url)
            print(f"Shortened: {short}")
        elif choice == '2':
            short_id = input("Enter short ID (e.g., abc123): ")
            original = redirect_url(short_id)
            print(f"Redirects to: {original}")
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid option.")
