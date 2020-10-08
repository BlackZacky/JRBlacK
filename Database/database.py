from collections import namedtuple
from pymongo import MongoClient
from datetime import datetime

from Database import MONGOURL, BOTID

import discord

class check:
    """
    Value: Boolean
    return: True or False
    """
    def __init__(self, client=False):
        self.coll = MongoClient(MONGOURL, retryWrites=False)["jrblack"]
        self.client = client

    def guild(self, GuildID:int):
        for x in self.coll["guilds"].find({"GuildID": GuildID}):
            return True
        return False

    def user(self, GuildID:int, MemberID:int):
        for x in self.coll["users"].find({"GuildID": GuildID, "MemberID": MemberID}):
            return True
        return False

    def bot(self, GuildID:int, BotID:int):
        for x in self.coll["bot"].find({"GuildID": GuildID, "BotID": BotID}):
            return True
        return False

class guild:
    """
    return guild info in database(MongoDB)
    """
    def __init__(self, client=False):
        self.coll   = MongoClient(MONGOURL, retryWrites=False)["jrblack"]["guilds"]
        self.tuple  = namedtuple("database_guild", ["status", "text"])
        self.check  = check()
        self.client = client

    def create(self, GuildID:int, GuildOW:int):
        if self.check.guild(GuildID):
            return self.tuple(False, 0)

        json = {"GuildID":     GuildID, 
                "GuildOW":     GuildOW,
                "Config":{
                    "Prefix": ".",
                    "BackgroundW": "False"},
                "ChannelID":{
                    "ChannelNews":       0,
                    "ChannelLogs":       0,
                    "ChannelLogsBan":    0,
                    "ChannelLottery":    0,
                    "ChannelCounter":    0,
                    "ChannelWelcome":    0,
                    "ChannelHardDisk":   0,
                    "ChannelHardDisk2":  0,
                    "ChannelHardDisk3":  0,
                    "ChannelWhitelist":  0,
                    "ChannelSuggestion": 0},
                "RoleID":{
                    "AutoRole":          0,
                    "MuteRole":          0},
                "System":{
                    "XpLevel":"False",
                    "Economy":"False"},
                    "GuildDate": datetime.utcnow()}

        return self.tuple(True, self.coll.insert(json))

    def delete(self, GuildID:int):
        if self.check.guild(GuildID):
            return self.tuple(True, self.coll.delete({"GuildID": GuildID}))

        return self.tuple(False, False)

    def post_logs(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelLogs': ChannelID}})

    def post_auto_react(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelSuggestion': ChannelID}})

    def post_harddisk(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelHardDisk': ChannelID}})

    def post_harddisk_2(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelHardDisk2': ChannelID}})

    def post_harddisk_3(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelHardDisk3': ChannelID}})

    def post_welcome(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelWelcome': ChannelID}})

    def post_counter(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelCounter': ChannelID}})

    def post_news(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelNews': ChannelID}})

    def post_lottery(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelLottery': ChannelID}})

    def post_auto_role(self, GuildID:int, RoleID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'RoleID.AutoRole': RoleID}})

    def post_mute_role(self, GuildID:int, RoleID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'RoleID.MuteRole': RoleID}})

    def post_system_xp_level(self, GuildID:int):
        if ([x['System']['XpLevel'] for x in self.coll.find({'GuildID':GuildID})])[0] == "True":
            return self.tuple(False, self.coll.update_one({'GuildID': GuildID}, {'$set':{'System.XpLevel': 'False'}}))

        return self.tuple(True, self.coll.update_one({'GuildID': GuildID}, {'$set':{'System.XpLevel': 'True'}}))

    def post_system_economy(self, GuildID:int):
        if ([x['System']['Economy'] for x in self.coll.find({'GuildID':GuildID})])[0] == "True":
            return self.tuple(False, self.coll.update_one({'GuildID': GuildID}, {'$set':{'System.Economy': 'False'}}))

        return self.tuple(True, self.coll.update_one({'GuildID': GuildID}, {'$set':{'System.Economy': 'True'}}))

    def post_whitelist(self, GuildID:int, ChannelID:int):
        return self.coll.update_one({'GuildID': GuildID}, {'$set':{'ChannelID.ChannelWhitelist': ChannelID}})

    def get_logs(self, GuildID:int):
        return ([x['ChannelID']['ChannelLogs'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_auto_react(self, GuildID:int):
        return ([x['ChannelID']['ChannelSuggestion'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_harddisk(self, GuildID:int):
        return ([x['ChannelID']['ChannelHardDisk'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_harddisk_2(self, GuildID:int):
        return ([x['ChannelID']['ChannelHardDisk2'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_harddisk_3(self, GuildID:int):
        return ([x['ChannelID']['ChannelHardDisk3'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_welcome(self, GuildID:int):
        return ([x['ChannelID']['ChannelWelcome'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_counter(self, GuildID:int):
       return ([x['ChannelID']['ChannelCounter'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_news(self, GuildID:int):
        return ([x['ChannelID']['ChannelNews'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_lottery(self, GuildID:int):
        return ([x['ChannelID']['ChannelLottery'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_auto_role(self, GuildID:int):
        return ([x['RoleID']['AutoRole'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_mute_role(self, GuildID:int):
        return ([x['RoleID']['MuteRole'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_system_xp_level(self, GuildID:int):
        return ([x['System']['XpLevel'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_system_economy(self, GuildID:int):
        return ([x['System']['Economy'] for x in self.coll.find({'GuildID':GuildID})])[0]

    def get_whitelist(self, GuildID:int):
        return ([x['ChannelID']['ChannelWhitelist'] for x in self.coll.find({'GuildID':GuildID})])[0]

class user:
    """
    return user info in database(MongoDB)
    """
    def __init__(self, client=False):
        self.coll   = MongoClient(MONGOURL, retryWrites=False)['jrblack']['users']
        self.tuple  = namedtuple("database_user", ["status", "text"]) 
        self.check  = check()
        self.client = client

    def create(self, GuildID:int, MemberID:int):
        if self.check.user(GuildID, MemberID):
            return self.tuple(False, 0)

        json = {"GuildID":        GuildID,
                "MemberID":       MemberID,
                "Messages":       0,
                "Report":         0,
                "Job":            "False",
                "Background":     "False",
                "Social":{
                    "Facebook":   "False",
                    "Youtube":    "False",
                    "Github":     "False",
                    "Instagram":  "False",
                    "TikTok":     "False",
                    "Twitter":    "False",
                    "Telegram":   "False"},
                "Bank":{
                    "Number":     0,
                    "MoneyHand":  0,
                    "MoneyBank":  0},
                "XpLevel":{
                    "Level":      0,
                    "Xp":         0},
                "Inventory":{
                    "Background": [],
                    "Weapon":     [],
                    "CreditCard": 0},
                "About":          "Sem descrição.",
                "Command":{
                    "Name": "False",
                    "Datetime": "False",
                },
        }

        return self.tuple(True, self.coll.insert(json))

    def delete(self, GuildID:int, MemberID:int):
        if self.check.guild(GuildID):
            return self.tuple(True, self.coll.delete({"GuildID": GuildID, "MemberID": MemberID}))
        return self.tuple(False, 0)

    def post_report(self, GuildID:int, MemberID:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"Report": 1}})

    def post_messages(self, GuildID:int, MemberID:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"Messages": 1}})

    def post_about(self, GuildID:int, MemberID:int, About:str):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$set":{"About": About}})

    def post_money_bank(self, GuildID:int, MemberID:int, Money:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"Bank.MoneyBank": Money}})

    def post_money_hand(self, GuildID:int, MemberID:int, Money:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"Bank.MoneyHand": Money}})

    def post_level(self, GuildID:int, MemberID:int):
        if ([x["XpLevel"]["Level"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0] < int(([x["XpLevel"]["Xp"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0] ** (1/4)):
            return self.tuple(True, self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"XpLevel.Level": 1}}))
        return self.tuple(False, False)

    def post_xp(self, GuildID:int, MemberID:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"XpLevel.Xp": 2}})

    def post_background(self, GuildID:int, MemberID:int, Url:str):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$set":{"Background": Url}})

    def post_inventory_background(self, GuildID:int, MemberID:int, Url:str):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$push":{"Inventory.Background": Url}})

    def post_inventory_weapon(self, GuildID:int, MemberID:int, Weapon:str):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$push":{"Inventory.Weapon": Weapon}})

    def post_credit_card(self, GuildID:int, MemberID:int, CardNumber:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$inc":{"Inventory.CreditCard": CardNumber}})

    def post_job(self, GuildID:int, MemberID:int, Job:int):
        return self.coll.update_one({"GuildID": GuildID, "MemberID": MemberID}, {"$set":{"Job": Job}})

    def get_report(self, GuildID:int, MemberID:int):
        return ([x["Report"] for x in self.coll.find({'GuildID':GuildID, "MemberID": MemberID})])[0]

    def get_messages(self, GuildID:int, MemberID:int):
        return ([x["Messages"] for x in self.coll.find({'GuildID':GuildID, "MemberID": MemberID})])[0]

    def get_about(self, GuildID:int, MemberID:int):
        return ([x["About"] for x in self.coll.find({'GuildID':GuildID, "MemberID": MemberID})])[0]

    def get_money_bank(self, GuildID:int, MemberID:int):
        return ([x["Bank"]["MoneyBank"] for x in self.coll.find({'GuildID':GuildID, "MemberID": MemberID})])[0]

    def get_money_hand(self, GuildID:int, MemberID:int):
        return ([x["Bank"]["MoneyHand"] for x in self.coll.find({'GuildID':GuildID, "MemberID": MemberID})])[0]

    def get_bank_rank(self, GuildID:int, MemberID:int):
        Rank = []
        Count = 0
        for i in self.coll.find({"GuildID":GuildID}).sort('Bank.MoneyBank', -1).limit(10):
            Count += 1
            Rank.append(f"**{Count}º ➜** <@{i['MemberID']}> - **${i['Bank']['MoneyBank']}**")

        return "\n\n".join(Rank)

    def get_level(self, GuildID:int, MemberID:int):
        return ([x["XpLevel"]["Level"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0]

    def get_xp(self, GuildID:int, MemberID:int):
        return ([x["XpLevel"]["Xp"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0]

    def get_background(self, GuildID:int, MemberID:int):
        return ([x["Background"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0]

    def get_inventory_background(self, GuildID:int, MemberID:int):
        return ([x["Inventory"]["Background"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0]

    def get_inventory_weapon(self, GuildID:int, MemberID:int):
        return ([x["Inventory"]["Weapon"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])[0]

    def get_credit_card(self, GuildID:int, MemberID:int):
        return ([x["Inventory"]["CreditCard"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])

    def get_job(self, GuildID:int, MemberID:int):
        return ([x["Job"] for x in self.coll.find({"GuildID":GuildID, "MemberID":MemberID})])

class bot:
    def __init__(self):
        self.coll  = MongoClient(MONGOURL, retryWrites=False)["jrblack"]["bot"]
        self.tuple = namedtuple("database_bot", ["status", "text"])
        self.check = check()

    def create(self, GuildID:int, BotID:int):
        if self.check.bot(GuildID, BotID):
            return False

        json = {"GuildID": GuildID,
                "BotID": BotID,
                "Lottery":{
                    "Money":5000},
                "Casanik":{
                  "Money": 10000}}

        self.coll.insert(json)
        return True

    def delete(self, GuildID:int):
        if not self.check.guild(GuildID):
            return False
        
        return self.coll.delete({"GuildID": GuildID})

    def post_casanik(self, GuildID:int, BotID:int, Money:int):
        return self.coll.update_one({"GuildID": GuildID, "BotID": BotID}, {"$inc":{"Casanik.Money": Money}})

    def get_casanik(self, GuildID:int, BotID:int):
        return ([x["Casanik"]["Money"] for x in self.coll.find({"GuildID":GuildID, "BotID":BotID})])[0]

print("Database: Conectado!")