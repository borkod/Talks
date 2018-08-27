import datetime
from dateutil.parser import parse

def lambda_handler(event, context):
   # get the current intent
    intent_name = event['currentIntent']['name']
    
    # Dispatch to your bot's intent handlers
    if intent_name == 'LunchMenuItem':
        return get_menu_handler(event)
        
# Event Handler for get menu intent.
def get_menu_handler(event):
    # get date
    date = event['currentIntent']['slots']['Day']
    
    # get the day of week from the date
    day_of_week = parse(date).weekday()
    
    # get the menu item for the meal and day of week
    menu_item = get_menu_item(day_of_week)
    
    return create_response(event, menu_item)      

# Returns the menu item for a specific meal and day of week
def get_menu_item(day_of_week):
    # menu is represented as a dictinary
    menu = ['salad', 'pizza', 'pasta', 'soup', 'hamburger', 'sushi', 'pizza']
        
    return menu[day_of_week]

# Generates a valid response for AWS Lex
def create_response(event, menu_item):
    return {
        'sessionAttributes': event['sessionAttributes'],
        'dialogAction':{
            'type':'Close',
            'fulfillmentState': 'Fulfilled',
            'message':{
                'contentType':'PlainText',
                'content':menu_item
            }
        }
    }

