Help () {
	echo "Debe ingresar 3 parámetros:\n posición inicial, velocidad inicial y tiempo total"
}

Help

read VALOR

if ! [ $# -eq 3 ]
then
	echo "corriendo programa"
else
	Help
fi

