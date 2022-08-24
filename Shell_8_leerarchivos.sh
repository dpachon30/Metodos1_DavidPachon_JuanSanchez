i=0
while IFS= read -r line
do
  RUTAS[i]=$line
  i=`expr $i + 1`
done < $1

echo " ${RUTAS[2]}"

