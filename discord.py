from discord_webhook import DiscordWebhook
from rich import print
import time
import keyboard
import sys

value = False
webhookLink = "webhook link here"

def Webhook():
    print("Type your message:")
    text = input()
    webhook = DiscordWebhook(url = webhookLink, content = text)
    webhook.execute()
    print("[green]Successfully sent a message.")

def Off():
    global value 
    value = True

keyboard.add_hotkey("num 9", Webhook)
keyboard.add_hotkey("end", Off)

while True:
    time.sleep(1)
    if value == True:
        print("Exiting program...")
        sys.exit(0)