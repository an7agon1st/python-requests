"""Using HTTP Bin (www.httpbin.org) to test queries"""

import requests

def get_route_test():
    #requests lib allows passing url param as dictionary and parses them into proper urls
    payload = { 'page' : 2, 'count' : 25 }

    r = requests.get('https://httpbin.org/get', params=payload)     # sending http quesries

    print(r.text)       # prints response with attributes

    print(r.url)        # prints requested url

def post_route_test():
    payload = { 'username' : 'antagonist', 'password' : 'testing' }      #payload data for POST req test

    r = requests.post('https://httpbin.org/post', data=payload)     # sending http quesries

    print(r.text)       # gives back json response

    r_dict = r.json()  # creates python dict from json dict

    print(r_dict['form'])

def basic_auth_test():

    r = requests.get('https://httpbin.org/basic-auth/antagonist/testing', auth=('antagonist', 'testing'))       # tests basic auth route for username: antagonst and password: testing

    wrng = requests.get('https://httpbin.org/basic-auth/antagonist/testing', auth=('wrong_credentials', 'wrong_password'))

    print(r.text)   # jSON response if authenticated, blank if wrong credentials

    print(wrng.text)        #blank

    print(wrng)     # unsuccessful response code (401)
    print(r)    # success (200)

def delay_test():

    r = requests.post('https://httpbin.org/delay/1', timeout=3)     # testing delay

    print(r)    # success code

    r = requests.post('https://httpbin.org/delay/6', timeout=3)     # testing delay, longer than timeout

    print(r)    # exception, ReadTimeout

    """ Requests waits indefinitely until website responds"""

get_route_test()
post_route_test()
basic_auth_test()
delay_test()

""" Remove the fuctions you do not want to test """