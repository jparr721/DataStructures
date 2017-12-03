#!/bin/gawk -f
BEGIN {n = 0}
/d/ {++n}
END {print n}
