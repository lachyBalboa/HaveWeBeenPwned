
import requests as res
import json
# insert emails here
emails = [

]

for email in emails:
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
