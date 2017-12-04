#!/bin/gawk -f
BEGIN {FS=":"
print "user_name    password    uid    gid   full_name    home    shell"
print "================================================================="	
}
{OFS="\t"}
{
}
END {
print $1,$2,$3,$4,$5,$6,$7
}
