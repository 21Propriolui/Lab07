from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod # creo un metodo che può essere usato senza self perché non accede alla classe
    def get_musei():
        cnx = ConnessioneDB.get_connection()   # connessione con il metodo definito in DB_connect
        musei = []  # lista a cui appenderò i risultati della query
        if cnx is None:
            print("Connessione non esistente")
            return None
        else:
            cursor = cnx.cursor()
            query = """
                    SELECT * 
                    FROM museo
                    ORDER BY(nome)
                    """
            cursor.execute(query)
            for riga in cursor:
                musei.append(Museo(riga[0],riga[1], riga[2]))  # creo degli oggetti museo con i parametri forniti dal DB
        cnx.close()
        cursor.close()
        nomi = []
        for museo in musei:
            nomi.append(museo.nome) # aggiungo alla lista di nomi ogni nome dell'oggetto museo
        return nomi