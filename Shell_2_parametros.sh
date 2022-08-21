Help () {
	echo "Debe ingresar 3 parámetros:\n posición inicial, velocidad inicial y tiempo total"
}


if ! [ $# -eq 3 ];
then
	Help
	exit 1
else
	echo "corriendo programa"
fi

