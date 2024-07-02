"""
Diccionarios Anidados lo agregas a una lista
"""
usuarios = [
    {'nombre':'Juan','edad':25,'ciudad':'california'},
    {'nombre':'Arturo','edad':22,'ciudad':'new york'},
    {'nombre':'Pedro','edad':15,'ciudad':'texas'},
    {'nombre':'Miguel','edad':23,'ciudad':'california'},
    {'nombre':'Jose','edad':29,'ciudad':'california'},
]
#print(usuarios[3]["ciudad"])

nuevo= {
      'nombre':'Oscar',
      'edad':36,
      'ciudad':'miami'
 }
usuarios.append(nuevo)
print(usuarios)

