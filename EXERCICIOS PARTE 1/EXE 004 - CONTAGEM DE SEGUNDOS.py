seg = input("Por favor, entre com o número de segundos que deseja converter: ")
segTotal = int(seg)
horas = segTotal // 3600
segrestantes = segTotal % 3600
dias = horas // 24
horasRest = horas % 24
minutos = segrestantes // 60
segundos = segrestantes % 60
print(dias, "dias,", horasRest, "horas,", minutos, "minutos e", segundos, "segundos.")
