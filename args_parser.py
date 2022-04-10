# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    args_parser.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 14:27:37 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 17:06:17 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from timer_printer import TimerPrinter
import argparse

def parseArgs():
	parser = argparse.ArgumentParser(prog='Shell Pomodoro', description='A pomodoro timer for your shell')
	parser.add_argument('-w', '--custom_work', nargs=2,  type=int, metavar=('minutes', 'seconds'), help='Set a custom WORK time to your pomodoro')
	parser.add_argument('-b', '--custom_break', nargs=2,  type=int, metavar=('minutes', 'seconds'), help='Set a custom BREAK time to your pomodoro')
	parser.add_argument('-e', '--extended', help='Extended time. 50 work minutes and 10 break minutes. Incompatible with custom times.', action='store_true')
	timer_args = parser.parse_args()
	if (timer_args.custom_work != None):
		TimerPrinter.minutes = timer_args.custom_work[0]
		TimerPrinter.seconds = timer_args.custom_work[1]
	if (timer_args.custom_break != None):
		TimerPrinter.breakMinutes = timer_args.custom_break[0]
		TimerPrinter.breakSeconds = timer_args.custom_break[1]
	if (timer_args.custom_work == None and timer_args.custom_break == None and timer_args.extended == True):
		TimerPrinter.minutes = 49
		TimerPrinter.breakMinutes = 10
	return 0
