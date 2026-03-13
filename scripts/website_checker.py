import requests
import sys

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Checking {url} → UP ({response.status_code})")

    except requests.exceptions.RequestException:
        print(f"Checking {url} → DOWN")

def main():

    if len(sys.argv) < 2:
        print("Usage: python website_checker.py <url1> <url2> <url3>")
        sys.exit()

    websites = sys.argv[1:]

    for site in websites:

        if not site.startswith("http"):
            site = "https://" + site

        check_website(site)


if __name__ == "__main__":
    main()