from pyshorteners import Shortener
ACCESS_TOKEN = 'dc5b6de2e41db4799a5f5d129130304d6de05597'

#shorten LOOOOONG URL
long_url = input()
url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN)
print("Short URL is {}".format(url_shortener.short(long_url)))

#Expand short URL
short_url = input()
url_expander = Shortener('Bitly', bitly_token = ACCESS_TOKEN)
print ("Long URL is {}".format(url_expander.expand(short_url)))