from Day3.Claim import Claim
from Day3.Diplomat import Diplomat
from utils.FileReader import FileReader

list_of_claims_scheme = FileReader.read('../sources/day3.txt')

list_of_claims = [Claim.parse(claim) for claim in list_of_claims_scheme]

diplomate = Diplomat(list_of_claims)
print(diplomate.number_of_conflicts())
