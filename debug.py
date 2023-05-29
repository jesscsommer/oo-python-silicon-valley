from lib import *


# code here
# e.g.
# Startup( 'Pied Piper', 'Richard Hendricks', 'www.pp.com' )
#   vc1 = VentureCapitalist( 'Peter Gregory', 100000000 )
#   fr1 = FundingRound( s1, vc1, 'Pre-Seed', 200000.99 )

s1 = Startup("Bubble", "Joshua Haas", "bubble.io")
s2 = Startup("Big Shot", "Someone", "domain.com")
s3 = Startup("Next Big Thing", "Jenny", "nextbig.thing")

vc1 = VentureCapitalist("Joe Schmo", 500)
vc2 = VentureCapitalist("Jane Doe", 10000000000000000000000000)
vc3 = VentureCapitalist("Nobody", 5)

fr1 = FundingRound(s1, vc1, "Pre-Seed", 765452456302556)
fr2 = FundingRound(s2,vc2, "Series C", 450600000000000000000)

s1.sign_contract(vc2, "Series B", 450.50)

s1_rounds = s1.num_funding_rounds()
s3_rounds = s3.num_funding_rounds()

s1_funds = s1.total_funds()
s3_funds = s3.total_funds()

s1_big = s1.big_investors()
s3_big = s3.big_investors()

vc1_contract = vc1.offer_contract(s2, "Series C", 575.75)

vc1_rounds = vc1.funding_rounds()
vc1_portfolio = vc1.portfolio()
vc1_biggest = vc1.biggest_investment()
vc1_domain = vc1.invested("domain.com")

vc3_rounds = vc3.funding_rounds()
vc3_portfolio = vc3.portfolio()
vc3_biggest = vc3.biggest_investment()
vc3_domain = vc3.invested("domain.com")


# do not remove
import ipdb; ipdb.set_trace()
