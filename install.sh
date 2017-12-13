#!/bin/bash
falhou(){
        case $1 in
        instalacao)
                echo "O programa falhou na instalação"
                exit 0 ;;
        *)
                echo "o programa falhou. Causa desconhecida"
                exit 0 ;;
        esac
}
apt-get update && apt-get install apache2 && apt-get install dialog || falhou instalacao
a2enmod cgid
cp /etc/apache2/conf-enabled/charset.conf charset.conf.bkp
echo "AddDefaultCharset UTF-8" >> /etc/apache2/conf-enabled/charset.conf
$(systemctl restart apache2)
./red.sh
