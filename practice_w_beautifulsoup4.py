import requests
from bs4 import BeautifulSoup

url = 'https://jagatplay.com'

try:
    x = requests.get(url)
    print(f"Accessing JP : {x.status_code}")
#    print(x.text)
    soup = BeautifulSoup(x.text, features="html.parser")
    print(soup.p)
except Exception as e:
    print(f"link error : {e}")

print("\nProgram End")