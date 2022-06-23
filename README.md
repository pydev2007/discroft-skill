# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/rss.svg" card_color="#7289da" width="50" height="50" style="vertical-align:bottom"/> Discroft
Simple mycroft discord bot.

## About
This skill allows Mycroft and Discord to communicate with each other! Use `!send <your command>` to send a command to Mycroft! This works anywhere with the discord app/website!

## Credits
Gavin Thompson

## Category
**IoT**

## Tags
#Discord
#Portable

## Get Started

First, you need to create an application. You can do this in the [Discord Developer Portal](https://discord.com/developers/applications). Click "New Application" and give your app a name. 

![Mycroft_gif_1](https://user-images.githubusercontent.com/80983612/173093969-2fa17a71-08dd-4e80-bfbb-192541044637.gif)

Next, create the bot. Go to the bot tab and click "add bot". Feel free to give your bot a name and profile picture!

![Mycroft_gif_2](https://user-images.githubusercontent.com/80983612/173107659-be569159-5fb0-4f81-942a-50d53888ce37.gif)

Now, you need to invite your bot to your server. Click on "OAuth2" then click "URL Generator". Select "bot" in scopes, then copy the link below. (the bot doesn't need permissions because it only takes commands.) Now paste the link into your browser, and select the desired server. Keep in mind you need a server to invite the bot into.

![Mycroft_gif_3](https://user-images.githubusercontent.com/80983612/173152605-382618ab-e057-482f-a7b7-c19cb45ed759.gif)

For the bot to work you need to paste your token into the Mycroft configuration. Click "Reset token" in the "Bot" tab. From here you can copy your token and paste in the config.

![Mycroft_gif_4](https://user-images.githubusercontent.com/80983612/173153515-41870e60-fa8f-4e57-b6fd-795d8b8262d5.gif)

Last, you need to set up your webhook. The Webhook allows requests to be forwarded from mycroft to Discord. 
In your server, click the settings button on the channel you would Mycroft messages to appear. Now click "Integrations" and "Webhooks", from here you can create a new Webhook and copy the URL. Paste the URL into the Mycroft config. Before you reboot, the configuration needs to be updated. You can either wait a few minutes for it to auto-update, or tell mycroft to "Update configuration". If the configuration isn't updated you may need to reboot once more.

![Mycroft_gif_5](https://user-images.githubusercontent.com/80983612/173154814-360c7d0e-1625-4a0d-83d9-eaee49b5a784.gif)

The bot should go online once initialized! 
