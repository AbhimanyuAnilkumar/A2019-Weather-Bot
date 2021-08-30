import requests
def bot_deploy():
    url = "http://automate.kloudpad.in/v1/authentication"

 

    payload="{\r\n  \"username\": \"rpa1@cloudsys.co.in\",\r\n  \"password\": \"Delta123#RPA1@\" \r\n}\r\n\r\n//Note: Token is automatically extracted and saved to a variable everytime this call is made...see the Tests tab for more details\r\n//https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-authenticate-password.html"
    headers = {
      'Content-Type': 'application/json'
    }

 

    response = requests.request("POST", url, headers=headers, data=payload)

 

    cr_token=response.json().get("token")

 

    url = "http://automate.kloudpad.in/v3/automations/deploy"

 

    payload="//https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-bot-deploy-task.html\r\n{\r\n  \"fileId\":14767, //id of the bot to execute\r\n  \"runAsUserIds\": [\r\n    36 //id(s) of the user account to run the bot - must have default device unless specified below\r\n  ],\r\n  \"poolIds\": [],\r\n  \"overrideDefaultDevice\": false,\r\n  \"callbackInfo\": {\r\n    \"url\": \"https://callbackserver.com/storeBotExecutionStatus\", //Callback URL - not required, but can be used - can be removed if no callback needed\r\n    \"headers\": {\r\n      \"X-Authorization\": cr_token\"\" //Callback API headers. Headers may contain authentication token, content type etc. Both key & value are of type string.\r\n    }\r\n  },\r\n  \"botInput\": { //optional values to map to the bot...NOTE: These values must match the exact variable names and must be defined as input values\r\n    \"sInput1\": {\r\n      \"type\": \"STRING\", //Type can be [ STRING, NUMBER, BOOLEAN, LIST, DICTIONARY, DATETIME ]\r\n      \"string\": \"cloudsys\" //key must match type, in this case string\r\n    },\r\n    \"sInput2\": {\r\n      \"type\": \"STRING\",\r\n      \"string\": \"hello world\"\r\n    }\r\n  }\r\n}"
    headers = {
      'Content-Type': 'application/json',
      'X-Authorization': cr_token
    }

 

    response = requests.request("POST", url, headers=headers, data=payload)
    a= dict(response.json())
    a=next(iter(a))
    print (a)
    if a == 'deploymentId':
        return ("Bot successfully executed pleasse check the result in VM")
 
