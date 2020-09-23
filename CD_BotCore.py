'''
JACOB SCRAPCHANSKY, 2020 - Python Based Discord Modular Bot system. 
Some parts of the script are reminiscent of its old name, FangOS DE. Fang_Apps and Fang_Extensions likely will stay the same to maintain compatibility.
'''

#Seperate standard inputs, make threaded.
import os #Import Necessary modules
import getpass
import time
import discord
import asyncio
import threading
import access as npm
import sys




prints = []
inputs = []
ExcAnyinputs = []
ids = 0
thread_id = 0
threads = []

# Embed Messages
# Announce Function
# Startup Messages
# Status changing
# Storage Listings
# Thread Limiters
# push_to true command
# Fix Read_messages
# System path
# Message_Push
# Annouce
# Guild, Channel, And User Stores
# General Stores
# NSWF Channel detect
# Moderator detect
# Mutplie definable command callers
# Custom help command
# when new parent specified make files
# Admin Help
# Add Startup system
# Add add and remove authority
# clearlogs command
# clearmessages command
# ReadLogs Commands
# ReadMessages commands
# Revoke list commands from general users
# Multiple Args for print
# Active server lookup
# Blacklisting
# add null input detection on file creation
# add ask if wants to create file
# Add custom running commands
# - AnyInput()
# - ExclusiveInput()
# - ExclusiveAnyInput()

# sys.argv Replacement
# ARGS variable
# authority
# reinit commands
# Message_host filing
# - GetUserNameREF()
# - GetUserName()
# - GetIDbyName()
# - RoleExists()
# - GetRolebyID()
# - GetRolebyName()
# - GetNickbyName()
# - GetNickbyID()
# - GetUserNameFull()
# - MessageDM()
# - AUTHORITY
# Add notifier
# ID Based Authority
# CALLER_ID

# - RAW_IN


message_channel = None
message_guild = None

version = '0.1.8 Beta'
closer = False
client = discord.Client()




def init_sys(intake):
    global bot_setup
    global TOKEN
    global filer_path
    global back_serv_mess
    back_serv_mess = []
    bot_setup = npm.gain_info(intake)
    filer_path = bot_setup[1]
    bot_setup = bot_setup[0]
    TOKEN = bot_setup['token']

if len(sys.argv) > 1:
    initer = sys.argv[1]
else:
    initer = None
init_sys(initer)


async def background_tasks():
    global prints
    global inputs
    global message_channel
    global closer
    while 1:
        if closer:
            await client.logout()
            await client.close()
            break
        total_length_prints = 0
        for x in prints:
            total_length_prints += len(x[1])
        if not(total_length_prints == 0):

            passto = ''
            
            for message in prints:
                try:
                    passto = ''
                    for x in message[1]:
                        passto = passto + x
                    message[1] = []
                    message[1].append(passto)
                    needed_amount = round((len(message[1][0]) / 2000) + 0.5)
                    count_up = 0
                    for _ in range(needed_amount):
                        message[1].append(message[1][0][0 + count_up:2000 + count_up])
                        count_up += 2000
                    del message[1][0]
                    for send in range(len(message[1])):
                        await message[0].send(message[1][send])
                except Exception:
                    pass
            for x in range(len(prints)):
                prints[x][1] = []

        await asyncio.sleep(0.1)


def print(channel, string="", end='\n'):
    global prints
    channel_exists = False
    for x in range(len(prints)):
        if prints[x][0] == channel:
            channel_exists = True
    if not(channel_exists):
        prints.append([channel, []])
    for x in range(len(prints)):
        if prints[x][0] == channel:
            prints[x][1].append(str(string) + str(end))



def input(channel, string=''):
    try:
        global inputs
        print(channel, string.replace('>', '>') + ' (Awaiting Input, Respond by starting with ":" )')
        for x in range(len(inputs)):
            if inputs[x][0] == channel:
                inputs[x][2] = 'terminate_thread_quiet'
                inputs[x][4] = 'New thread in place.'
        inputs.append([channel, string, None, time.time(), None])
        quitter = 1
        while 1:
            for x in range(len(inputs)):
                try:
                    if inputs[x][0] == channel:
                        if inputs[x][3] + 120 < time.time():
                            inputs[x][2] = 'terminate_thread'
                            inputs[x][4] = 'Lack of response.'
                        if inputs[x][2] != None:
                            if inputs[x][2].strip() == 'terminate_thread':
                                print(channel, "Process Terminated: {}".format(inputs[x][4]))
                                del inputs[x]
                                quit()
                            if inputs[x][2].strip() == 'terminate_thread_quiet':
                                del inputs[x]
                                quit()
                            final = inputs[x][2]
                            del inputs[x]
                            return final
                except Exception:
                    break
    except Exception as exc:
        npm.nprint(str(exc))

def ExcAnyinput(name, user_id, channel, string=''):
    try:
        user_id = str(user_id)
        global ExcAnyinputs
        print(channel, string.replace('>', '/>') + 'Awaiting input from {}'.format(name))
        for x in range(len(ExcAnyinputs)):
            if ExcAnyinputs[x][0] == channel and ExcAnyinputs[5] == str(user_id):
                ExcAnyinputs[x][2] = 'terminate_thread_quiet'
                ExcAnyinputs[x][4] = 'New thread in place.'
        ExcAnyinputs.append([channel, string, None, time.time(), None, user_id])
        quitter = 1
        while 1:
            for x in range(len(ExcAnyinputs)):
                try:
                    if ExcAnyinputs[x][0] == channel:
                        if ExcAnyinputs[x][3] + 120 < time.time():
                            ExcAnyinputs[x][2] = 'terminate_thread'
                            ExcAnyinputs[x][4] = 'Lack of response.'
                        if ExcAnyinputs[x][2] != None:
                            if ExcAnyinputs[x][2].strip() == 'terminate_thread':
                                print(channel, "Process Terminated: {}".format(ExcAnyinputs[x][4]))
                                del ExcAnyinputs[x]
                                quit()
                            if ExcAnyinputs[x][2].strip() == 'terminate_thread_quiet':
                                del ExcAnyinputs[x]
                                quit()
                            final = ExcAnyinputs[x][2]
                            del ExcAnyinputs[x]
                            return final
                except Exception:
                    break
    except Exception as exc:
        npm.nprint(str(exc))


@client.event
async def on_error(event, *args, **kwargs):
    npm.nprint(args)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('{} help'.format(bot_setup['callsign'].strip())))

@client.event
async def on_message(message):
    global threads
    global thread_id
    global message_channel
    global message_guild
    global inputs
    global filer_path
    global back_serv_mess
    global ExcAnyinputs
    try:
        for thread in range(len(threads)):
            if "stopped" in threads[thread]['OBJECT']:
                del threads[thread]
        if message.content.strip().split()[0] == ':':
            if (str(message.channel).strip() == bot_setup['channel'].strip() or bot_setup['channel'].strip() == 'ALL'):
                for x in range(len(inputs)):
                    if inputs[x][0] == message.channel:
                        inputs[x][2] = message.content[2:]
                        inputs[x][4] = 'Forced Termination.'


        if len(ExcAnyinputs) != 0:
            if (str(message.channel).strip() == bot_setup['channel'].strip() or bot_setup['channel'].strip() == 'ALL'):
                for x in range(len(inputs)):
                    if inputs[x][0] == message.channel and inputs[x][5] == str(message.author.id):
                        inputs[x][2] = message.content
                        inputs[x][4] = 'Forced Termination.'


        if message.content.strip().split()[0] == bot_setup['callsign']:

            if str(message.channel).strip() == bot_setup['channel'].strip() or bot_setup['channel'].strip() == 'ALL':
                thread_id += 1
                try:
                    for x in range(len(back_serv_mess)):
                        if back_serv_mess[x][0] == str(message.guild).strip().replace("^", " "):
                            await message.channel.send(str(back_serv_mess[x][1]))
                            time.sleep(1)
                            del back_serv_mess[x]
                            break
                except Exception as exc:
                    npm.nprint("Error: " + str(exc) + " " + str(back_serv_mess))
                thread_holder = standard_inputs(message.content[len(bot_setup['callsign'].strip())+1:].encode('ascii', 'ignore').decode(), thread_id, message.guild, message.channel, message.author)
                try:
                    opened = open(filer_path + '/' + 'command_log.txt', 'a')
                    opened.write(str(time.ctime() + ", " + str(message.guild) + ", " + str(message.author) + ": " + message.content[len(bot_setup['callsign'].strip())+1:].encode('ascii', 'ignore').decode()).replace('-', '<dash>') + '-\n')
                    opened.close()
                except Exception as exc:
                    npm.nprint(str(exc))
                threads.append({'OBJECT':str(thread_holder), 'ID':thread_id, 'COMMAND':message.content})
                thread_holder.name = thread_id
                
            else:
                await message.channel.send("Please use the {} channel.".format(bot_setup['channel'].strip()))

        if message.content.strip().split()[0] == 'botcore_close':
            if (bot_setup['callsign'].strip() == message.content.strip().split()[1]) or ("ALL" == message.content.strip().split()[1]):
                
                if not(HasAuthority(str(message.author.id))):
                    print(message.channel, "You do not have the authority to use this command")
            
                if str(message.channel).strip() == bot_setup['channel'].strip() or bot_setup['channel'].strip() == 'ALL':
                    await client.close()
                    quit()
                
                else:
                    await message.channel.send("Please use the {} channel.".format(bot_setup['channel'].strip()))


        
    except Exception:
        pass



client.loop.create_task(background_tasks())

user = getpass.getuser() + '/' + bot_setup['parent_folder'] #Define necessary variables
presetv = []
preset = False
prompt_e = ''

fang_a_c = False #Search for Fang_Apps and Fang_Extensions and
fang_e_c = False #creates if does not exist
fang_store_e = False

parent_exists = os.path.isdir('/Users/' + user)

if not(parent_exists):
    os.mkdir('/Users/' + user)
for x in os.listdir("/Users/" + user):
    if x == 'Fang_Apps':
        fang_a_c = True
    if x == 'Fang_Extensions':
        fang_e_c = True
    if x == "Fang_Storage":
        fang_store_e = True
if fang_a_c == False:
    os.mkdir("/Users/" + user + "/Fang_Apps")
if fang_e_c == False:
    os.mkdir("/Users/" + user + "/Fang_Extensions")
if not(fang_store_e):
    os.mkdir("/Users/" + user + "/Fang_Storage")

store_guild_e = False
store_channel_e = False
store_user_e = False

for x in os.listdir("/Users/" + user + "/Fang_Storage"):
    if x == 'Guild_Store':
        store_guild_e = True
    if x == 'Channel_Store':
        store_channel_e = True
    if x == 'User_Store':
        store_user_e = True

if not(store_guild_e):
    os.mkdir("/Users/" + user + "/Fang_Storage/Guild_Store")
if not(store_channel_e):
    os.mkdir("/Users/" + user + "/Fang_Storage/Channel_Store")
if not(store_user_e):
    os.mkdir("/Users/" + user + "/Fang_Storage/User_Store")
    
for x in os.listdir("/Users/" + user + "/Fang_Extensions"): #remove Whitespace from names of all files in Apps/Extensions
    os.rename("/Users/" + user + "/Fang_Extensions/" + x, "/Users/" + \
              user + "/Fang_Extensions/" + x.replace(' ', ''))
for x in os.listdir("/Users/" + user + "/Fang_Apps"):
    os.rename("/Users/" + user + "/Fang_Apps/" + x, "/Users/" + \
              user + "/Fang_Apps/" + x.replace(' ', ''))


command_filer_exists = False

for x in os.listdir(filer_path):
    if x == 'command_log.txt':
        command_filer_exists = True
if not(command_filer_exists):
    opened = open(filer_path + '/' + 'command_log.txt', 'w')
    opened.close()

current_messages_exists = False
for x in os.listdir(filer_path):
    if x == 'current_messages.txt':
        current_messages_exists = True
if not(current_messages_exists):
    opened = open(filer_path + '/' + 'current_messages.txt', 'w')
    opened.close()

message_filer_exists = False
for x in os.listdir(filer_path):
    if x == 'message_log.txt':
        message_filer_exists = True
if not(message_filer_exists):
    opened = open(filer_path + '/' + 'message_log.txt', 'w')
    opened.close()
    



    

extensions = [] #List definitons for extensions
extension_n = []
extensions_a = []

def HasAuthority(user):
    global bot_setup
    user = str(user).strip()
    if user in bot_setup['authority']:
        return True
    else:
        return False
def reinit():
    global extensions
    global extensions_n
    global filer_path
    global bot_setup
    global TOKEN
    global user
    extensions = []
    extension_n = []
    extensions_a = []
    user = getpass.getuser() + '/' + bot_setup['parent_folder']
    for x in os.listdir("/Users/" + user + "/Fang_Extensions"): #Gather list of extensions
        if x[len(x)-4:] == "fext":
            extensions.append("/Users/" + user + "/Fang_Extensions/" + x)
            extension_n.append(x)

reinit()
def prompt(channel, text="Enter your command: ", line=True, prompt_text="> "): #Prompt Func.
    global inputs
    if line == True:
        print(channel, "-------------------")
    print(channel, text)
    returner = input(channel, prompt_text)

    return returner
    
take_in_val = None
class standard_inputs(threading.Thread):
    def __init__(self, take_in, id_, guild, channel, caller):
        global take_in_val
        global threads
        take_in_val = take_in
        self.guild = guild
        self.channel = channel
        self.channel_id = channel.id
        self.caller = str(caller)
        self.caller_id = caller.id
        self.guild_id = guild.id
        threading.Thread.__init__(self)
        self.start()


    def Guild_Store(self, Name, Content):
        global user
        access_folder = "Guild_Store"
        ID = self.guild_id
        if not(os.path.isdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)):
            os.mkdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)
        opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "w")
        opened.write(Content)
        opened.close()
    def Guild_Read(self, Name):
        global user
        ID = self.guild_id
        access_folder = "Guild_Store"
        if not(os.path.isfile("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name)):
            return None
        else:
            opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "r")
            returner = opened.read()
            opened.close()
            return returner

    def Channel_Store(self, Name, Content):
        global user
        access_folder = "Channel_Store"
        ID = self.channel_id
        if not(os.path.isdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)):
            os.mkdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)
        opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "w")
        opened.write(Content)
        opened.close()
    def Channel_Read(self, Name):
        global user
        ID = self.channel_id
        access_folder = "Channel_Store"
        if not(os.path.isfile("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name)):
            return None
        else:
            opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "r")
            returner = opened.read()
            opened.close()
            return returner

    def User_Store(self, Name, Content):
        global user
        access_folder = "User_Store"
        ID = self.caller_id
        if not(os.path.isdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)):
            os.mkdir("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + Name)
        opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "w")
        opened.write(Content)
        opened.close()
    def User_Read(self, Name, Content):
        global user
        ID = self.caller_id
        access_folder = "User_Store"
        if not(os.path.isfile("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name)):
            return None
        else:
            opened = open("/Users/" + user + "/Fang_Storage/" + access_folder + "/" + ID + "/" + Name, "r")
            returner = opened.read()
            opened.close()
            return returner


    def print(self, string="", end='\n'):
        print(self.channel, string, end)

    def UserExists(self, user):
        try:
            user_existance = self.guild.get_member(int(user.replace('<@!', '').replace('<@', '').replace('>', '')))
        except Exception:
            return False
        if user_existance == None:
            return False
        else:
            return user

    def ConsolePrint(self, string, end='\n'):
        npm.nprint(string, end)

    def input(self, string=''):
        global inputs
        returner = input(self.channel, string)

        return returner

    def ExclusiveAnyInput(self, name, user_id, string=''):
        try:
            user_existance = self.guild.get_member(int(user.replace('<@!', '').replace('<@', '').replace('>', '')))
        except Exception:
            return False
        if user_existance == None:
            return False
        else:
            returner = ExcAnyinput(name, str(user_id), self.channel, string)
            return returner

    def run(self): #Built in inputs
        global take_in_val
        global presetv #preset command globalize
        global preset
        global inputs
        global threads
        global version
        global back_serv_mess
        take_in = take_in_val
        
        commands = presetv + take_in.strip().split() #Make list of command/args


        
        if len(commands) == 0: #Detect if no input is specified
            self.print()
            self.print("No input detected")
            return None

        if commands[0] == 'search_logs':
            if not(HasAuthority(self.caller_id)):
                self.print("You do not have the authority to access this command")
                return commands[0]
            if len(commands) < 2:
                self.print("No lookup term Specified.")
                return commands[0]
            else:
                final = ''
                for x in commands[1:]:
                    final = final + ' ' + x
                final = final[1:]
                self.print("Searching commands for '{}'".format(final))
                opened = open(filer_path + '/command_log.txt', 'r')
                splitted = opened.read().split('-\n')
                give_back = ""
                logs_found = 0
                for x in splitted:
                    if final.lower() in x.lower():
                        give_back = give_back + "\n-------------\n" + x.replace('<dash>', '-')
                        logs_found += 1
                self.print("'{}' logs containing '{}' found.\n".format(logs_found, final))
                self.print(give_back)
        if commands[0] == 'message_server':
            if not(HasAuthority(self.caller_id)):
                self.print("You do not have the authority to access this command")
                return commands[0]
            if len(commands) < 2:
                self.print("No Server Name Specified.")
                return commands[0]
            if len(commands) < 3:
                self.print("No message given")
                return commands[0]
            else:
                final = ''
                for x in commands[2:]:
                    final = final + " " + x
                back_serv_mess.append([commands[1].replace("^", " "), final])
                self.print("Sent!")

        if commands[0] == 'read_messages':
            if not(HasAuthority(self.caller_id)):
                self.print('You don\'t have the permissions to access this command.')
                return commands[0]
            opened = open(filer_path + '/' + 'current_messages.txt', 'r')
            self.print("Messages: \n" + opened.read())
            opened.close()

        if commands[0] == 'clear_messages':
            if not(HasAuthority(self.caller_id)):
                self.print('You don\'t have the permissions to access this command.')
                return commands[0]
            opened = open(filer_path + '/' + 'current_messages.txt', 'r')
            old_text = opened.read()
            opened.close()
            opened = open(filer_path + '/' + 'current_messages.txt', 'w')
            opened.write("")
            opened.close()
            opened = open(filer_path + '/' + 'message_log.txt', 'a')
            opened.write("\n\n" + old_text)
            opened.close()
            self.print("Cleared to message logs.")

        if commands[0] == 'reinit':
            if not(HasAuthority(self.caller_id)):
                self.print("You do not have the authority to access this command")
                return commands[0]
            if len(commands) < 2:
                self.print("No File Name Specified.")
            else:
                init_sys(commands[1])
                reinit()
                self.print("Sucessfully reinitialized.")

        if commands[0] == 'list': #list command
            if len(commands) == 1:
                self.print()
                self.print("apps\nextensions")
                self.print()
                get_in = prompt(self.channel, "Input list", line=False)
                if get_in == "extensions":
                    self.print()
                    for x in extension_n:
                        self.print(x)
                    return commands[0]
                if get_in == "apps":
                    apps = []
                    for x in os.listdir("/Users/" + user + "/Fang_Apps"):
                        if x[len(x)-2:] == 'py':
                            apps.append(x)
                    self.print()
                    for x in apps:
                        self.print(x)
                    return commands[0]
                else:
                    self.print("Error while listing")
            if len(commands) >= 2:
                if commands[1] == "extensions":
                    self.print()
                    for x in extension_n:
                        self.print(x)
                    return commands[0]
                if commands[1] == "apps":
                    apps = []
                    for x in os.listdir("/Users/" + user + "/Fang_Apps"):
                        if x[len(x)-2:] == 'py':
                            apps.append(x)
                    self.print()
                    for x in apps:
                        self.print(x)
                    return commands[0]
                else:
                    self.print("Error while listing")

                    
        
        if commands[0] == 'help': #help command
            self.print('\n' + bot_setup['help'] + '\n\nPowered by CD BotCore v{}'.format(version))

        if commands[0] == 'debug': #help command
            if not(HasAuthority(self.caller_id)):
                self.print("You do not have the permissions to access this command")
                return commands[0]
            self.print(inputs)
            self.print(threads)
            self.print(threading.enumerate())




        
        if commands[0] == "math": #Calculation


            if len(commands) == 1:
                try:
                    self.print()
                    equation = prompt(self.channel, "Enter problem", False)
                    if len(equation) > 20:
                        self.print("Sorry, equations over the length of 20 are not allowed because of Nolan.")
                        return commands[0]
                    self.print(eval(equation))
                except Exception as exc:
                    self.print("Error While computing problem: " + str(exc))
            if len(commands) == 2:
                try:
                    if len(commands[1]) > 20:
                        self.print("Sorry, equations over the length of 20 are not allowed because of Nolan.")
                        return commands[0]
                    self.print(eval(commands[1]))
                except Exception:
                    self.print("error while computing problem")
            elif len(commands) >= 3:
                self.print("Extra argument detected")
            return commands[0]





        if commands[0] == "message_host":
            if len(commands) < 2:
                self.print('Please supply a message to send!')
                return commands[0]
            else:
                final = self.caller + ':'
                for x in commands[1:]:
                    final += " " + x.encode('ascii', 'replace').decode()
                opened = open(filer_path + '/' + 'current_messages.txt', 'a')
                opened.write(time.ctime() + ", " + str(self.guild) + ", " + final)
                opened.close()
                self.print('Sent!')
                return commands[0]


        if commands[0] == 'load': #Load Program


            files = []
            self.print()
            if len(commands) == 1:            
                self.print("Scanning for available apps...")
                self.print()
                time.sleep(0.5)
                for file in os.listdir("/Users/" + user + "/Fang_Apps"):
                    if file[len(file)-2:] == "py":
                        files.append(file)

                if len(files) == 0:
                    self.print("No Files Available")
                    return commands[0]

                
                
                for x in files:
                    self.print(x[:len(x)-3])
                self.print()
                file_name = prompt(self.channel, "Input the name of the file from the list above", False)
                if len(file_name) == 0:
                    self.print("Error while opening program. ")
                    return commands[0]
                self.print()
                self.print("Loading " + file_name + "...")
                self.print()
                time.sleep(0.5)
                for x in files:
                    if file_name + ".py" == x:
                       try:
                            opened = open("/Users/" + user + "/Fang_Apps/" + file_name + ".py", 'r')
                            contents = opened.read()
                            opened.close()
                            exec(contents, {'VERSION':version, 'CALLER':self.caller, 'GUILD':self.guild, 'CHANNEL':self.channel, 'print':self.print, 'input':self.input})
                       except Exception as exc:
                           self.print("Error while opening program: {}".format(str(exc)))
            elif len(commands) == 2:
                self.print()
                self.print("Loading " + commands[1] + "...")
                self.print()
                try: 
                    opened = open("/Users/" + user + "/Fang_Apps/" + commands[1] + ".py", 'r')
                    contents = opened.read()
                    opened.close()
                    exec(contents, {'VERSION':version, 'CALLER':self.caller, 'GUILD':self.guild, 'CHANNEL':self.channel, 'print':self.print, 'input':self.input })
                except Exception as exc:
                    self.print("Error while opening program: {}".format(str(exc)))
                
            else:
                self.print("Extra argument detected")
            return commands[0]


        
        if commands[0] != "clear_messages" and commands[0] != "read_messages" and commands[0] != "search_logs" and commands[0] != "message_server" and commands[0] != "reinit" and commands[0] != "message_host" and commands[0] != "debug" and commands[0] != "load" and commands[0] != "math" and commands[0] != "help" and commands[0] != "list":


             for x in extensions:
                 opened = open(x, 'r')
                 opened_l = str(opened.read()).strip().split()
                 opened.close()
                 if opened_l[0] == "'''" + commands[0] + "'''":
                     passto = ''
                     for y in range(len(commands) - 1):
                         passto = passto + " " + commands[y + 1]
                         
                     opened = open(x, 'r')
                     contents = opened.read()
                     opened.close()
                     try:
                        exec(contents, {'Guild_Read':self.Guild_Read, 'Guild_Store':self.Guild_Store, 'ExclusiveAnyInput':self.ExclusiveAnyInput, 'ConsolePrint':self.ConsolePrint, 'CALLER_ID':self.caller_id, 'HasAuthority':HasAuthority, 'UserExists': self.UserExists, 'VERSION':version, 'REF_CALLER':'<@!' + str(self.caller_id) + '>','CALLER':self.caller, 'GUILD':str(self.guild), 'CHANNEL':self.channel, 'print':self.print, 'input':self.input, 'argv':['python3'] + passto.strip().split(), 'sys.argv':['python3'] + passto.strip().split()})
                     except Exception as exc:
                        self.print('Extension Error: ' + str(exc))
                     return commands[0]

                 
             self.print("Command not found: " + str(take_in))

client.run(TOKEN)

