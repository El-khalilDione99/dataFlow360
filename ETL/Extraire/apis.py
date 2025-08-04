import requests



# récuperation des donné pour chaque endpoint
def extarc_APIS(endpoint,token):
    reponse = requests.get(f"{url_base}/{endpoint}", headers={"Authorization":f"Bearer {token}"})
    donnees = reponse.json()

    return donnees


if __name__=="__main__": # Bonne pratique

    url_base = "http://192.168.3.51:8000"

    reponse_login = requests.post(f"{url_base}/utilisateurs/login",params={"username":"kalilou","password":"5072143"})
    token = reponse_login.json()["access_token"]

    cours = extarc_APIS("cours",token) # enpoint cours
    eleves = extarc_APIS("eleves",token) # endpoint eleves 
    notes = extarc_APIS("notes",token) # endpoint notes
    enseignants = extarc_APIS("enseignants", token) # endpoint enseignants 
    presences = extarc_APIS("presences", token) # endpoint presences 
    etablissements = extarc_APIS("etablissements", token) # enpoints etablissements 
    matiere = extarc_APIS("matiere", token) # enpoint matiers
    regions = extarc_APIS("regions", token) # endpoint regions
  