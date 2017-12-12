#!/bin/bash
 clear

 verificando(){
 > arm_info
 for nome in $(cat registrados.csv | cut -d";" -f1); do
         for ip in $(cat registrados.csv | grep ^$nome\; | cut -d";" -f2); do
                 ping -W 1 -i 1 -c 1 $ip &> /dev/null 
                 [[ $? == "0" ]] && \
                 echo '['$(date)'host:'$nome'ip:'$ip']->UP' >> arm_info || \
                 echo '['$(date)'host:'$nome'ip:'$ip']->DOWN' >> arm_info
         done
 done
 cat arm_info >> arm_infolog
 }
 verificando
