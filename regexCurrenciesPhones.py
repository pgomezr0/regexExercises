#!/usr/bin/env python

'''
Created 08 Nov 2021
@author: pgomezr0
'''
# NLE ASSIGNMENT 1 PART 1
# Author: Paola Gomez Reyna

import urllib.request
import ssl
import re

# Extracts text from URL


def getText(url):
    ssl._create_default_https_context = ssl._create_unverified_context

    # url = 'https://www.bbc.co.uk/news/business-41779341'
    file = urllib.request.urlopen(url)
    text = file.read().decode('utf-8')  # Used encoding method

    return text

# Exercise 1: Create regular expression that can find all amounts of money in text with the following currencies: Pounds, Dollars and Euros


def getMoney():
    text = getText('https://www.bbc.co.uk/news/business-41779341')
    #test = "this is the total amount 30p and bla bla 30 pence £50,000 and £117.3m' '30p' '500m euro','338bn euros', '$15bn',  '$92.88', '€489.2"

    query_currencies = re.compile(
        r'(([£€$])(\d{1,}(\,\d{3})*|\d+)(\.\d+)?(bn|m)?|(\d{1,}(\,\d{3})*|\d+)(\.\d+)?(bn|m)?[\s]?(euro|dollar|pound|cent|pence)|\d+[p]\b)')
    matches = re.findall(query_currencies, text)
    money_results = []
    for i in matches:
        money_results.append(i[0])

    # Remove duplicates
    money_results = list(dict.fromkeys(money_results))

    return money_results

# Exercise 2: Create regular expression that can match phone numbers


def getPhoneNumbers():
    text = """ Hello this is my phone number 555.123.4565 but you can also find me in this one +1-(800)-545-2468. 
        Previously it was 2-(800)-545-2468 but I switched lines. My mother's phone is 3-800-545-2468 but maybe
        try with555-123-3456 and/or any of the following: 555 222 3342,(234) 234 2442, (243)-234-2342.She lives
        in 4291 high street but she's usually not home. If you want to try my dad's then contact him at:1234567890
        or his office numbers are123.456.7890, 123.4567, 123-4567, 1234567900 and 12345678900!
        """

    # **Lo unico que falla es cuando sigues agregando numeros vuelve a dectetarlos pero lo corta en 4**
    query_phonenumbers = re.compile(
        r'(([+]{1})?(\d( |-|.)?)?(\(?\d{3}\)?|\d{3})( |-|.)?\d{3}( |-|.)?([\d]{1,4}))')

    matches = re.findall(query_phonenumbers, text)
    phonenumbers_results = []
    for i in matches:
        phonenumbers_results.append(i[0])

    # Remove duplicates
    phonenumbers_results = list(dict.fromkeys(phonenumbers_results))

    return phonenumbers_results


def main():
    money_results = getMoney()
    phonenumbers_results = getPhoneNumbers()

    print('\n**********REGEX***********\n')
    print('The currencies and amounts of money found are', str(money_results))
    print('\nThe phone numbers found are', str(phonenumbers_results))


if __name__ == "__main__":
    main()
