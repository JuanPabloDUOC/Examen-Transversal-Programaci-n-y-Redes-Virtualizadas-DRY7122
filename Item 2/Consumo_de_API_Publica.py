import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "LX3K7iXea6rPD5ijBJ9oTuTt3p2yIBSo"


while True:
    origen = input("Ciudad de Origen: ")
    if origen == "salir" or origen == "s":
        break
    destino = input("Ciudad de Destino: ")
    if destino == "salir" or destino == "s":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":origen, "to":destino, "locale":"es_ES","unit":"K"}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = Solicitud de ruta exitosa.\n")
        print("=============================================")
        print("Indicaciones desde " + (origen) + " hasta " + (destino))
        print("Duración del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilómetros:      " + str("{:.2f}".format(json_data["route"]["distance"])))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str("{:.2f}".format(each["distance"])) + " km)")
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Información entregada no válida para una o ambas direcciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Falta una entrada para una o ambas direcciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Consulte:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
