import math

def media(num):
    """
    Calcula el promedio de una lista de números.
    Verifica y elimina NaNs en los datos.
    Parametros
    ---------
    num: lista
         lista con los numeros
    Retorna
    -------
    promedio: float
          el promedio de los numeros
    """
    #verificar si hay NaNs y eliminarlos:
    num = [x for x in num if not math.isnan(x)]
    if not num:
        return float('nan')
    promedio = sum(num) / len(num)
    return promedio

def moda(num):
    """
    Identifica la moda de una lista "num"
    --------
    Parametros:
    num
    retorna un int que indica el valor y la cantidad de veces que se repite
    """
    num=[x for x in num if not math.isnan(x)]
    frecuencias={}
    if len(num)==0:
        return None
    if not num:
        return float("nan")
    for x in num:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    max_frec=max(frecuencias.values())
    modas=[k for k, v in frecuencias.items() if v==max_frec]

    return modas, max_frec

def mediana(num):
    num=[x for x in num if not math.isnan(x)]
    if len(num) == 0:
        return None
    if not num:
        return float("nan")
    num_ordenados=sorted(num)
    n=len(num)
    mitad=n//2
    if n%2==0:
        return (num_ordenados[mitad-1]+num_ordenados[mitad])/2
    else:
        return num_ordenados[mitad]

def desviacion_absoluta(num):
    num=[x for x in num if not math.isnan(x)]
    if len(num)==0:
        return None
    if not num:
        return float('nan')
    med = mediana(num)
    desv_abs = [abs(x - med) for x in num]
    return mediana(desv_abs)

def rango(num):
    num=[x for x in num if not math.isnan(x)]
    if len(num) == 0:
        return None
    if not num:
        return float("nan")
    range=num[-1]-num[0]
    return range
def varianza(num):
    num=[x for x in num if not math.isnan(x)]
    if len(num) == 0:
        return None
    if not num:
        return float("nan")
    mu=media(num)
    return sum((x-mu)**2 for x in num)/len(num)

def desviacion_estandar(num):
    sigma=math.sqrt(varianza(num))
    return sigma

def percentil(num, p):
    """
    datos-> lista de valores
    que se estudia
    p-> percentil ingresado que 
    retorna el valor ubicado en
    este percentil.
    """
    if p<0 or p>100:
        raise ValueError("El percentil debe estar entre 0 y 100")
    if len(num) == 0:
        return None
    if not num:
        return float("nan")
    num=sorted(num)
    n=len(num)
    
    pos=(p/100)*(n-1)
    i=int(pos)
    frac=pos-i
    
    if (i+1)<n:
        return num[i] * (1 - frac) + num[i + 1] * frac
    else:
        return num[i]

def rango_intercuartilico(num):
    if len(num) == 0:
        return None
    if not num:
        return float("nan")
    q1 = percentil(num, 25)
    q3 = percentil(num, 75)
    return q3 - q1
    
def covarianza(vals_x, vals_y):
    #revisar que no existan NaNs, y los eliminamos
    x=[]
    y=[]
    for i in range(len(vals_x)):
        if math.isfinite(vals_x[i]) & math.isfinite(vals_y[i]):
            x.append(vals_x[i])
            y.append(vals_y[i])
    p_x=media(x)
    p_y=media(y)
    tt=[]
    for xv, yv in zip(x,y):
        tt.append( (xv - p_x)*(yv - p_y))
    covarianza = sum(tt)/len(tt)
    return covarianza

def correlacion(vals_x, vals_y):
    x=[]
    y=[]
    for i in range(len(vals_x)):
        if math.isfinite(vals_x[i]) & math.isfinite(vals_y[i]):
            x.append(vals_x[i])
            y.append(vals_y[i])
            r_xy = covarianza(x,y) /math.sqrt(varianza(x) * varianza(y))
            return r_xy