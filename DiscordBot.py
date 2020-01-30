import glob, os
import discord
import asyncio
import json
import random
'''
Bot's other files...
'''
from config import *


class MyClient(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.prefix = "!m "
		self.servers = {}
		self.badwords = []
		self.botimage = "http://via.placeholder.com/350x350" #### Image for embeds
		self.autosave = True
		self.autosave_frequency = 30 #### How many seconds between autosaves.



	#### Task that runs save every 30sec ####
	async def doSave(self,):
		await self.wait_until_ready()
		while not self.is_closed():
			if self.autosave == True:
				await self.saveData()
			await asyncio.sleep(self.autosave_frequency)

	#### Saves data from self.servers to data.json ####
	async def saveData(self,):
		print("Saving started!")
		tempdata = self.servers
		with open('data.json', 'w') as fpp:
			json.dump(tempdata, fpp, sort_keys=True, indent=4)

		fpp.close()
		print("Saving done!")

	#### Loads data from data.json and saves it to self.servers ####
	async def loadData(self):
		try:
			print("Loading started!")
			data = {}
			with open('data.json', 'r') as fp:
				data = json.load(fp)
			self.servers = data
			fp.close()
			print("Loading done!")

		except:
			#### If bot fails to load data.json make self.servers an empty dictionary to avoid crashes also disable autosave that all data is not lost in autosave.
			print("[#### WARNING ####]: Bot was unable to load data from storage.")
			self.autosave = False
			self.servers = {}


	async def on_ready(self): #### This runs when bot is ready to go.
		await self.loadData()
        
        #### Makes function doSave() run every x seconds saving all data from self.servers to data.json
		self.saveLoop = self.loop.create_task(self.doSave())
		print(discord.__version__)
		print('Logged on as {0}!'.format(self.user))


	async def on_message(self, message):
		#### Checks if message has wanted prefix so its detected to be a command ####
		if message.content.startswith(self.prefix):
            command = message.content.strip(self.prefix+" ")

			if command == "test":
				print(self.servers)
				await channel.send("It seems that the test was successfull.")

			if command == "save":
				await self.saveData()
				await channel.send("Saving done!")

			if command == "load":
				await self.loadData()
				await channel.send("Loading done!")


client = MyClient()
client.run(botkey)