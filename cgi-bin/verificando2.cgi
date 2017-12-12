#!/bin/bash
read OP
PO=$(echo $OP | cut -d"=" -f2)
echo "content-type: text/html"
echo
echo "<meta http-equiv="refresh" content=0;url="../todosIPs.html">"
#echo $PO
	if [[ $PO == 1 ]]
	then
	./um.cgi
else
	echo "<h1>opção inválida</h1>"
	if [[ $PO == 2 ]]
then
	./dois.cgi
else
	echo "<h1>opção inválida</h1>"
fi

