#password generater
#by Cooper Mahring
import random
import string
import os
readwrite = raw_input("Do you want to read or write a file? (r/w) :  ")
if readwrite == "w":
	website = raw_input("What website url do you want to save this for? :  ")
	username = raw_input("what username is this associated with? :  ")
	raw_input("If there is a password already saved for this website and username, it will be overwritten. Click enter to continue.")
	passlength = raw_input("Password Length:  ")
	numbers = raw_input("Do you want numbers? (y/n):  ")
	letters = raw_input("Do you want letters? (y/n):  ")
	capitals = raw_input("Do you want some capital letters? (y/n):  ")
	specials = raw_input("Do you want special characters? (y/n):  ")
	specialchars = ['`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','\\','/','?',';',':','\'','\"',',']
	password = ""
	while len(password) < int(passlength):
		rand = random.randrange(0,3,1)
		randnum = 0
		if rand == 0 and numbers == "y":
			randnum = random.randrange(0,10,1)
			password = password + str(randnum)
		if rand == 1 and letters == "y":
			randnum = random.randrange(0,2,1)
			randstring = random.choice(string.letters)
			if capitals == "y" and randnum == 1:
				randstring = randstring.upper()
			password = password + randstring
		if rand == 2 and specials == "y":
			password = password + random.choice(specialchars)
	if not os.path.exists("/opt/passwordgen"):
		os.chdir("/opt")
		os.mkdir("passwordgen")
	if not os.path.exists("/opt/passwordgen/"+website):
		os.chdir("/opt/passwordgen")
		os.mkdir(website)
	os.chdir("/opt/passwordgen/"+website)
	fo = open(username+".txt", "w+")
	position = fo.tell()
	fo.write(  "Website:   " + website)
	fo.write("\nUsername:  " + username)
	fo.write("\nPassword:  " + password)
	position = fo.seek(0,0)
	print fo.tell()
	print fo.read(100000)
if readwrite == "r":
	website = raw_input("What website? :  ")
	username = raw_input("What username? :  ")
	if os.path.exists("/opt/passwordgen/"+website):
		if os.path.isfile("/opt/passwordgen/"+website+"/"+username+".txt"):
			fo = open("/opt/passwordgen/"+website+"/"+username+".txt")
			print "********************************************"
			print fo.read(100000)
			print "********************************************"
		else:
			print "It doesn\'t seem like you have that username with that website stored on this computer"
	else:
		print "It doesn\'t seem like you have that website stored on this computer"
else:
	print "you didn\'t put either r or w in... Goodbye"