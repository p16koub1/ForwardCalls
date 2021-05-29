import os
from twilio.rest import Client


def create_call(address, number):
    #Visit Twilio Console to get these:
    acount_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(acount_sid, auth_token)
    call = client.calls.create(
        url = address,
        to = number,
        from_= 'twilio_provided_number'
    )

#Call number based on white/black list
def call_numbers(phone_numbers, whitelist, blacklist):
    for phone in phone_numbers:
        if phone in whitelist:
            create_call('yourwebhookerprovider//whitelist', phone)

        elif phone in blacklist:
            create_call('yourwebhookerprovider//blacklist', phone)
            
        else:
            phone_numbers = open('./phone_numbers.txt', 'w').writelines(phone)


#Whitelist location:
whitelist = open('/whitelist.txt', 'r').readlines()
#Blacklist location:
blacklist = open('/blacklist.txt', 'r').readlines()
#Numbers location:
phone_numbers = open('/phone_numbers.txt', 'r').readlines()
call_numbers(phone_numbers, whitelist, blacklist)



        



    

