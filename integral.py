from sympy import *

def alerta(evento):
    x=symbols("x")
    y=sqrt(2*x+1)
    res = integrate(y,x)
    alert(res) 
    document['boton'].bind("click", alerta)