#!/bin/bash
regex="^-."
args=""
ARGUMENTS=()
FILES=()

function clean() {
	echo "Cleaning old .backup files"
	rm -rf ~/.backup
}

function backup_files() {
		clean
		echo "Making .backup..."
		mkdir ~/.backup
		cp -R ${FILES[@]} ~/.backup
}

for input in "$@"
do
	if [[ $input =~ $regex ]];
	then
		#Arguments
		ARGUMENTS+=$input
	else
		#Files
		FILES+="`pwd`/$input "
	fi
done
if [[ ${#FILES[@]} -eq 0 ]]; then
	echo "No files, bitch"
else
	backup_files ${FILES[@]}
fi



while getopts ":lnh" opt; do
	case "${opt}" in
		l)
			printf "Listing files in .backup:\n"
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
