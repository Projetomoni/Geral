#!/bin/bash
echo "content-type: text/html"
echo
	echo "<html>"
       ./ciclo_ping.cgi &> /dev/null
        echo $! > /var/run/ciclo_ping.pid
        echo "<h1>ciclo_ping.cgi está em execução</h1>"
        pid=$(cat /var/run/ciclo_ping.pid)
