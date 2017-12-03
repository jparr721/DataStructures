#!/bin/gawk -f
BEGIN {
print "directories  files  links  total  storage(bytes)"
print "================================================"
} 
{n = 0}
/-/ {++n}
END {print n}

