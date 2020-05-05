from telegram import User
from telegram.ext import Updater
import urllib
updater=Updater(token='1227962721:AAEIJ41_MdJjL-xg4pMXv5ljqvt-KsOGtNw', use_context=True)
dispatcher=updater.dispatcher

def start(context, update):
    bot.send_message(User.first_name,text="Hello "+User.first_name+" I am CrowdProduct's Event Handling Bot, which day's events would you like to look at ?"+'\n'+"Or enter the date accordingly for that day's events, or 'all' for all the events.")
    
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

#part 2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

creds = ServiceAccountCredentials.from_json_keyfile_name('insert file here', scope)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] #different URLs
client = gspread.authorize(creds)

#all events
sheet = client.open('name').sheet1
pp = pprint.PrettyPrinter()
events = sheet.get_all_records()
pp.pprint(events)

#specific to the date
date=String(input("Enter the date in a DD and Month format:")
i=1
if date in sheet.col_value(3):
            i++
for x in range(0,i+1):
            pp.pprint(sheet.row_values(x))