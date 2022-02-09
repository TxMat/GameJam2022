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
        self.name ="satanique"
        self.description = "ne peux plus pondre, buff de stats"

    def action(self,expedition):
        # ne peux plus pondre, buff de stats
        pass

class goy_ish(ritual):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name ="goy_ish"
        self.description = "plus de luck"

    def action(self,expedition):
        # plus de luck
        pass

class cursed(ritual):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name ="cursed"
        self.description = "creuse une tombe, meurt dans 3 jours"

    def action(self,expedition):
        # creuse une tombe, meurt dans 3 jours
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
        pass

class toxic(gaz):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name =""
        self.description="rend les poulets fous, stat aléatoire rendue à 0 pendant X cases"
    
    def action(self,expedition):
        # rend les poulets fous, stat aléatoire rendue à 0 pendant X cases
        pass

class soporifique(gaz):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.name ="soporifique"
        self.description="endort, arrête l'expédition si non résisté"
    
    def action(self,expedition):
        # endort, arrête l'expédition si non résisté
        pass
    
class ore(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="ore"
        self.name= "minerai"

    def action(self,expedition):
        # ajoute une quant random d'un minerai random
        pass

    
class dna(Events):
    def __init__(self, name = "", description = "", e_type = ""):
        super().__init__()
        self.type="dna"
        self.name="trouvaille d'ADN"
  
    def action(self,expedition):
        # ajoute une quant random d'un minerai random
        pass  
