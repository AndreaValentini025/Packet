// ==UserScript==
// @name         Autocompilazione progetti formativi
// @namespace    https://github.com/AndreaValentini025/Prova
// @version      0.1
// @description  Compilazione automatica per richieste di attività progettuali
// @author       Valentini Andrea & Artoni Alessandro
// @match        http://127.0.0.1:8000/polls/inserimento/
// @match        https://placement.unimore.it/it/aziende/aiuto/
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

function copy(){
    GM_setValue("nome",document.getElementById("Nome").value);
    GM_setValue("cognome",document.getElementById("Cognome").value);
    GM_setValue("azienda",document.getElementById("Azienda").value);
    GM_setValue("funzione_aziendale",document.getElementById("FunzionaAziendale").value);
    GM_setValue("attivita_azienda",document.getElementById("AttivitaAzienda").value);
    GM_setValue("citta",document.getElementById("Citta").value);
    GM_setValue("nazione",document.getElementById("Nazione").value);
    GM_setValue("email",document.getElementById("Email").value);
    GM_setValue("telefono",document.getElementById("Telefono").value);
    GM_setValue("cellulare",document.getElementById("Cellulare").value);
    GM_setValue("argomento",document.getElementById("argomentiContatto").value);
    GM_setValue("testo",document.getElementById("Testo").value);
}

function paste(){
   var nome = document.getElementById("Nome") ;
   var cognome = document.getElementById("Cognome") ;
   var azienda = document.getElementById("Azienda") ;
   var funzione_aziendale = document.getElementById("FunzionaAziendale") ;
   var attivita_azienda = document.getElementById("AttivitaAzienda") ;
   var citta = document.getElementById("Citta") ;
   var nazione = document.getElementById("Nazione") ;
   var email = document.getElementById("Email") ;
   var telefono = document.getElementById("Telefono") ;
   var cellulare = document.getElementById("Cellulare") ;
   var argomento = document.getElementById("argomentiContatto") ;
   var testo = document.getElementById("Testo") ;

    nome.value = GM_getValue("nome");
    cognome.value = GM_getValue("cognome");
    azienda.value = GM_getValue("azienda");
    funzione_aziendale.value = GM_getValue("funzione_aziendale");
    attivita_azienda.value = GM_getValue("attivita_azienda");
    citta.value = GM_getValue("citta");
    nazione.value = GM_getValue("nazione");
    email.value = GM_getValue("email");
    telefono.value = GM_getValue("telefono");
    cellulare.value = GM_getValue("cellulare");
    argomento.value = GM_getValue("argomento");
    testo.value = GM_getValue("testo");
}

(function() {
    'use strict';

    if(window.location.hostname == "127.0.0.1"){
        var buttonCopy = document.createElement("input");
             buttonCopy.type = "button";
             buttonCopy.value = "Retrive data";
             buttonCopy.onclick = copy;
			 document.getElementById("buttonDiv").appendChild(buttonCopy);
    }
    else
    {
        var buttonPaste = document.createElement("input");
             buttonPaste.type = "button";
             buttonPaste.value = "Paste data";
             buttonPaste.onclick = paste;
			 document.getElementById("PageText").parentElement.appendChild(buttonPaste);
    }
})();