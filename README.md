# DiscordBot_template
This is a simple discordbot template wich has few things built into it allready.

# Setup
Put your discord bot's token into ```config.py``` and run ```DiscordBot.py``` to start the bot up.

# Autosave
Bot has autosave feature built in. You can use ```self.servers``` variable as storage. This should be dictionary. 

Bot saves data from this variable to ```data.json``` file every 30 seconds by default. To change the autosave frequency change variable ```self.autosave_frequency``` in init. 

If bot is unable to load data from ```data.json``` it will set ```self.servers``` eaqual to empty dictionary and dissable autosave by turning flag ```self.autosave``` to false. 

This is because if ```self.servers``` is not defined the bot wont start at all. Auto save is dissabled for safety reasons that your ```data.json``` wont be overridden with empty dictioanry.

# Autosave Functions
- ```saveData()``` saves data from ```self.servers``` to ```data.json```
- ```loadData()``` loads data from ```data.json``` to ```self.servers```
- ```doSave()``` this is a function that runs in loop and runs ```saveData()``` every x seconds defined by ```self.autosave_frequency```
