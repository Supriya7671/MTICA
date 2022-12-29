def KelvinTOFahrenheit(Temperature):
    assert(Temperature>=0),"Colder then absolute zero at MTICA!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print (KelvinTOFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print (KelvinTOFahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print (KelvinTOFahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print (KelvinTOFahrenheit(-5))
except Exception as ob:
    print(ob)

print("Thank you")
              
