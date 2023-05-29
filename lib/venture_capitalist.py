from .funding_round import FundingRound

class VentureCapitalist:

    all = []
    
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        type(self).add_to_all_vcs(self)
    
    # Class methods
    @classmethod
    def add_to_all_vcs(cls, new_vc):
        if isinstance(new_vc, cls):
            cls.all.append(new_vc)
        else: 
            raise TypeError("New VC must be an instance of Venture Capitalist")
    
    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all 
                if vc.total_worth > 1000000000]

    # Properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str: 
            self._name = name
        else: 
            raise TypeError("Name must be a string")
    
    @property
    def total_worth(self):
        return self._total_worth
    
    @total_worth.setter
    def total_worth(self, total_worth):
        if type(total_worth) == float or type(total_worth) == int:
            self._total_worth = total_worth
        else: 
            raise TypeError("Total worth must be a number")
