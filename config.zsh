# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.zsh                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dpuente- <dpuente-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/16 16:45:34 by dpuente-          #+#    #+#              #
#    Updated: 2022/02/16 17:45:26 by dpuente-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#! /bin/bash

if [ ! "command -v python3" ] ; then # python3 is not installed
		echo '\nSomething went wrong\nPlease install python3\n'
else
	mkdir -p ~/Utils/pomodoro/
	cp -r -n . ~/Utils/pomodoro/
	alias pomodoro="python3 ~/Utils/pomodoro/pomodoro.py"
fi