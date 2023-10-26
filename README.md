# Oblig3
Jeg har laget et workflow i Actions delen av repository, valgte en template som heter Python application for å generere den grunnleggende .yml filen for å kjøere testene på push.

Python applikasjonen heter python-app.yml, jeg endret python versjonen på filen til python versjonen jeg bruker som er 3.12.0.

Den installerer alle packages som er nødvendig fra requirements.txt og kjører pytest.

Gjorde en commit på denne filen så den gjør at Github Actions kjører workflow hver gang jeg gjør en push, som igjen kjører da disse testene.

Resultatene kan man se i Actions delen, den viser at kjøringene av testene skjer og de passerer. 
