mi_biografia=["Mi nombre es Adrian Oña y nací el 1 de junio de 2002, mis padres son Edwin Oña Saravia y Carla Medrano",
              "de pequeño viví en la casa de mis abuelos junto a mis padres hasta la etapa de kinder, estuve en dos",
              "kinderes, el Carita de Angel y el Saul Mendoza, siempre hubieron discusiones entre mis padres hasta que ",
              "llegó el dia en que se divorciaron, para ese dia contaba ya con mi hermano Alejandro que tendria unos 2",
               "años yo creo, nos llevamos con 3 asi que estaba por empezar la escuela. Quedamos en custodia de mi mamá y",
               "pasamos la etapa escolar en diferentes escuelas, hice amigos de aqui para alla, nos fuimos a vivir a Oruro",
                "un tiempo pero regresabamos a Sucre en vacaciones hasta que un año fue definitivo y nuestra custodia paso",
               "a manos de mi padre. Luego de eso entre a secundaria, me adapte de nuevo a vivir en Sucre y pase la mayor parte",
               "de secundaria en el colegio Domingo Savio, siempre me mantuve entre el top 5 de mejores alumnos e hice amigos,",
                "tambien participe en diferentes eventos o lidere actos de curso.",
                "En la promocion tuve mi primera novia y vivimos una relacion complicada pero a la vez muy feliz, duro un par de años.",
                "En ese lapso habia acabado el colegio y entrado a la carrera que queria desde que la conoci, me refiero a ",
                "Ingenieria en Diseño y animacion digital, pues esta tenia todo lo que me gustaba, arte y ciencia, el primer semestre",
                "empezo y todo iba bien hasta que justo ese año sucedio la pandemia del COVID 19, la cual afecto a todo el mundo",
                "y nos orillo a la virtualidad, nos adaptamos y asi fui pasando los semestres entrantes con un arrastre que me lleve",
                "en el primero por no poderme cambiar de grupo en calculo1, no pude dar examenes asi que no habia notas pero bueno,",
                "las demas materias si las he pasado, algunas con mas dificultad que otras debo decir, pero aqui estoy en sexto semestre",
                "esperando poder acabar a tiempo la carrera y poder iniciar otra mas adelante. Este año entro de auxiliar tambien."]
bucle=1

def imprimir_bio():
        for i in range(len(mi_biografia)):
            print(mi_biografia[i])

def imprimir_opciones():
    print("1.Imprimir Biografia","\n2.Salir del programa")

print("---------MENU DE LA BIOGRAFIA DE ADRIAN-----------","\n Elije las opciones:")
class menu:
    
    while bucle==1:
        
        imprimir_opciones()
        elegir_opcion=int(input(">>> "))
        
       
        while elegir_opcion==1:
    
            imprimir_bio()
            imprimir_opciones()
            elegir_opcion=int(input())
        
        if elegir_opcion==2:
                print("Programa finalizado")
                bucle=0
             
            

        

        


