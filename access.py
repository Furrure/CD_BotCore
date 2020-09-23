import sys
import os
path = sys.path[0]
def gain_info(intake):
	if intake == None:
		spath = input('Please Specify Setup Folder Name: \n> ').strip()
		setup_file_path = path + '/' + spath
	else:
		setup_file_path = path + '/' + intake
		spath = intake
	if not(spath in os.listdir(path)):
		print('"{}" not found, creating folder...'.format(spath))
		os.mkdir(path + '/' + spath)
	if not('callsign.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/callsign.dfi', 'w')
		opened.write('bot')
		opened.close()
	if not('channel.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/channel.dfi', 'w')
		opened.write('ALL')
		opened.close()
	if not('help.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/help.dfi', 'w')
		opened.write('The Developer has not yet included any help intructions.')
		opened.close()
	if not('parent_folder.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/parent_folder.dfi', 'w')
		opened.write('')
		opened.close()
	if not('token.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/token.dfi', 'w')
		opened.write('')
		opened.close()
	if not('authority.dfi' in os.listdir(setup_file_path)):
		opened = open(setup_file_path + '/authority.dfi', 'w')
		opened.write('')
		opened.close()

	opened = open(setup_file_path + '/callsign.dfi', 'r')
	callsign = opened.read().strip()
	if callsign == '':
		print("No callsign specified.")
		quit()
	opened.close()

	opened = open(setup_file_path + '/channel.dfi', 'r')
	channel = opened.read().strip()
	if channel == "":
		print("No channel specified.")
		quit()
	opened.close()

	opened = open(setup_file_path + '/help.dfi', 'r')
	help_info = opened.read().strip()
	if help_info == "":
		help_info = "No help provided."
	opened.close()

	opened = open(setup_file_path + '/parent_folder.dfi', 'r')
	parent_folder = opened.read().strip()
	if parent_folder == "":
		print("No parent folder specified.")
		quit()
	opened.close()

	opened = open(setup_file_path + '/token.dfi', 'r')
	token = opened.read().strip()
	if token == "":
		print("No token specified.")
		quit()
	opened.close()

	opened = open(setup_file_path + '/authority.dfi', 'r')
	authority = opened.read().strip().split('\n')
	opened.close()

	return [{'callsign':callsign, 'channel':channel, 'help':help_info, 'parent_folder':parent_folder, 'token':token, 'authority':authority}, setup_file_path]


	
def nprint(string, end='\n'):
	print(string, end)
def ninput(string):
	return input(string)

