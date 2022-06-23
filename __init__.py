# Copyright 2022 Gavin Thompson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from mycroft import MycroftSkill, intent_file_handler
from mycroft_bus_client import MessageBusClient, Message
from mycroft.util.log import LOG
import asyncio
from threading import Thread
import requests
from websocket import create_connection
from discord.ext import commands 
from discord import Webhook, RequestsWebhookAdapter

class discroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        TOKEN = self.settings.get("Token")
        self.URL = self.settings.get("Url")

        self.discord_bot(TOKEN)


        try:
            webtest = requests.get(self.URL)
            if webtest.status_code == 200:
                self.client = MessageBusClient()
                self.client.on('speak', self.sndmsg) 
                self.client.run_in_thread()
        
            else:
                LOG.error("Invalid URL please make sure the URL and the token is valid")
                
        except:
            LOG.error("Could not connect to the URL")




    def discord_bot(self, TOKEN):
        # Commands and starting the bot
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop) 
        bot = commands.Bot(command_prefix="!")

        @bot.event
        async def on_ready():
            LOG.info(f'{bot.user.name} has connected to Discord!')
            
        @bot.command(name='send', help='Sends command to mycroft')
        async def command(ctx, *, commands):
            self.bus.emit(Message('recognizer_loop:utterance',{"utterances": [commands],"lang": self.lang}))

        self.loop = asyncio.get_event_loop()
        self.loop.create_task(bot.start(TOKEN))
        Thread(target=self.loop.run_forever).start()

    def sndmsg(self, message):
        # Sends messages through the webhook when Mycroft speaks
        self.DiscordHook = Webhook.from_url(self.URL, adapter=RequestsWebhookAdapter()) 
        data = message.data.get("utterance")  
        self.DiscordHook.send(data) 
        LOG.info("Sending message to Discord")

def create_skill():
    return discroft()