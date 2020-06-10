#!/bin/bash

echo -n "Type any number from 1-3:"

valid=0

while
[ $valid == 0 ]

do

        read ans
        case $ans in
	1	) echo Hello World
		   valid=1 ;;
	2	) echo The message is still cooler than you
		   valid=1 ;;
	3	) echo What are good resources to learn more about bash?
		   valid=1 ;;
        *       ) echo 1-3 numbers please ;;
        esac
done
