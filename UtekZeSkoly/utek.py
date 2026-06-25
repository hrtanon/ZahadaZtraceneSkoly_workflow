
import random
import json




def iniciuj_stav():
    hodnoty={"pozice":"vestibul",
        "inventar":[],
        "stav":True
        }
    return hodnoty



def zmena_pozice(choice,hodnoty:dict[str,any]):

    if hodnoty["pozice"]=="vestibul" and choice== "jdi jih" :
        hodnoty["pozice"]="ucebna"

    elif hodnoty["pozice"]=="vestibul" and choice== "jdi zapad" :
        hodnoty["pozice"]="kabinet"
        
    elif hodnoty["pozice"]=="ucebna" and choice== "jdi sever" :
        hodnoty["pozice"]="vestibul"
        print()

    elif hodnoty["pozice"]=="kabinet" and choice== "jdi vychod" :
        hodnoty["pozice"]="vestibul"
    

def komunikace(path):
    pass
    with open(path,"r", encoding="utf-8")as f:
        data=json.load(f)
        hlaska=random.choice[data]
        return f"{hlaska}"

def vypis_popis(hodnoty:dict[str,any]) -> None:
    """Vypíše do terminálu textový popis aktuální místnosti a možností.

    Args:
        stav: Slovník s aktuálním stavem hry.
    """
    mistnost = hodnoty["pozice"]
    
    if mistnost == "vestibul":
        print("\nStojíš ve vestibulu školy. Hlavní dveře ven jsou zamčené.")
        print("Můžeš jít na sever (kabinet) nebo na západ (učebna).")
        
    elif mistnost == "ucebna":
        print("\nPřesunul ses do učebny. Na katedře leží rezavý klíč.")
        print("Můžeš jít na východ (vestibul).")
        
    elif mistnost == "kabinet":
        print("\nJsi v kabinetu. Na tabuli je napsáno: Klíč je v učebně.")
        print("Můžeš jít na jih (vestibul).")





def choice(hodnoty:dict[str,any]):
    while True:
        try:
            choice=str(input("zadej volbu")).lower().strip()
            
            if choice=="jdi sever":
                zmena_pozice(choice,hodnoty)
                return choice

            elif choice=="jdi jih":
                zmena_pozice(choice,hodnoty)
                return choice


            elif choice=="jdi vychod":
                zmena_pozice(choice,hodnoty)
                return choice



            elif choice=="jdi zapad":
                zmena_pozice(choice,hodnoty)
                return choice
            
            elif choice=="seber klic":
                akce(choice,hodnoty)

            elif choice=="pouuzi klic":
                akce(choice,hodnoty)

            elif choice=="konec":
                hodnoty["stav"]=False
                return
        except ValueError:
            continue


def inventar(hodnoty:dict[str,any]):
    hodnoty["inventar"]= "klíc"
    print("sebral jsi klic")
    return hodnoty

def akce(choice,hodnoty):
    if choice=="pouzit klic" and hodnoty["pozice"]=="vestibul":
        hodnoty["stav"]=False
    elif choice=="seber klic" and hodnoty["pozice"]=="ucebna":
        inventar(hodnoty)
    else :
        return None
    



def game_loop():
    hodnoty=iniciuj_stav()
    while hodnoty["stav"]==True:
        
        vypis_popis(hodnoty)
        chice=choice(hodnoty)
        akce(chice,hodnoty)
        
        


game_loop()

