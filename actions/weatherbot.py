import requests
import time
import json
from collections import namedtuple
from json import JSONEncoder
def CityWeather():
    url = "http://automate.kloudpad.in/v1/authentication"

    payload="{\r\n  \"username\": \"rpa1@cloudsys.co.in\",\r\n  \"password\": \"Delta123#RPA1@\" \r\n}\r\n\r\n//Note: Token is automatically extracted and saved to a variable everytime this call is made...see the Tests tab for more details\r\n//https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-authenticate-password.html"
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    cr_token=response.json().get("token")
    return (cr_token)

def CityTemp(input1):
    cr_token=CityWeather()
 #   print(cr_token)
    url = "http://automate.kloudpad.in/v3/automations/deploy"
    #input1 = "New York" #location
    payload="//https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-bot-deploy-task.html\r\n{\r\n  \"fileId\":14920, //id of the bot to execute\r\n  \"runAsUserIds\": [\r\n    36 //id(s) of the user account to run the bot - must have default device unless specified below\r\n  ],\r\n  \"poolIds\": [],\r\n  \"overrideDefaultDevice\": false,\r\n  \"callbackInfo\": {\r\n    \"url\": \"https://callbackserver.com/storeBotExecutionStatus\", //Callback URL - not required, but can be used - can be removed if no callback needed\r\n    \"headers\": {\r\n      \"X-Authorization\": \"eyJhbGciOiJSUzUxMiJ9.eyJzdWIiOiIzNiIsImNsaWVudFR5cGUiOiJXRUIiLCJsaWNlbnNlcyI6WyJSVU5USU1FIl0sImFuYWx5dGljc0xpY2Vuc2VzUHVyY2hhc2VkIjp7IkFuYWx5dGljc0NsaWVudCI6dHJ1ZX0sInRlbmFudFV1aWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiLCJoeWJyaWRUZW5hbnQiOiIiLCJpYXQiOjE2MDY4NDcxMzYsImV4cCI6MTYwNjg0ODMzNiwiaXNzIjoiQXV0b21hdGlvbkFueXdoZXJlIiwibmFub1RpbWUiOjE3MzE0MzY5MzMzNjUyMDB9.UM8mE7etUtwmuITMnMfHArIMfF9tCGKcPWQRK2_vhml7uZUZhO1XIa2AQ91wLziHLBTHikkvy5n0_v5gx4bMKv0suNmAfgyHyIHlVoYhKQyQe7mErAcQxpz0g6s723lAbS4C5M-EpzHekWnxlxa5DCA6Fmejfg5-VMTJuYjekUFKfu0XoZt0SQkOSiznWXI-ppSmvP2KjIC9SUTvzFeL5tHflKtiI7aa0VK77DoCg8E48rABAMPtixzengF5IyIp7XmiF-tElUAvRPGdr8kr3yldzP0uM5T4Nm5pUnktCSiCG891YqSKrifEPSOyxMisX4TKZW8JykJSfKdabXqa5A\" //Callback API headers. Headers may contain authentication token, content type etc. Both key & value are of type string.\r\n    }\r\n  },\r\n  \"botInput\": { //optional values to map to the bot...NOTE: These values must match the exact variable names and must be defined as input values\r\n    \"vApiKey\": {\r\n      \"type\": \"STRING\", //Type can be [ STRING, NUMBER, BOOLEAN, LIST, DICTIONARY, DATETIME ]\r\n      \"string\": \"51c162bc479d6ff7fb9f6fea8f6f0951\" //key must match type, in this case string\r\n    },\r\n    \"vCity\": {\r\n      \"type\": \"STRING\",\r\n      \"string\": \""+input1+"\"\r\n    }\r\n  } \r\n   \r\n}"
    headers = {
      'Content-Type': 'application/json',
      'X-Authorization': cr_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json().get('deploymentId'))
    deploy_id = response.json().get('deploymentId')
    time.sleep(25)
    url = "http://automate.kloudpad.in/v2/activity/list"

    payload="//https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-bot-deploy-task.html\r\n{\r\n  \"filter\": {\r\n    \"operator\": \"eq\",\r\n    \"field\": \"deploymentId\",\r\n    \"value\": \""+deploy_id+"\"\r\n  }\r\n}"
    headers = {
      'Content-Type': 'application/json',
      'X-Authorization': cr_token
    }
   
    response = requests.request("POST", url, headers=headers, data=payload)
    dataresponse= response.json()
   

   
    resp_dict = json.dumps(dataresponse)
   
    resp_dicts = json.loads(resp_dict)
    #print(resp_dict)

   # print(strs[170]) # "ns1:timeSeriesResponseType"

    botsoutput = resp_dicts['list']
   
   
    for s in range(len(botsoutput)):
#for s in range(len(students)):
        return("The bot status {} and output {}.".format(botsoutput[s]["status"], botsoutput[s]["botOutVariables"]["values"]["sOutput"]["string"]))
             
#CityTemp("New York")


