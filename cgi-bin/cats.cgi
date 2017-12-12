#!/bin/bash
IFS=$'\n'
read SO
VAI=$(echo $SO | cut -d"=" -f2)
echo "content-type: text/html"
echo
um(){
	for x in $(cat ./resto/arm_info); do
		echo "<p>$x</p>"
	done
}

dois(){
	for x in $(cat ./resto/arm_infolog); do
		echo "<p>$x</p>"
	done
}

if [[ $VAI == "atual" ]] ; then
um
elif [[ $VAI == "completo" ]] ; then
dois
else
echo "Opção Inexistente"
fi
