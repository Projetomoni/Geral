#!/bin/bash
while : ; do
	source pingar.cgi &
	echo $!> pid
	sleep 10
done
