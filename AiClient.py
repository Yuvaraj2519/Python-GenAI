from openai import AzureOpenAI
from dotenv import load_dotenv
import os


def getresponse (prompt):

        load_dotenv()
        
        api_version = os.environ['API_VERSION']
        api_key = os.environ['API_KEY']
        azure_endpoint = os.environ['AZURE_ENDPOINT']
        azure_deployment = os.environ['AZURE_DEPLOYMENT']
        client = AzureOpenAI(
                api_version=api_version,
                api_key=api_key,
                azure_endpoint=azure_endpoint,
                azure_deployment=azure_deployment
        )
        prompt = prompt
        chat_completion = client.chat.completions.create (
        messages=[
                {
                        "role": "user",
                        "content": prompt,
                        }
                ], model="apt-3,5-turbo",
        )
        # print (os.environ ['API_VERSION])
        # print (chat_completion.id)
        for choice in chat_completion.choices:
           return choice.message.content

query = input("Al client: how can i help you/nUser:")
print ("AI Client: "+getresponse (query))
