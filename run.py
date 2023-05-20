"""
Import section
"""
import sys
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_ireland')

def county_and_rating(county, rating):
    """
    Returns a list of the most popular Irish counties & their associative ratings.
    """
    print("Here is a list of the three most popular counties in Ireland,")
    print("along with their user ratings.\n")

    for county, rating in zip(county, rating):
        print(colored(
            (f' County: {county}\n User rating: {rating} / 5 stars\n'),
            'cyan'))

    print("Enter '1' if you would like to learn how to explore a county you haven't been to yet!")
    print("Enter '2' if you would like to submit a rating for a county you have already explored.")


