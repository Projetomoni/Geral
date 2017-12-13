#!/bin/bash
read POST
echo content-type: text/html
echo
foi(){
cat <<EOFFF
  <html>
<head>
<script>alert("Cadastrado com sucesso!");</script>
<meta http-equiv="refresh" content=0;url="../menu.html">
</head>
  </html>
EOFFF
}

foinao(){
cat <<EOFFF
  <html>
<head>
<script>alert("Erro no cadastro, Redirecinando...");</script>
<meta http-equiv="refresh" content=0;url="../addequip.html">
</head>
  </html>
EOFFF
}

maquina=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
ip=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)

if [[ ! $(grep "^$maquina;" resto/registrados.csv) ]] ; then
                if [[ ! $(grep "^$ip;" resto/registrados.csv) ]] ; then
                  foinao
        else
   echo "$maquina;$ip" >> resto/registrados.csv
    foi
        fi
else
   foinao
fi

