def evaluar():
    try:
        print("Programa para calificar notas de los Estudiantes mediante 2 Notas. ")
        nota1 = int(input("Ingresa la primera parte de tu nota. "))
        nota2 = int(input("ingresa la segunda parte de tu nota. "))
        nota1 = 0.4*nota1
        nota2 = 0.6*nota2
        notafinal = nota1 + nota2 
        print (f'El porcentaje de la nota final es: {notafinal}')
    except Exception:
        print (f'El programa tiene un Error Intentelo Mas tarde')
    






