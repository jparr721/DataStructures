#!/bin/bash
#Ask for admin password
sudo -v

if [ -z "$1" ]
then
	echo "The usage of this program is: backup [options] targetFileList"
	exit 1
fi

if [[ $1 != *'-'* ]]; then
	file1=$1
	file2=$2
	file3=$3
else
	file1=$2
	file2=$3
	file3=$4
fi

function backup_files() {
	if [[ -z `ls -a | grep .backup` ]]; then
		echo "Making .backup..."
		mkdir ~/.backup
		cp -R `pwd`/{$1,$2,$3} ~/.backup
	else
		rm -rf ~/.backup
		mkdir ~/.backup
		cp -R `pwd`/{$1,$2,$3} ~/.backup
	fi
}

backup_files $file1 $file2 $file3

while getopts ":lnh" opt; do
	case "${opt}" in
		l)
			printf "Listing files in .backup:\n\n"
			ls -al ../proj2
			;;
		n)
			printf "There are `ls -1 | wc -l` files that take up `du -k ~/.backup | awk '{print $1"kb"}'` of space in .backup\n\n"
			;;
		h)
			printf "\n\n"
			echo "BACKUP(1)		Extended Command Manual		BACKUP(1)"
			echo "-n	Show the number of files in .backup and how much space they take up"
			echo "-l	List files currently in -l"
			echo "-h	Show help page"
			;;
		\?)
			printf "backup: Invalid option: $1\n\n"
			# fak off m8
			exit 1
			;;

	esac
done
shift $((OPTIND -1))
