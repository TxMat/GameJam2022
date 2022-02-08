class Level():
    def __init__(self,
                name: str,
                background_img = None,
                icon = None,
                ore_list: list = [],
                dna_list: list = [],
                encounters_list: list = [],
                description: str = "Rien a voir ici",
                danger_lvl: int = 1,
                average_length: int = 5,
                requirement: int = 0):
        self.name = name
        self.bg = background_img
        self.ico = icon
        self.ores = ore_list
        self.enc = encounters_list
        self.desc = descriptio,
        self.danger = danger_lvl
        self.av_len = average_length
        self.req = requirement
