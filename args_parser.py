# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    args_parser.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:27:37 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 14:33:19 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parseArgs():
	
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
	
def parseCustomTime():
	if len(sys.argv) != 4:
		print ( TimerPrinter.RedColor + "\nYour argument is not well written\nFor custom pomodoro use:\n\tpomodoro -c <minutes> <seconds>\nExample:\n\tpomodoro -c 35 12" + TimerPrinter.ResetColor)
		return 1
	else:
		TimerPrinter.minutes = int(sys.argv[2])
		TimerPrinter.seconds = int(sys.argv[3])
		return 0
