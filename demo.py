from api.ai import Agent
import json


#initialize the agent 
agent = Agent(
     '<subscription-key>',
     '841d0b494b1c4abbb587f2bddacd87fc',
     '377275e794464e5cbe74eb66f8ca98b2',
)

# actions defined in the API.AI console that fire locally when an intent is
# recognized
def saveType(flowerType):
	print 'do something here'

def saveColor(color):
	print 'do something here'

def createOrder(address):
	print 'do something here'

def main():
	user_input = ''

	#loop the queries to API.AI so we can have a conversation client-side
	while user_input != 'exit':

		#parse the user input
		user_input  = raw_input("me: ")
		#query the console with the user input, retrieve the response
		response = agent.query(user_input)
		#parse the response
		result = response['result']
		fulfillment = result['fulfillment']

		print 'bot: ' + fulfillment['speech']

		#if an action is deteted, fire the appropriate function
		if result['action'] == 'saveFlowerType':
			saveType(user_input)
		elif result['action'] == 'saveColor':
			saveColor(user_input)
		elif result['action'] == 'createOrder':
			createOrder(user_input)
		else:
			pass

if __name__ == "__main__":
    main()
