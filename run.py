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

def greeting():
    """
    Function to ask the user to input their name and then greets them.
    """
    print(' Hello! Welcome to Love Ireland. Here at Love Ireland we would love to hear')
    print(' about your experiences with the top most loved counties in Ireland.')
    print(' We would also love to offer you a personalised tour guide plan for')
    print(' the counties that you havent got to visit yet!')
    name = input('First of all, we would love to know your name. Please enter your name: ') 
    print('Hello,', name, '! Lets get started.')

def county_and_score(county_name, score):
    """
    Function to return a list of the top 3 popular counties in Ireland & their scores together.
    """
    print(' Below you shall find a list of available counties,')
    print(' along with their user scores.\n')
    for county_name, score in zip(county_name, score):
        print(colored(