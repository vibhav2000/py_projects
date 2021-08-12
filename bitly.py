import bitly_api   
BITLY_ACCESS_TOKEN ="dc5b6de2e41db4799a5f5d129130304d6de05597"
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

full_link = input()
short_url = access.shorten(full_link)
print('Shorted URL = ',short_url['url'])
