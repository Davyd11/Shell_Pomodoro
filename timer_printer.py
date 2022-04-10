
import time, sys, os

class TimerPrinter:
	
	#TODO: future implementation for a second timer with the current time
	
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
	def print(_minutes, _seconds, _color):
		minute1, minute2 = splitNumbers(_minutes);
		second1, second2 = splitNumbers(_seconds);
	
		os.system('clear')
		for n in range(0, 5, +1):
		        stringTime = ( _color + TimerPrinter.NumberArray[minute1][n] + TimerPrinter.NumberArray[minute2][n] + TimerPrinter.CharTimer[0][n] + TimerPrinter.NumberArray[second1][n] +  TimerPrinter.NumberArray[second2][n] +  TimerPrinter.CharTimer[1][n])
		        sys.stdout.write("{:2s}\n".format(stringTime))

def splitNumbers(_number): # Split numbers into to diferent ints for better aplication
	
	if _number <= 9:
		number1 = 0;
		number2 = _number;
	else:
		number1 = int(str(_number)[0]);
		number2 = int(str(_number)[1]);
	return(number1, number2)

