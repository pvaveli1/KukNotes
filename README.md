# KukNotes
Erstellen einer Notizenanwendung
==============================================================================================
Programmiersprache:Python;
Framework: PyCharm;
verwendete Bibliotheken: flask;
verwendetes Format: JSON;
url: http://localhost:1337/notes

==============================================================================================

ANLEITUNG

1.  Terminal öffnen
2.  Gehen Sie in das Projektverzeichnis und führen Sie die „RestApi.py“ aus, um das Programm zu starten
    
    #Alle Notizen anzeigen
    GET-REQUEST = curl -i http://localhost:1337/notes
    
    #Eine bestimmte Notiz anzeigen, anhand einer existierenden id
    GET-Request = curl -i http://localhost:1337/notes/<id>
    
    #Notiz hinzufuegen
    POST-Request = curl -i -H "Content-Type: application/json" -X POST -d '{"note":"Fitness"}' http://localhost:1337/notes
    
    #Notiz verändern
    PUT-Request  = curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:1337/notes/3  

--------------
Hinweis: Bei einem Neustart des Servers, verschwinden alle Notizen die mit der POST-Request ausgeführt wurden.

-------------
