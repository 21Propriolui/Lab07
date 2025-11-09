import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()  # prendo epoche e musei direttamente dal model
        musei.insert(0,"Nessun filtro")
        epoche.insert(0,"Nessun filtro")  # aggiungo la possibilità di non mettere filtri
        for museo in musei:
            self._view.dropdown_museo.options.append(ft.dropdown.Option(museo)) # per ogni museo lo aggiungo alle opzioni del dropdown
        for epoca in epoche:
            self._view.dropdown_epoca.options.append(ft.dropdown.Option(epoca)) # per ogni epoca la aggiungo alle opzioni del dropdown
        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    def imposta_dropdown_museo(self, e):
        self.museo_selezionato = self._view.dropdown_museo.value  # valore del dropdown

    def imposta_dropdown_epoca(self, e):
        self.epoca_selezionata = self._view.dropdown_epoca.value  # valore del dropdown


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e): # bottone per quando scelgo museo ed epoca
        self._view.list_view_artefatti.controls.clear()
        if self.museo_selezionato == 'Nessun filtro':
            museo = None
        else:
            museo = self.museo_selezionato
        if self.epoca_selezionata == 'Nessun filtro':
            epoca = None
        else:
            epoca = self.epoca_selezionata

        artefatti = self._model.get_artefatti_filtrati(epoca, museo)  # lancio la query con i parametri del dropdown
        if artefatti:
            for artefatto in artefatti:
                self._view.list_view_artefatti.controls.append(ft.Text(artefatto))
        else:
            self._view.list_view_artefatti.controls.append(ft.Text('Nessun artefatto trovato con i filtri utilizzati', size=40, color='red'))
        self._view.update()