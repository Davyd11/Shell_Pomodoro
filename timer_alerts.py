# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    timer_alerts.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 15:04:55 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 15:06:06 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from timer_printer import TimerPrinter
import sys, os, time

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
