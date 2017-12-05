#!/bin/gawk -f
BEGIN {FS=":"
print "user_name    password    uid    gid   full_name    home    shell"
print "================================================================="	
}
{OFS="\t"}
{
}
{
print $1"  "$2"  "$3"  "$4"  "$5"  "$6"  "$7
}
END {
print "Next available uid:"$3+1
print "Next available gid:"$3+1
}
