#!/bin/bash
case "$1" in 
start)
   ./ciclo_ping.sh &> /dev/null &
   echo $!>/var/run/ciclo_ping.pid
   echo ciclo_ping.sh está em execução, pid=`cat /var/run/ciclo_ping.pid`
   ;;
stop)
   kill `cat /var/run/ciclo_ping.pid`
   rm /var/run/ciclo_ping.pid
   echo ciclo_ping.sh não está mais em execução
   ;;
restart)
   $0 stop
   $0 start
   ;;
status)
   if [ -e /var/run/ciclo_ping.pid ]; then
      echo ciclo_ping.sh está em execução, pid=`cat /var/run/ciclo_ping.pid`
   else
      echo ciclo_ping.sh não está em execução
   fi
   ;;
*)
   echo "Usage: $0 {start|stop|status|restart}"
esac
read -p "Pressione [enter] para continuar..."
. monito.sh
