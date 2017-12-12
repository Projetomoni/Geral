#!/bin/bash
menu(){
  clear
    echo "================================="
   echo "1) Relatorio Atual"
   echo "2) Relatório Completo"
   echo "3) Iniciar serviço"
   echo "4) Parar serviço"
   echo "5) Status do serviço"
   echo "6) Equipamentos Monitorados"
   echo "7) Ping Específico"
   echo "8) Sair"
   echo "================================="
   read -p "Escolha uma opção: " OPCAO
   case $OPCAO in
           1) less arm_info ; menu ;;
           2) less arm_infolog ; menu;;
           3) source serv_ping.sh 'start' ;;
           4) source serv_ping.sh 'stop' ;;
           5) source serv_ping.sh 'status' ;;
           6) less registrados.csv ; clear ; menu ;;
           7) . espec.sh ;;
           8) exit 0 ;;
           *) echo Opção inexistente ;;
esac
}
menu
