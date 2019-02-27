import requests as req

r = req.get('https://imgs.xkcd.com/comics/python.png')
# grab an image (comic) from a website

print(r)    # gets response object (code: 200)
print(dir(r))       # gets attributes and methods of response object
#help(r) gives a more detailed explanation

print(r.text)       #gives content in unicode (html for that page)
#to parse, use html parser

"""print(r.content)"""    
    #prints the bytes of the image

with open('comic.png', 'wb') as f:
    f.write(r.content)      #downloads the bytes of that image

print(r.status_code)    #prints HTTP status code

print(r.ok)     # prints true for good response

print(r.headers)        # prints headers (info)






