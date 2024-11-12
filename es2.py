tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Monza", [
        ("gennaio", ("elettrico", 30)),
        ("gennaio", ("gas", 15)),
        ("febbraio", ("elettrico", 20)),
        ("febbraio", ("gas", 10)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Mantova", [
        ("gennaio", ("elettrico", 34)),
        ("gennaio", ("gas", 21)),
        ("febbraio", ("elettrico", 78)),
        ("febbraio", ("gas", 84)),
        # Aggiungi altri mesi e consumi
    ]),
    # Aggiungi altre città
)
def media_risorsa(citta, risorsa):
    media=0
    conta=0
    for citta2,[(mese,(risorsa2,energiamax))] in tupla_consumi_energetici:
        if(citta2==citta and risorsa2==risorsa):
            media+=energiamax
            conta+=1
        media2/=conta
        return media2
      

print(media_risorsa(tupla_consumi_energetici))    



