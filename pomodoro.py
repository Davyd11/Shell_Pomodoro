# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pomodoro.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dpuente- <dpuente-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/14 12:36:13 by dpuente-          #+#    #+#              #
#    Updated: 2022/02/23 10:50:19 by dpuente-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
#█░▄▄░█▀░██░▄░█░▄▄░██░▄░██░▄▄█▀▄▄▀█▄▄▄░█▀▄▄▀█▀▄▄▀
#█░▀▄░██░███▀▄███▄▀█░▀▀░▀█▄▄▀█░▀▀████░██▀▄▄▀█▄▀▀░
#█░▀▀░█▀░▀█░▀▀█░▀▀░████░██▀▀▄█▄▀▀▄██▌▐██▄▀▀▄██▀▀▄
#▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ all numbers needed for the ascii timer

import secrets
from socketserver import DatagramRequestHandler
import time, sys, os

class Data:
	
	#TODO: future implementation for a second timer with the current time
	#seconds = time.time()
	#CurentTime = time.ctime(seconds)
	
	#############################
	# Ascii numbers and symbols #
	#############################

	NumberArray = [["▄▄▄▄▄","█░▄▄░", "█░▀▄░", "█░▀▀░", "▀▀▀▀▀"],				#0
					["▄▄▄▄", "█▀░█", "██░█", "█▀░▀", "▀▀▀▀"],					#1
					["▄▄▄▄", "█░▄░", "██▀▄", "█░▀▀", "▀▀▀▀"],					#2
					["▄▄▄▄▄","█░▄▄░", "███▄▀", "█░▀▀░", "▀▀▀▀▀","▄▄▄▄▄▄"],		#3
					["▄▄▄▄▄▄","██░▄░█","█░▀▀░▀","████░█","▀▀▀▀▀▀"],				#4
					["▄▄▄▄","█░▄▄","█▄▄▀","█▀▀▄","▀▀▀▀"],						#5
					["▄▄▄▄▄","█▀▄▄▀","█░▀▀█","█▄▀▀▄","▀▀▀▀▀"],					#6
					["▄▄▄▄▄","█▄▄▄░","███░█","██▌▐█","▀▀▀▀▀"],					#7
					["▄▄▄▄▄","█▀▄▄▀","█▀▄▄▀","█▄▀▀▄","▀▀▀▀▀"],					#8
					["▄▄▄▄▄","█▀▄▄▀","█▄▀▀░","██▀▀▄","▀▀▀▀▀"]]					#9

	Alert = 	["██╗     █████╗ ██╗     ███████╗██████╗ ████████╗    ██╗",
				"██║    ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝    ██║",
				"██║    ███████║██║     █████╗  ██████╔╝   ██║       ██║",
				"╚═╝    ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║       ╚═╝",
				"██╗    ██║  ██║███████╗███████╗██║  ██║   ██║       ██╗",
				"╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═╝"]
	CharTimer = [["▄▄", "█▀", "██", "█▄", "▀▀"], ["▄", "█", "█", "█", "▀"]] # : and extra spaces

	#################################
	# Minutes and seconds by default#
	#################################
	
	minutes = 24
	breakMinutes = 4
	seconds = 59

	##########################
	# Colors for text output #
	##########################
	
	GreenColor = "\033[0;32m"
	BlueColor = "\033[0;34m"
	YellowColor = "\033[1;33m"
	RedColor = "\033[0;31m"
	ResetColor = "\033[0m"


def inputChecker():
	
	if len(sys.argv) == 2:
		if (sys.argv[1] == "-e"):
			Data.minutes = 49
			Data.breakMinutes = 9
		elif len(sys.argv) != 1:
			print ( Data.RedColor + "\nYour argument is not well written\nFor a extended pomodoro use the argument [ -e ]\n" + Data.ResetColor)
			return 1
	return 0
	
def SplitNumbers(_number): # Split numbers into to diferent ints for better aplication
	
	if _number <= 9:
		number1 = 0;
		number2 = _number;
	else:
		number1 = int(str(_number)[0]);
		number2 = int(str(_number)[1]);
	return(number1, number2)

def printTimer(_minutes, _seconds, _color):
	
	minute1, minute2 = SplitNumbers(_minutes);
	second1, second2 = SplitNumbers(_seconds);
	
	os.system('clear')
	for n in range(0, 5, +1):
		stringTime = ( _color + Data.NumberArray[minute1][n] + Data.NumberArray[minute2][n] + Data.CharTimer[0][n] + Data.NumberArray[second1][n] +  Data.NumberArray[second2][n] +  Data.CharTimer[1][n])
		sys.stdout.write("{:2s}\n".format(stringTime))

def pomodoro(_minutes, _color):

	minutes = _minutes
	seconds = Data.seconds
	for remaining in range(60 * minutes, 0, -1):
		printTimer(minutes, seconds, _color)
		if seconds > 0:
			seconds -= 1
		else:
			if minutes <= 0:
				return 0
			minutes -= 1
			seconds = 59
		time.sleep(1)

def PrintAlert():
	
	os.system('clear')
	for n in range(0, 5, +1):
		sys.stdout.write("{:2s}\n".format( Data.YellowColor + Data.Alert[n]))
	sys.stdout.write("{:2s}\n\n".format( Data.Alert[n + 1]) + Data.ResetColor)

def alertMessage(_mesage):
	while (input(_mesage) == " "):
		os.system('echo -e "\a"')
		time.sleep(0.5)
	return(0);

def pomodoroProcedure():
	input("\nPress ENTER to start...")
	for n in range(10, 0, -1): # Limit of 10 for protection
		pomodoro(Data.minutes, Data.BlueColor)
		sys.stdout.write("\n\n")
		PrintAlert()
		alertMessage("\nPress ENTER to start your break...")
		pomodoro(Data.breakMinutes, Data.GreenColor)
		sys.stdout.write("\n\n")
		PrintAlert()
		alertMessage("\nPress ENTER to focus...")
	

if __name__ == "__main__":
	if inputChecker() == 0:
		pomodoroProcedure()
