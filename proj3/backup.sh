#!/bin/bash
#Ask for admin password
sudo -v

target="" # Default to an empty target


while getopts ":lnh" opt; do
	case "${opt}" in
		l)
			echo "Listing files in .backup:" 1>&2
			ls -al ../proj2
			;;
		n)
			echo "There are `ls -1 | wc -l` files that take up `du -k ~/.backup | awk '{print $1"kb"}'` of space in .backup"
			;;
		h)
			echo "BACKUP(1)		Extended Command Manual		BACKUP(1)"
			echo "-n	Show the number of files in .backup and how much space they take up"
			echo "-l	List files currently in -l"
			;;
		\?)
			echo "Usage: cmd [-l] [-n] [--help]"
			# fak off m8
			exit 1
			;;

	esac
done
shift $((OPTIND -1))
