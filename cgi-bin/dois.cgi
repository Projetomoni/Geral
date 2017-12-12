#!/bin/bash
echo "content-type: text/html"
echo
        killall ciclo_ping.cgi
        rm -rf /var/run/ciclo_ping.pid
        echo "<h1>ciclo_ping.cgi não está mais em execução</h1>"
