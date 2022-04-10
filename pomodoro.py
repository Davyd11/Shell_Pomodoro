# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pomodoro.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: javgonza <javgonza@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/14 12:36:13 by javgonza          #+#    #+#              #
#    Updated: 2022/04/10 15:15:57 by javgonza         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3

from timer_printer import TimerPrinter
from args_parser import parseArgs
from pomodoro_procedure import pomodoroProcedure

if __name__ == "__main__":
	try:
		if parseArgs() == 0:
			pomodoroProcedure()
		raise KeyboardInterrupt
	except KeyboardInterrupt:
		print(TimerPrinter.BlueColor + "\nSee you later. Bye\n" + TimerPrinter.ResetColor)
