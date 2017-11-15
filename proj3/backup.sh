#!/bin/bash

if [ -z "$1" ]
then
	echo "The usage of this program is: backup [options] targetFileList"
	exit 1
fi
if [[ -d $2 || -f $2 ]]; then
	for input in "$@"
	do
		if [[ -d $input || -f $input ]]; then
			let file1 = $input
			if [[ -n $file1 ]]; then
				let file2 = $input
			fi
					if [[ -n file2 ]]; then
						let file3 = $input
					fi
		elif [[ $input = *'-'* ]]; then
			continue
		fi
	done
fi

function clean() {
	echo "Cleaning old .backup files"
	rm -rf ~/.backup
}

function backup_files() {
		clean
		echo "Making .backup..."
		mkdir ~/.backup
		cp -R `pwd`/{$1,$2,$3} ~/.backup
}

backup_files $file1 $file2 $file3

while getopts ":lnh" opt; do
	case "${opt}" in
		l)
			printf "Listing files in .backup:\n\n"
			ls -al ~/.backup | awk '{print $9}'
			;;
		n)
			printf "There are `ls -1 | wc -l` files that take up `du -skh ~/.backup | awk '{print $1"b"}'` of space in .backup\n\n"
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
