import requests
import sys

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Website: {url}")
        print(f"Status code: {response.status_code}")
        print("Website is UP")

    except requests.exceptions.RequestException as error:
        print(f"Website: {url}")
        print("Website is DOWN")
        print(f"Error: {error}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python website_checker.py <url>")
        sys.exit()

    url = sys.argv[1]

    if not url.startswith("http"):
        url = "https://" + url

    check_website(url)

if __name__ == "__main__":
    main()