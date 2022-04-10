# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pomodoro_procedure.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/10 15:00:48 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 16:53:51 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from timer_printer import TimerPrinter
from timer_alerts import *
import sys, time

def pomodoro(_minutes, _color, _seconds):
	minutes = _minutes
	seconds = _seconds
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

def pomodoroNormalTimer():
	pomodoro(TimerPrinter.minutes, TimerPrinter.BlueColor, TimerPrinter.seconds)
	sys.stdout.write("\n\n")
	printAlert()

def pomodoroBreakTimer():
	pomodoro(TimerPrinter.breakMinutes, TimerPrinter.GreenColor, TimerPrinter.breakSeconds)
	sys.stdout.write("\n\n")
	printAlert()

def pomodoroProcedure():
	input("\nPress ENTER to start...")
	for n in range(10, 0, -1): # Limit of 10 for protection
		pomodoroNormalTimer()
		alertMessage("\nPress ENTER to start your break...")
		pomodoroBreakTimer()
		alertMessage("\nPress ENTER to focus...")
