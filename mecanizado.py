import math

def calcular_velocidad_de_corte(diametro, velocidad_de_rotacion):
    return(math.pi*diametro*velocidad_de_rotacion)/1000

def calcular_avance_por_dientes(avance_total, cantidad_de_dientes):
    return avance_total/cantidad_de_dientes


#definir propiedades de corte para diferentes materiales
propiedades_de_corte={"acero":{"coeficiente_potencia":0.1,"factor_material":5},
                       "aluminio":{"coeficiente_potencia":0.08,"factor_material":2}}

#funcion lambda
calcular_potencia_de_corte= lambda coeficiente,velocidad,avance,factor:(coeficiente*velocidad*avance)+factor

# entrada dinamica de datos
try:
    diametro= float(input("Ingrese el diametro de la fresa (mm): "))
    velocidad_de_rotacion=float(input("Ingresa la velocidad de rotacion de la fresa (rpm):"))
    avance_total=float(input("Ingrese el avance total: "))
    cantidad_de_dientes=int(input("Ingrese la cantidad de dientes de la fresa: "))
    tipo_material=input("Ingrese el tipo de material: ")

    velocidad_de_corte=calcular_velocidad_de_corte(diametro,velocidad_de_rotacion)
    avance_por_diente=calcular_avance_por_dientes(avance_total,cantidad_de_dientes)

 # verificar material
    if tipo_material in propiedades_de_corte:
        propiedades=propiedades_de_corte[tipo_material]
        coeficiente_potencia=propiedades["coeficiente_potencia"]
        factor_material=propiedades["facto_material"]

 #funcionn lambda
        potencia_de_corte=calcular_potencia_de_corte(coeficiente_potencia,velocidad_de_corte,avance_por_diente,factor_material)

        print("\n resultados")
        print(f"velocidad de corte: {velocidad_de_corte:.2f} m/min")
        print(f"avance por diente{avance_por_diente:.2f} mm/diente")
        print(f"potencia de corte{potencia_de_corte:.2f} W")
    else:
        print(f"No se encontraron propiedadese para ese material '{tipo_material}'")
except ValueError:
    print("ERROR: ingrese numeros validos")
except ZeroDivisionError:
    print("ERROR: no se puede dividir entre 0")
except Exception as e:
    print(f"oooo error inesperado wow!!:{e}")