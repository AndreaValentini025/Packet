// ==UserScript==
// @name         Autocompilazione progetti formativi
// @namespace    https://github.com/AndreaValentini025/Prova
// @version      0.1
// @description  Compilazione automatica per richieste di attività progettuali
// @author       Valentini Andrea & Artoni Alessandro
// @match        https://services.ing.unimore.it/tirocini/gestione/*/
// @match        file:///C:/Users/hp/OneDrive/Desktop/Pagina1Alma.html
// @match        file:///A:/andre/Desktop/Pagina1Alma.html
// @match        file:///C:/Users/hp/OneDrive/Desktop/Pagina2Alma.html
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

function copy(){

    GM_setValue("referente", document.getElementById("referente").value);
    GM_setValue("nome",document.getElementById("id_nome").value);
    GM_setValue("cognome",document.getElementById("id_cognome").value);
    GM_setValue("codice_fiscale",document.getElementById("id_codice_fiscale").value);
    GM_setValue("matricola",document.getElementById("id_matricola").value);
    GM_setValue("tutor",document.getElementById("id_tutor").value);
    GM_setValue("sede",document.getElementById("id_sede").value);
    GM_setValue("durata",document.getElementById("id_durata").value);
    GM_setValue("data_inizio",document.getElementById("id_data_inizio").value);
    GM_setValue("data_fine",document.getElementById("id_data_fine").value);
    GM_setValue("obiettivi",document.getElementById("id_obiettivi").value);
	alert("Dati copiati");
	document.getElementById("conferma").disabled=false;
    window.open("https://placement.unimore.it/staff/home/ent/tirocini/pf/progettoformativostep1.aspx?lang=it&idAzienda=30000510");
}

function pastePage1(){
   var tipo = document.getElementById("TipoTirocinio") ;
   var regione = document.getElementById("RegioneDocumento") ;
   var data_inizio = document.getElementById("DataInizioProgettoFormativo") ;
   var data_fine = document.getElementById("DataFineProgettoFormativo") ;
   var codice_fiscale = document.getElementById("CodFisc") ;
   var matricola = document.getElementById("Matricola") ;
    var di= new Date(GM_getValue("data_inizio"));
    data_inizio.value = di.toLocaleDateString();
    var df= new Date(GM_getValue("data_fine"));
    data_fine.value = df.toLocaleDateString();
    codice_fiscale.value = GM_getValue("codice_fiscale");
    tipo.value = 2;
    var opt = tipo.getElementsByTagName("option");
    for(var i = 0; i < opt.length; i++){
        if(opt[i].value != tipo.value){
            console.log(opt[i].value + " " + tipo.getElementsByTagName("option")[i].selected);
            opt[i].selected = false;
        }
        else{
            console.log(opt[i].value + " " + tipo.getElementsByTagName("option")[i].selected);
            opt[i].selected = true;
        }
    }
    regione.value = 1006;
    //regione.getElementsByTagName("option")[regione.value].selected = true;
    matricola.value = GM_getValue("matricola");
}

function pastePage2(){
   var nome_tutor_accademico = document.getElementById("TutorAccademicoTutorAccademicoNome") ;
   var cognome_tutor_accademico = document.getElementById("TutorAccademicoTutorAccademicoCognome") ;
   var email_tutor_accademico = document.getElementById("TutorAccademicoTutorAccademicoEmail") ;
   var nome_tutor_aziendale = document.getElementById("TutorAziendaleNome") ;
   var cognome_tutor_aziendale = document.getElementById("TutorAziendaleCognome") ;
   var email_tutor_aziendale = document.getElementById("TutorAziendaleEmail") ;
   var referente = document.getElementById("RappresentanteNominativo") ;
   var sede = document.getElementById("StabilimentoRepartoUfficio") ;
   var ora_ingresso = document.getElementById("OrarioAccessoInizio") ;
   var ora_uscita = document.getElementById("OrarioAccessoFine") ;
   var durata = document.getElementById("TirocinioDurata") ;
   var obiettivi = document.getElementById("Attivita") ;

   var nome_tutor = GM_getValue("tutor").slice(0, GM_getValue("tutor").lastIndexOf(" "));
   var cognome_tutor = GM_getValue("tutor").slice(GM_getValue("tutor").lastIndexOf(" ") + 1);
   nome_tutor_accademico.value = nome_tutor;
   cognome_tutor_accademico.value = cognome_tutor;
   email_tutor_accademico.value = nome_tutor.toLowerCase().replace(/\s+/g, '') + "." + cognome_tutor.toLowerCase() + "@unimore.it";
   nome_tutor_aziendale.value = "Massimo";
   cognome_tutor_aziendale.value = "Borghi";
   email_tutor_aziendale.value = "direttore.dief@unimore.it";
   referente.value = GM_getValue("referente");
   sede.value = GM_getValue("sede");
   ora_ingresso.value = "08:00";
   ora_uscita.value = "19:00";
   durata.value = GM_getValue("durata");
   obiettivi.value = GM_getValue("obiettivi");
}

(function() {
    'use strict';

    if(window.location.hostname == "services.ing.unimore.it"){
        var buttonCopy = document.createElement("input");
             buttonCopy.type = "button";
             buttonCopy.value = "Retrive data";
             buttonCopy.style.backgroundColor = "green";
             buttonCopy.onclick = copy;
			 document.getElementById("formDelete").insertAdjacentElement('afterbegin', buttonCopy);
    }
    else if(window.location.pathname == "/A:/andre/Desktop/Pagina1Alma.html" || window.location.pathname == "/C:/Users/hp/OneDrive/Desktop/Pagina1Alma.html")
    {
        var buttonPaste = document.createElement("input");
             buttonPaste.type = "button";
             buttonPaste.value = "Paste data";
             buttonPaste.onclick = pastePage1;
			 document.getElementById("PageContent").appendChild(buttonPaste);
    }
    else{
        var buttonPaste2 = document.createElement("input");
             buttonPaste2.type = "button";
             buttonPaste2.value = "Paste data";
             buttonPaste2.onclick = pastePage2;
			 document.getElementById("dettaglioProgettoFormativo").appendChild(buttonPaste2);
    }
})();
