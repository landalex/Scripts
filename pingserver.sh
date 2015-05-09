#!/bin/bash

SERVER="alexland.ca"

/sbin/ping -c 1 $SERVER >/Users/AlexLand/Scripts/ping.out 2>&1
if [ $? -ne 0 ] ; then #if ping exits nonzero...
	echo -n "red" | nc -4u -w0 localhost 1738
else
	echo -n "green" | nc -4u -w0 localhost 1738
fi

#For logging
date >> /Users/AlexLand/Scripts/ping.out
