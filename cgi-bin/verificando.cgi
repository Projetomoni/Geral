#!/bin/bash
read OP
PO=$(echo $OP | cut -d"=" -f2)
echo "content-type: text/html"
echo
um(){
        ./ciclo_ping.cgi &> /dev/null
        echo $!>/var/run/ciclo_ping.pid
        echo "<h1>ciclo_ping.cgi está em execução</h1>"
        pid= `cat /var/run/ciclo_ping.pid`
}

dois(){
        killall ciclo_ping.pid
        rm -rf /var/run/ciclo_ping.pid
        echo "<h1>ciclo_ping.cgi não está mais em execução</h1>"
}

case $PO in

 "iniciar") um ;;
 "parar") dois ;;
 *) echo "<h1>Opcão Inexistente</h1>"

esac



