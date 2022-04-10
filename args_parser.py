# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    args_parser.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:27:37 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 16:37:37 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from timer_printer import TimerPrinter
import argparse

def parseArgs():
	parser = argparse.ArgumentParser(prog='Shell Pomodoro', description='A pomodoro timer for your shell')
	parser.add_argument('-c', '--custom_time', nargs=2,  type=int, metavar=('minutes', 'seconds'), help='Add a custom time to your pomodoro')
	parser.add_argument('-e', '--extended', help='Extended time. 50 minutes and 10 break minutes. Incompatible with --custom_time.', action='store_true')
	timer_args = parser.parse_args()
	if (timer_args.custom_time != None):
		TimerPrinter.minutes = timer_args.custom_time[0]
		TimerPrinter.seconds = timer_args.custom_time[1]
	elif (timer_args.extended == True):
		TimerPrinter.minutes = 49
		TimerPrinter.breakMinutes = 49
