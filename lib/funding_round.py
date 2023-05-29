class FundingRound:
    
    all = []
    
    def __init__(self, startup, vc, round_type, investment):
        self._startup = startup
        self._venture_capitalist = vc
        self.type = round_type
        self.investment = investment
        type(self).add_to_all_rounds(self)

    # Class methods
    @classmethod
    def add_to_all_rounds(cls, new_round):
        if isinstance(new_round, cls):
            cls.all.append(new_round)
        else: 
            raise TypeError("New round must be an instance of Funding Round")

    # Properties 
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, round_type):
        if type(round_type) == str:
            self._type = round_type 
        else: 
            raise TypeError("Type must be a string")
        
    @property
    def investment(self):
        return self._investment
    
    @investment.setter
    def investment(self, investment):
        if type(investment) == int or type(investment) == float:
            self._investment = investment
        else: 
            raise TypeError("Investment must be a number")