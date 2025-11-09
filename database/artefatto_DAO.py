from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod  # creo un metodo che può essere usato senza self perché non accede alla classe
    def get_artefatti(epoca, museo):
        cnx = ConnessioneDB.get_connection()   # connessione con il metodo definito in DB_connect
        artefatti = []  # lista a cui appenderò i risultati della query
        if cnx is None:
            print("Connessione non esistente")
            return None
        else:
            cursor = cnx.cursor()
            query = """
                    SELECT artefatto.id, artefatto.nome, artefatto.tipologia, epoca, id_museo
                    FROM artefatto, museo 
                    WHERE artefatto.id_museo=museo.id
                    AND artefatto.epoca = COALESCE(%s, artefatto.epoca)
                    AND museo.nome = COALESCE(%s, museo.nome)
                    """  # cerco gli artefatti con determinate epoche e musei
            # con COALESCE se il valore è null restituisce il parametro seguente
            cursor.execute(query, (epoca, museo))  # al posto di %s inserisco i parametri forniti
            for riga in cursor:
                artefatti.append(Artefatto(riga[0], riga[1], riga[2], riga[3], riga[4]))  # creo degli oggetti artefatto con i parametri forniti dal DB
        cnx.close()
        cursor.close()
        return artefatti

    @staticmethod  # creo un metodo che può essere usato senza self perché non accede alla classe
    def get_epoche():
        cnx = ConnessioneDB.get_connection()   # connessione con il metodo definito in DB_connect
        artefatti = []  # lista a cui appenderò i risultati della query
        if cnx is None:
            print("Connessione non esistente")
            return None
        else:
            cursor = cnx.cursor()
            query = """
                    SELECT *
                    FROM artefatto
                    ORDER BY(epoca)
                    """  # seleziono gli artefatti
            cursor.execute(query)
            for riga in cursor:
                artefatti.append(Artefatto(riga[0], riga[1], riga[2], riga[3], riga[4]))  # cursor restituisce una tupla quindi prendo solo il valore dell'epoca
        cnx.close()
        cursor.close()
        epoche = []
        for artefatto in artefatti:
            if artefatto.epoca not in epoche:  # aggiungo solo le epoche che non sono già presenti
                epoche.append(artefatto.epoca) # aggiungo alla lista di epoche ogni epoca dell'oggetto artefatto
        return epoche