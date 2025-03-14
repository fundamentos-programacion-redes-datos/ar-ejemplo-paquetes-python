"""

"""
def obtener_reporte(tipo, lista):

    reporte = ""
     
    if tipo == 1:
        reporte = "\nListado de Estudiantes\n"  # Cadena para almacenar la lista de docentes
        
        # Construcción del reporte de estudiantes a partir de la lista de estudiantes
        for i in lista:
            reporte = f"{reporte}{i[0]} {i[1]} -correo:{i[2]}-, edad:{i[3]}\n"
    else:
        if tipo == 2:
            reporte = "\nListado de Docentes\n"  # Cadena para almacenar
            
            # Construcción del reporte de docentes a partir de la lista de docentes
            for i in lista:
                reporte = f"{reporte}{i[0]} {i[1]} -ciudad de residencia:{i[2]}\n"

    return reporte

