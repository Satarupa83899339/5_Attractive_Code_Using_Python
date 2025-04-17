#Link Shortener
import pyshorteners

#get the link from the user
link = input("Enter the link:")

#create a shortener object
shortener = pyshorteners.Shortener()

#shorten the link using TinyURL
shortened_link = shortener.tinyurl.short(link)
#print the shortened link
print("Shortened Link:", shortened_link)
