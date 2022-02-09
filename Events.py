import random


class Events():
    def __init__(self, name = "", description = "", e_type = ""):
        self.name = name
        self.description = description
        self.e_type = e_type
        # self.scene = ???


    def action(self,expedition):
        pass

class ritual(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="ritual"
        self.int_mod = 0
        self.int_mult = 1
        self.str_mod = 0
        self.str_mult = 1
        self.sta_mod = 0
        self.sta_mult = 1

class satanique(ritual):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.int_mult = 2        
        self.str_mult = 2       
        self.sta_mult = 2

        self.name ="satanique"
        self.description = "ne peux plus pondre, buff de stats"

    def action(self,cock):
        # ne peux plus pondre, buff de stats
        cock.fertile = False

class luck_up(ritual):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.int_mult = 4  
        self.name ="luck up"
        self.description = "plus de luck"

    def action(self,cock):
        # plus de luck
        pass

class cursed(ritual):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.int_mult = 0.5      
        self.str_mult = 0.5      
        self.sta_mult = 0.5
        self.name ="cursed"
        self.description = "creuse une tombe, baisse les stats"

    def action(self,cock):
        # creuse une tombe,  baisse les stats
        
        pass

 
        
class gaz(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="gaz"

class inflammable(gaz):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name ="inflammable"
        self.description="peut exploser, arrête l'expédition si triggered"
    
    def action(self,expedition):
        # peut exploser, arrête l'expédition si triggered
        resistance =  False
        for i in expedition.cock_dic.values():
            for y in i.perks:
                if y == "fireproof":
                    resistance = True
        if resistance == False:
            expedition.end()
        

class toxic(gaz):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name =""
        self.description="rend les poulets fous, stat aléatoire rendue à 0 pendant X cases"
    
    def action(self,expedition):
        # rend les poulets fous, stat aléatoire rendue à 0 pendant X cases
        resistance =  False
        for i in expedition.cock_dic.values():
            for y in i.perks:
                if y == "gasproof":
                    resistance = True
        if resistance == False:
            expedition.end()

class soporifique(gaz):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name ="soporifique"
        self.description="endort, arrête l'expédition si non résisté"
    
    def action(self,expedition):
        # endort, arrête l'expédition si non résisté        
        resistance =  False
        for cock in expedition.cock_dic.values():
            for y in cock.perks:
                if y == "gasproof":
                    resistance = True
        if resistance == False:
            expedition.end()
            pass
    
class ore(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="ore"
        self.name= "minerai"

    def action(self,expedition):
        # ajoute une quant random d'un minerai random
        expedition.loot_ores[random.choice(list(expedition.loot_ores))] += random.randint(1,20)
    
class dna(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="dna"
        self.name="trouvaille d'ADN"
  
    def action(self,expedition):
        # ajoute une quant random d'un minerai 
        expedition.loot_dna[random.choice(list(expedition.loot_dna))] += random.randint(1,3)
