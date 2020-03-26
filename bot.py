from flask import Flask,request
import requests
import time
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    # first question that the user prompts
    if 'hi' in incoming_msg:
        quote = 'How are you feeling right now?\n1. really happy\n2. content\n3. okay'
        msg.body(quote)
        responded=True
    elif 'hello' in incoming_msg:
        quote = 'How are you feeling right now?\n1. really happy\n2. content\n3. okay'
        msg.body(quote)
        responded=True
    elif 'hey' in incoming_msg:
        quote = 'How are you feeling right now?\n1. really happy\n2. content\n3. okay'
        msg.body(quote)
        responded=True
    if '1' in incoming_msg:
        answer = 'that\'s great I don\'t know what more I can do for you!'
        msg.body(answer)
        responded=True
    elif '2' in incoming_msg:
        answer = 'Life is great, appreciate the moments'
        msg.body(answer)
        responded=True
    elif '3' in incoming_msg:
        answer= 'Woah I don\'t what could possibly be wrong, you seem fine'
        msg.body(answer)
        responded=True
    
    # time.sleep(5)
    # msg.body('I\'m wondering if this is something you wanted help with or did you want to get it off your chest?')
    # if 'help' in incoming_msg:
    #     answer = 'I will try to do my best'
    #     msg.body(answer)
    #     responded=True
    # elif 'off' in incoming_msg:
    #     answer = 'I am here with you and fully support you'
    #     msg.body(answer)
    #     responded=True
    # if '4' in incoming_msg:
    #     quote='Aren\'t we all feeling the same way with the quarantine going on right now?'
    #     msg.body(quote)
    #     responded=True
    # if '5' in incoming_msg:
    #     quote='Don\'t worry we are here to help and get you feeling better'
    #     msg.body(quote)
    #     responded=True
    if not responded:
        msg.body('Sorry I can only offer self-help advice, if you want cooking tips jamie oliver is a better guide')
    return str(resp)

if __name__ == '__main__':
    app.run()
    

