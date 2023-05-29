from .funding_round import FundingRound
from .venture_capitalist import VentureCapitalist

class Startup:

    all = []

    def __init__(self, name, founder, domain):
        self.name = name
        self.founder = founder
        self._domain = domain 
        type(self).add_to_all_startups(self)

    # Class methods

    @classmethod
    def add_to_all_startups(cls, new_startup):
        if isinstance(new_startup, cls):
            cls.all.append(new_startup)
        else: 
            raise TypeError("New startup must be an instance of Startup")
    
    @classmethod
    def find_by_founder(cls, founder_name):
        for startup in cls.all:
            if startup.founder.lower() == founder_name.lower():
                return startup
        return "No founder by that name"
    
    @classmethod
    def domains(cls):
        return [startup._domain for startup in cls.all]
    
    # Instance methods

    def pivot(self, domain, name):
        setattr(self, "_domain", domain)
        self.name = name
    
    # Associations & Aggregate Methods

    def sign_contract(self, vc, invest_type, amt):
        if not isinstance(vc, VentureCapitalist): 
            raise TypeError("VC must be an instance of VentureCapitalist")
        if type(invest_type) != str: 
            raise TypeError("Investment type must be a string")
        if type(amt) != float:
            raise TypeError("Investment amount must be a float")
        FundingRound(self, vc, invest_type, amt)

    def rounds(self):
        return [fr for fr in FundingRound.all if fr._startup == self]
    
    def num_funding_rounds(self):
        results = self.rounds()
        if results: return len(results)
        return "No funding rounds for that startup"
    
    def total_funds(self):
        funds = [fr.investment for fr in self.rounds()]
        if funds: return sum(funds)
        return "No funds raised for that startup"
    
    def investors(self):
        vcs = {fr._venture_captialist for fr in self.rounds()}
        if vcs: return vcs 
        return "No investors in that startup"

    def big_investors(self):
        big_vcs = {fr._venture_capitalist for fr in self.rounds() 
                    if fr._venture_capitalist.total_worth > 1000000000}
        if big_vcs: return big_vcs
        return "No big investors in that startup"

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
    def founder(self):
        return self._founder 
    
    @founder.setter
    def founder(self, founder):
        if type(founder) == str:
            self._founder = founder
        else: 
            raise TypeError("Founder must be a string")
    
    @property
    def _domain(self):
        return self.__domain
    
    @_domain.setter
    def _domain(self, domain):
        if type(domain) == str: 
            self.__domain = domain
        else: 
            raise TypeError("Domain must be a string")