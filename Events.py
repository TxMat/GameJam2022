import random


class Events():
    def __init__(self):
        self.name = ""
        self.description = ""
        self.type = ""
        # self.scene = ???


    def action(self,expedition):
        pass

class ritual(Events):
    def __init__(self):
        super().__init__()
        self.type="ritual"

class satanique(ritual):
    def __init__(self):
        super().__init__()
        self.name ="satanique"
        self.description = "ne peux plus pondre, buff de stats"

    def action(self,cock):
        # ne peux plus pondre, buff de stats
        cock.fertile = False
        cock.intelligence = cock.intelligence*2,
        cock.strength =  cock.strength*2,
        cock.stamina = cock.stamina*2,

class goy_ish(ritual):
    def __init__(self):
        super().__init__()
        self.name ="goy_ish"
        self.description = "plus de luck"

    def action(self,cock):
        # plus de luck
        pass

class cursed(ritual):
    def __init__(self):
        super().__init__()
        self.name ="cursed"
        self.description = "creuse une tombe, meurt dans 3 jours"

    def action(self,cock):
        # creuse une tombe, meurt dans 3 jours
        pass

 
        
class gaz(Events):
    def __init__(self):
        super().__init__()
        self.type="gaz"

class inflammable(gaz):
    def __init__(self):
        super().__init__()
        self.name ="inflammable"
        self.description="peut exploser, arrête l'expédition si triggered"
    
    def action(self,expedition):
        # peut exploser, arrête l'expédition si triggered
        resistance =  False
        for i in expedition.cock_dic:
            for y in i.perks:
                if y == "Perk_protection_fire":
                    resistance = True
        if resistance == False:
            #expedition.stop()
            pass
        

class toxic(gaz):
    def __init__(self):
        super().__init__()
        self.name =""
        self.description="rend les poulets fous, stat aléatoire rendue à 0 pendant X cases"
    
    def action(self,expedition):
        # rend les poulets fous, stat aléatoire rendue à 0 pendant X cases
        resistance =  False
        for i in expedition.cock_dic:
            for y in i.perks:
                if y == "Perk_protection_gaz":
                    resistance = True
        if resistance == False:
            #expedition.stop()
            pass
        pass

class soporifique(gaz):
    def __init__(self):
        super().__init__()
        self.name ="soporifique"
        self.description="endort, arrête l'expédition si non résisté"
    
    def action(self,expedition):
        # endort, arrête l'expédition si non résisté        
        resistance =  False
        for cock in expedition.cock_dic:
            for y in cock.perks:
                if y == "Perk_protection_gaz":
                    resistance = True
        if resistance == False:
            #expedition.stop()
            pass
    
class ore(Events):
    def __init__(self):
        super().__init__()
        self.type="ore"
        self.name= "minerai"

    def action(self,expedition):
        # ajoute une quant random d'un minerai random
        expedition.loot_ores[random.choice(list(expedition.loot_ores))] += random.randint(1,3)


    
class dna(Events):
    def __init__(self):
        super().__init__()
        self.type="dna"
        self.name="trouvaille d'ADN"
  
    def action(self,expedition):
        # ajoute une quant random d'un minerai 
        expedition.loot_dna[random.choice(list(expedition.loot_dna))] += random.randint(1,3)
