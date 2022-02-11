class Perks():
    def __init__(self,
                 name: str = "",
                 icon=None,
                 tier: int = 1,
                 description: str = "",
                 int_mod: int = 0,
                 int_mult: float = 1,
                 str_mod: int = 0,
                 str_mult: float = 1,
                 sta_mod: int = 0,
                 sta_mult: float = 1):
        self.name = name
        self.ico = icon
        self.tier = tier
        self.desc = description
        self.int_mod = int_mod
        self.int_mult = int_mult
        self.str_mod = str_mod
        self.str_mult = str_mult
        self.sta_mod = sta_mod
        self.sta_mult = sta_mult

    def action(self, cock) -> None:
        # overridden by each perk
        pass


class IronStomach(Perks):
    def __init__(self, description=""):
        super().__init__(name="iron stomach")
        self.description = description

    def action(self, cock) -> None:
        cock.max_hunger = 300


def gen_perks():
    perks = {}
    perks["danger_radar"] = Perks(name="danger radar", description="Vous etes alerte aux dangers")
    perks["glass_cannon"] = Perks(name="glass cannon", str_mult=5, sta_mult=0.2,
                                  description="Tres fort, mais tres fragile")
    perks["gold_radar"] = Perks(name="gold radar", description="Plus de minerais")
    perks["red_herring"] = Perks(name="???", description="Ca a peut-etre un effet, qui sait.")
    perks["the_answer"] = Perks(name="??!", description="Ca a probablement un effet, qui sait")
    perks["iron_stomach"] = IronStomach(description="Vous pouvez manger plus")
    perks["light_up"] = Perks(name="light up", int_mult=1.5, int_mod=20, description="Vous voyez mieux dans les mines")
    perks["fireproof"] = Perks(name="fireproof", description="Vous etes ignifuge")
    perks["gasproof"] = Perks(name="gasproof", description="Vous etes insensible au gaz")
    perks["breathless"] = Perks(name="breathless", description="Vous n'avez pas besoin de respirer")
    perks["rats"] = Perks(name="rats", int_mod=10, description="Des rats vous aide")
    perks["saving_grace"] = Perks(name="1up", description="Vous avez droit a une seconde chance")
    perks["tentacle"] = Perks(name="tentacle", str_mult=1.5, str_mod=20,
                              description="Vos tentacules vous aide a porter plus")
    perks["worm"] = Perks(name="worm", int_mod=10, sta_mult=1.5, sta_mod=20, description="Des vers vous aide")
    return perks
