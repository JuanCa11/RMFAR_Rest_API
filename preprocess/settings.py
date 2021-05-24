FUZZY_SETS = {
    'SCA_AREA': ["BARRIO MUY PEQUEÑO", "BARRIO PEQUEÑO", "BARRIO MEDIANO", "BARRIO GRANDE"],
    'DENSIDAD_NOCTURNA': ["DENSIDAD NOCTURNA MUY BAJA", "DENSIDAD NOCTURNA BAJA", "DENSIDAD NOCTURNA MEDIA",
                          "DENSIDAD NORCTURNA ALTA"],
    'DENSIDAD_BANCARIA': ["DENSIDAD BANCARIA MUY BAJA", "DENSIDAD BANCARIA BAJA", "DENSIDAD BANCARIA MEDIA",
                          "DENSIDAD BANCARIA ALTA"],
    'DENSIDAD_TIENDAS': ["DENSIDAD COMERCIAL MUY BAJA", "DENSIDAD COMERCIAL BAJA", "DENSIDAD COMERCIAL MEDIA",
                         "DENSIDAD COMERCIAL ALTA"],
    'DENSIDAD_PARQUES': ["DENSIDAD PARQUES MUY BAJA", "DENSIDAD PARQUES BAJA", "DENSIDAD PARQUES MEDIA",
                         "DENSIDAD PARQUES ALTA"],
    'ILUMINACION': ["ILUMINACION MUY BAJA", "ILUMINACION BAJA", "ILUMINACION MEDIA", "ILUMINACION ALTA"],
    'PERSONAS': ["CANTIDAD DE PERSONAS MUY BAJA", "CANTIDAD DE PERSONAS BAJA", "CANTIDAD DE PERSONAS MEDIA",
                 "CANTIDAD DE PERSONAS ALTA"],
    'SEGURIDAD': ["SEGURIDAD MUY BAJA", "SEGURIDAD BAJA", "SEGURIDAD MEDIA", "SEGURIDAD ALTA"],
    'SENDERO': ["SENDERO MUY BAJO", "SENDERO BAJO", "SENDERO MEDIO", "SENDERO ALTO"],
    'TRANSPORTE': ["TRANSPORTE MUY BAJO", "TRANSPORTE BAJO", "TRANSPORTE MEDIO", "TRANSPORTE ALTO"],
}

NO_FUZZY_SETS = {
    'GENERO': ['FEMENINO','MASCULINO'],
    'HORA_INT': ["MAÑANA", "MEDIO DIA", "TARDE", "NOCHE"],
    'DIA_SEMANA_INT': ["FIN DE SEMANA", "ENTRE SEMANA"],
    'DIA_MES_INT': ["QUINCENA", "NO QUINCENA"],
        'MES': ['MONTH_1', 'MONTH_2', 'MONTH_3', 'MONTH_4', 'MONTH_5', 'MONTH_6', 'MONTH_7', 'MONTH_8', 'MONTH_9', 'MONTH_10',     'MONTH_11', 'MONTH_12'],
    'ACTIVIDAD': ['SENDERO PUBLICO', 'LOCAL COMERCIAL', 'PROPIEDAD PRIVADA', 'ESTACION DE TRANSPORTE',
                  'TRANSPORTE PUBLICO', 'PARQUES', 'TRANSPORTE PRIVADO'],
}

CLUSTER_FEATURE = 'MES'
DEFAULT_CLASS = 'HURTO A PATRIMONIO'
TARGET = ['HURTO A PERSONAS', 'HURTO A PATRIMONIO']

WILDCARDS = {
    'SCA_AREA': ["BARRIO MUY PEQUEÑO", "BARRIO PEQUEÑO", "BARRIO MEDIANO", "BARRIO GRANDE"],
    'DENSIDAD_NOCTURNA': ["DENSIDAD NOCTURNA MUY BAJA", "DENSIDAD NOCTURNA BAJA", "DENSIDAD NOCTURNA MEDIA", "DENSIDAD NORCTURNA ALTA"],
    'DENSIDAD_BANCARIA': ["DENSIDAD BANCARIA MUY BAJA", "DENSIDAD BANCARIA BAJA", "DENSIDAD BANCARIA MEDIA", "DENSIDAD BANCARIA ALTA"],
    'DENSIDAD_TIENDAS': ["DENSIDAD COMERCIAL MUY BAJA", "DENSIDAD COMERCIAL BAJA", "DENSIDAD COMERCIAL MEDIA", "DENSIDAD COMERCIAL ALTA"],
    'DENSIDAD_PARQUES': ["DENSIDAD PARQUES MUY BAJA", "DENSIDAD PARQUES BAJA", "DENSIDAD PARQUES MEDIA", "DENSIDAD PARQUES ALTA"],
    'ILUMINACION': ["ILUMINACION MUY BAJA", "ILUMINACION BAJA", "ILUMINACION MEDIA", "ILUMINACION ALTA"],
    'PERSONAS': ["CANTIDAD DE PERSONAS MUY BAJA", "CANTIDAD DE PERSONAS BAJA", "CANTIDAD DE PERSONAS MEDIA", "CANTIDAD DE PERSONAS ALTA"],
    'SEGURIDAD': ["SEGURIDAD MUY BAJA", "SEGURIDAD BAJA", "SEGURIDAD MEDIA", "SEGURIDAD ALTA"],
    'SENDERO': ["SENDERO MUY BAJO", "SENDERO BAJO", "SENDERO MEDIO", "SENDERO ALTO"],
    'TRANSPORTE': ["TRANSPORTE MUY BAJO", "TRANSPORTE BAJO", "TRANSPORTE MEDIO", "TRANSPORTE ALTO"],
    'HORA_INT': ["MAÑANA", "MEDIO DIA", "TARDE", "NOCHE"],
    'DIA_SEMANA_INT': ["FIN DE SEMANA", "ENTRE SEMANA"],
    'DIA_MES_INT': ["QUINCENA", "NO QUINCENA"],
    'MES': ['MONTH_1', 'MONTH_2', 'MONTH_3', 'MONTH_4', 'MONTH_5', 'MONTH_6', 'MONTH_7', 'MONTH_8', 'MONTH_9', 'MONTH_10', 'MONTH_11', 'MONTH_12'],
    'ACTIVIDAD': ['SENDERO PUBLICO', 'LOCAL COMERCIAL', 'PROPIEDAD PRIVADA', 'ESTACION DE TRANSPORTE',
                  'TRANSPORTE PUBLICO', 'PARQUES', 'TRANSPORTE PRIVADO'],
}

SANITY_MSG = {
    'SCA_AREA': '',
    'DENSIDAD_NOCTURNA': 'BARRIO CON',
    'DENSIDAD_BANCARIA': 'BARRIO CON',
    'DENSIDAD_TIENDAS': 'BARRIO CON',
    'DENSIDAD_PARQUES': 'BARRIO CON',
    'ILUMINACION': 'BARRIO CON',
    'PERSONAS': 'BARRIO CON',
    'SEGURIDAD': 'BARRIO CON',
    'SENDERO': 'BARRIO CON',
    'TRANSPORTE': 'BARRIO CON',
    'HORA_INT': 'IR O ESTAR EN EL/LA',
    'DIA_SEMANA_INT': 'IR O ESTAR EN',
    'DIA_MES_INT': 'IR O ESTAR EN',
    'MES': 'IR O ESTAR EN EL MES DE',
    'ACTIVIDAD': 'LA ACTIVIDAD EN',
}

PARSE_MONTH = {
    'MONTH_1': 'ENERO',
    'MONTH_2': 'FEBRERO',
    'MONTH_3': 'MARZO',
    'MONTH_4': 'ABRIL',
    'MONTH_5': 'MAYO',
    'MONTH_6': 'JUNIO',
    'MONTH_7': 'JULIO',
    'MONTH_8': 'AGOSTO',
    'MONTH_9': 'SEPTIEMBRE',
    'MONTH_10': 'OCTUBRE',
    'MONTH_11': 'NOVIEMBRE',
    'MONTH_12': 'DICIEMBRE'
}