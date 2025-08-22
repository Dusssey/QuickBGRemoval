A super lighteweight and quick discord bot that can be locally hosted for quick background removals. Can set up in less than 30 mins.

1. Go to Discord Developers Page and Create a Application.
2. Name it whatever you like, then head to Bot Tab, Enable Message Intents.
3. Go to Oauth tab, and select "Bot" and "applications.commands" for your Scopes.
4. For Bot Permissions, hit Administrator for easy install.
5. Copy the generated link at the bottom of the Permissions Bot, and thats your install link.
6. Head back to the Bot Tab, and Reset your Bot Token for a Clean Token. Store it somewhere safe.
7. Go to remove.bg/api and create an account and follow the steps to get your own API Key.
8. Once you have your Bot Token and API Key, clone the repository.
9. Open up config.json.example, REMOVE the .example so the file is just named config.json
10. In the file, put your bot token where it is outlined, and do the same with your API Key
11. In your IDE, open everything up in a venv, and run bot.py
12. Commands are !removebg (attatchment), or !removebg (URL) without parenthesis.
