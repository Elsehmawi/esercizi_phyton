 


tupla_partite = (
    ("Barcellona", "Milan", 7, 4),
    ("Inter", "Juve", 1, 1),
    ("Barcellona", "Fiorentina", 2, 4),
    ("Lecce", "Atalanat", 0, 3),
    ("Napoli", "Roma", 1, 2),
)


def media_gol_partite(tupla_partite):
    somma=0
    conta=0
    media1=0
  
 
    for squadra_casa,squadraospiti,punteggiosquadradicasa,punteggiosquadraospiti in tupla_partite:
        somma=punteggiosquadraospiti+punteggiosquadradicasa
    conta+=1
    media1=somma/conta
    return media1
 
 
 
 

 
def media_gol_squadra(tupla_partite,squadra):
     somma=0
     media2=0
     conta=0
     for squadra_di_casa,squadra_ospite,punteggiosquadradicasa,punteggiosquadraospiti  in tupla_partite:
         if (squadra==squadra_di_casa ):
             somma+=punteggiosquadradicasa
             conta+=1
             media2=somma/conta
         else:
             somma+=punteggiosquadraospiti
             conta+=1
             media2=somma/conta
            
             
             return media2
        
def partita_con_più_gol(tupla_partite):
    maggiorgol=[]
    max=0
    s1max=""
    s2max=""
    puntimax=0
   



    for squadra_di_casa,squadra_ospite,punteggiosquadradicasa,punteggiosquadraospiti in tupla_partite:
         somma=punteggiosquadradicasa+punteggiosquadraospiti
         if(max<somma):
             max=somma
             s1max=squadra_di_casa
             s2max=squadra_ospite
             puntimax=punteggiosquadradicasa,punteggiosquadraospiti
             maggiorgol=[max,s1max,s2max,puntimax]

         return maggiorgol    
def partita_con_meno_gol(tupla_partite):
    menogol=[]
    min=2
    s1min=""
    s2min=""
    puntimin=0
   



    for squadra_di_casa,squadra_ospite,punteggiosquadradicasa,punteggiosquadraospiti in tupla_partite:
         somma=punteggiosquadradicasa+punteggiosquadraospiti
         if(min>somma):
             min=somma
             s1min=squadra_di_casa
             s2min=squadra_ospite
             puntimin=punteggiosquadradicasa,punteggiosquadraospiti
             menogol=[min,s1min,s2min,puntimin]

         return menogol              

print(media_gol_partite(tupla_partite))
print(media_gol_squadra(tupla_partite,"Barcellona"))
print(partita_con_più_gol(tupla_partite,))
print(partita_con_meno_gol(tupla_partite))
        

         
 


             
             

 

    


