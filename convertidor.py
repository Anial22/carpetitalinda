import temperatura
import masa
import tiempo

def convertir_temperatura(valor,unidad_origen,unidad_destino):
   if unidad_origen == "celsius" and unidad_destino =="farenheit":
     return temperatura.celsius_a_fahrenheit(valor)

if __name__=="__main__":
   valor = 20
   unidad_origen ="celsius"
   unidad_destino= "fahrenheit"
   resultado= convertir_temperatura(valor,unidad_origen, unidad_destino)
   print(f"(valor) de (unidad_origen) equivale a (resultado) (unidad_destino)" )
