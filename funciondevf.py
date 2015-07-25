def Funcion(var):
        invertida = var[::-1]
        ve = ['E', 'e']
        i = 0
        contador = 0
        while i < len(var):
        	contador += ve.count(var[i])
        	i += 1
        resultado = invertida+", "+"frencuencia de e:"+str(contador)

        return resultado



palabra = "El DevF rockea"

print Funcion(palabra)


   
    


