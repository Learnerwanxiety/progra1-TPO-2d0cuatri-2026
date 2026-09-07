"""la idea de este archivo es contener data basica utilizada para el proyecto, es decir, no se debe agregar logica aca, 
la idea es generar las registros basicos para el proyecto en la etapa de inicializacion, y tambien guardar los regitros que se generen para las pruebas,
 asi no tienen que correr la aplicacion cada vez que quieran probrar algo."""

#registro inicial
socios = [
    [101, "Carlos Gómez",   "Tenis",      4500.0, "Activo"],
    [102, "Ana Martínez",   "Natación",   5000.0, "Activo"],
    [103, "Lucía Fernández", "Gimnasio",  3800.0, "Inactivo"],
    [104, "Roberto Díaz",   "Básquet",    4200.0, "Activo"],
    [105, "Mariana López",  "Fútbol",     4000.0, "Activo"]
] 

opciones_de_menu = [
  "1.) Dar de alta un registro",
  "2.) Consultar un registro",
  "3.) Modificar un registro",
  "4.) Eliminar un registro",
  "5.) Mostrar todos los registros",
  "6.) Consultar registros por categoría",
  "7.) Estadisticas",
  "8.) Salir",
]