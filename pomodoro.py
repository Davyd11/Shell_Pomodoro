# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pomodoro.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <javgonza@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/14 12:36:13 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 14:19:49 by javgonza         ###   ########.fr        #
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
from timer_printer import TimerPrinter

def inputChecker():
	
	if len(sys.argv) > 1:
		if (sys.argv[1] == "-e"):
			TimerPrinter.minutes = 49
			TimerPrinter.breakMinutes = 10
		elif (sys.argv[1] == "-c"):
		      return parseCustomTime()
		else:
			print ( TimerPrinter.RedColor + "\nYour argument is not well written\nFor a extended pomodoro use the argument [ -e ]\n" + TimerPrinter.ResetColor)
			return 1
	return 0
	
#def splitNumbers(_number): # Split numbers into to diferent ints for better aplication
#	
#	if _number <= 9:
#		number1 = 0;
#		number2 = _number;
#	else:
#		number1 = int(str(_number)[0]);
#		number2 = int(str(_number)[1]);
#	return(number1, number2)

def parseCustomTime():
	if len(sys.argv) != 4:
		print ( TimerPrinter.RedColor + "\nYour argument is not well written\nFor custom pomodoro use:\n\tpomodoro -c <minutes> <seconds>\nExample:\n\tpomodoro -c 35 12" + TimerPrinter.ResetColor)
		return 1
	else:
		TimerPrinter.minutes = int(sys.argv[2])
		TimerPrinter.seconds = int(sys.argv[3])
		return 0

def pomodoro(_minutes, _color):
	minutes = _minutes
	seconds = TimerPrinter.seconds
	for remaining in range(60 * minutes + seconds, 0, -1):
		TimerPrinter.print(minutes, seconds, _color)
		if seconds > 0:
			seconds -= 1
		else:
			if minutes <= 0:
				return 0
			minutes -= 1
			seconds = 59
		time.sleep(1)

def printAlert():
	
	os.system('clear')
	for n in range(0, 5, +1):
		sys.stdout.write("{:2s}\n".format( TimerPrinter.YellowColor + TimerPrinter.Alert[n]))
	sys.stdout.write("{:2s}\n\n".format( TimerPrinter.Alert[n + 1]) + TimerPrinter.ResetColor)
	if "LC_TERMINAL" in os.environ:
		if os.environ["LC_TERMINAL"] == "iTerm2":
			sys.stdout.write("\33]9;Pomodoro has finished\7")

def alertMessage(_message):
	while (input(_message) == " "):
		os.system('echo -e "\a"')
		time.sleep(0.5)
	return(0)

def pomodoroProcedure():
	input("\nPress ENTER to start...")
	for n in range(10, 0, -1): # Limit of 10 for protection
		pomodoro(TimerPrinter.minutes, TimerPrinter.BlueColor)
		sys.stdout.write("\n\n")
		printAlert()
		alertMessage("\nPress ENTER to start your break...")
		pomodoro(TimerPrinter.breakMinutes, TimerPrinter.GreenColor)
		sys.stdout.write("\n\n")
		printAlert()
		alertMessage("\nPress ENTER to focus...")
	

if __name__ == "__main__":
	try:
		if inputChecker() == 0:
			pomodoroProcedure()
		raise KeyboardInterrupt
	except KeyboardInterrupt:
#		os.system('clear')
		print(TimerPrinter.BlueColor + "\nSee you later. Bye\n" + TimerPrinter.ResetColor)
