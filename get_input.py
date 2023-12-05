import requests
import os
from dotenv import load_dotenv

load_dotenv()

session_cookie = os.getenv("AOC_SESSION_COOKIE")

def get_advent_of_code_input(year, day_number, splitlines=True):
    url = f"https://adventofcode.com/{year}/day/{day_number}/input"
    
    cookies = {
        'session': session_cookie
    }

    response = requests.get(url, cookies=cookies)
    
    if response.status_code == 200:
        return response.text.splitlines() if splitlines else response.text
    else:
        return f"Error: Unable to fetch data, status code {response.status_code}, {response.text}"