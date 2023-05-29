from .funding_round import FundingRound

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