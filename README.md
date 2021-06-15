<h1>Projektidee</h1>
<h3>Ausgangslage</h3>
Mitarbeitende im Gesundheitsbereich müssen sich sehr viele Sachen merken und sich die Informationen von verschiedenen Orten beschaffen.
Dies bringt eine hohe und gefährliche Fehlerquelle mit sich.<br>
<h3>Funktion/Projektidee</h3>
Mit meinem Projekt will ich dies erleichtern. Die Patientendaten können mit den wichtigsten Informationen erfasst werden
und zu jedem Zeitpunkt abgerufen werden, um zu wissen, was bei welchem Patient verarbeicht werden muss. <br><br>
<h3>Workflow</h3>
<h4>Dateieingabe</h4>
Die Patientendaten (Name, Alter, usw.) werden erfasst. Zusätzlich werden die verschriebenen Medikamente und die Tageszeit, zu der sie angewendet werden müssen, erfasst. <br>
<h4>Dateiverarbeitung/Speicherung</h4>
Die Daten werden in zwei JSON Dateien in Form eines Dictionary gespeichert.<br>
<h4>Datenausgabe</h4>
Der Name einer Person kann eingeben werden bzw. die Datenbank kann durchsucht werden. Anschliessend werden alle Medikamentenangaben und sonstige Informationen
zu dieser Person angezeigt.  
Wenn die Medikamente verabreicht wurden, muss dies entsprechend angehackt werden.<br>
Neben dem Anzeigen der Daten kann auch eine Statistik angezeigt werden, um zu überprüfen,
ob alle Medikamente immer verabreicht wurden.<br>
<h1>Diagramme</h1>
Neues Medikament zu einer Person hinzufügen<br>
<img src="{{url_for('static', filename='medtrack_diagramm_Medikament erfassen.png')}}"><br>
Person suchen und verabreichte Medikamente bestätigen<br>
<img src="{{url_for('static', filename='medtrack_diagramm_Person suchen.png')}}">