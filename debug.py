from lib import *


# code here
# e.g.
# Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
#   vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
#   fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )

s1 = Startup("Bubble", "Joshua Haas", "bubble.io")
s2 = Startup("Big Shot", "Someone", "domain.com")
vc1 = VentureCapitalist("Joe Schmo", 500)
vc2 = VentureCapitalist("Jane Doe", 10000000000000000000000000)
fr1 = FundingRound(s1, vc1, "Pre-Seed", 765452456302556)
fr2 = FundingRound(s2,vc2, "Series C", 450600000000000000000)




# do not remove
import ipdb; ipdb.set_trace()
