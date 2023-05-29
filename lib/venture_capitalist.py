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
    
    # Associations & Aggregate Methods
    
    def offer_contract(self, startup, invest_type, amt): 
        from .startup import Startup
        if not isinstance(startup, Startup): 
            raise TypeError("Startup must be an instance of Startup")
        if type(invest_type) != str: 
            raise TypeError("Investment type must be a string")
        if type(amt) != float:
            raise TypeError("Investment amount must be a float")
        FundingRound(startup, self, invest_type, amt)
    
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr._venture_capitalist == self]

    def portfolio(self):
        if self.funding_rounds(): 
            return {fr._startup for fr in self.funding_rounds()}
        return "This VC has not funded any startups yet"
    
    def biggest_investment(self):
        if self.funding_rounds():
            largest = self.funding_rounds()[0]
            for fr in self.funding_rounds():
                if fr.investment > largest.investment: 
                    largest = fr 
            return largest 
        return "No investments yet"
    
    def invested(self, domain):
        results = [fr.investment for fr in self.funding_rounds() 
                    if fr._startup._domain.lower() == domain.lower()]
        if results: return sum(results)
        return "Nothing invested in that domain"
    

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
