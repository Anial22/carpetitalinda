def segundo_a_minutos(segundos):
    return segundos /60

def horas_a_minutos(horas):
    return horas *60

if __name__=="__main__":
    segundos= 150
    minutos= segundo_a_minutos(segundos)
    print(f"(segundos) sg equivalen a (minutos) minutos")