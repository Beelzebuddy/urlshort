import pyshorteners

link = input('Enter a link: ')

shortner = pyshorteners.shortner()

x = shortner.tinyurl.short(link)