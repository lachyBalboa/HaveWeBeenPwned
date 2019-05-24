
import requests as res
import json
# insert emails here
## TODO add command-line support
def haveWeBeenPwned(us:list):
        '''Pass in a list of email addresses to query. '''

        for email in us:
                response = res.get("https://haveibeenpwned.com/api/v2/breachedaccount/{account}".format(account=email))
                if response.text:
                        print("Email Pwned : {0}".format(email))
                        output = json.loads(response.text)
                        breachDate = output[0]["BreachDate"]
                        breachName = output[0]["Name"]
                        breachDomain = output[0]["Domain"]
                        print("Name: {0}".format(breachName))
                        print("Domain: {0}".format(breachDomain))
                        print("Breach Date: {0}".format(breachDate))
                        print()
                print("{0} has not been seen in any breaches".format(me))

def haveIBeenPwned(me:str):
        ''' Query a single email address'''
        #TODO add verbose mode support etc. Limit information without it
        response = res.get("https://haveibeenpwned.com/api/v2/breachedaccount/{account}".format(account=me))

        if response.text:
                output = json.loads(response.text)
                print("Email Pwned : {0} {1} times".format(me, len(output)))
                print("Here are the details \n")
                for breachData in output:
                        breachDate = breachData["BreachDate"]
                        breachName = breachData["Name"]
                        breachDomain = breachData["Domain"]
                        print("Name: {0}".format(breachName))
                        print("Domain: {0}".format(breachDomain))
                        print("Breach Date: {0}".format(breachDate))
                        print()
                
                #print(response.text)
        else:
                # Response empty = not pwned
                print("{0} has not been seen in any breaches".format(me))

#TODO Add password API Support