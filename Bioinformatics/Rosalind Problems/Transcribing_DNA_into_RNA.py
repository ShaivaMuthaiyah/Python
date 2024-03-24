# sample input
seq = "CGTTTTTCTATGCTTTACCCAACCTTACTAGGTACAGAACGTCGATGGCTGGATACTTCCCAGCCATAAGGACATAGCCACCATCGTACAGTGCCTTGCGCCGCCCATTGTCTGATGAGCAGCAGAGATACTCCAGTTCGTGTCCTGACACCGTCGCTCCGGTACCTTCACTTAGAACACTATGTAGCTCACCCTTTCCCTTCAAGCATAAGGGTCCGTTAATTGTGAAGTTGAGGATAGAGACTGAGCGTCCTAGTGTCGTGAAAGCAGTATTGGATTTGTTCTCTCAATAGTGCTATGAGCGTCATAAGTTGGAAAACGCAAAAAATCTTCTACGAAGCGGACGTAGCCGTTCCCATTGGCCCTGACCTCGGTGGGCTGCGCGCTCCTATCATGACGGACTCTTTGCTAATCCTTCTCAGACGCGTCTCACCGCGGCCATTCCCAACGATGTCGGGGCGTGGGACTAATGAAAGTAACATGCGGGATGAAAAAAAGTATTAGAATTTGTGCAGGTGGAGGAATCACATATGTCTATCGATATGTGGGAAGACTAATCACTTTTAGGTCGGAGCATAGTGATAGAAGAGAACGATGGGTTATATAATAAGGAATGATCTTATGGTAACTCTTTAAGTAGCTAAGCCGCTGTACTTTCATGAACACGTTCAGATGACTAAGTCACATCCTGACTTGATCATAATAGATAAGTACCAGATGAGGCCTTATGCAAATTGGTGTTGGACTTCCGGTGTCCTATTAGTTGGCTAATCTGGAAGGCTCATGGGTCCGGTTCGAATTCGCTCTAGTGTGAGAATTCTGCTTGAGTTTGGATGTACGTGTCCCAGGAAGACAACGCTGCGTGGTGAGTGAGTGCCCCTGTAACGGGAAGCAAGATGGCG"

# use the inbuilt replace function to replace the T with the U
def transcribeRNA(seq):
  return seq.replace("T", "U")

print(transcribeRNA(seq))

# Output:
# CGUUUUUCUAUGCUUUACCCAACCUUACUAGGUACAGAACGUCGAUGGCUGGAUACUUCCCAGCCAUAAGGACAUAGCCACCAUCGUACAGUGCCUUGCGCCGCCCAUUGUCUGAUGAGCAGCAGAGAUACUCCAGUUCGUGUCCUGACACCGUCGCUCCGGUACCUUCACUUAGAACACUAUGUAGCUCACCCUUUCCCUUCAAGCAUAAGGGUCCGUUAAUUGUGAAGUUGAGGAUAGAGACUGAGCGUCCUAGUGUCGUGAAAGCAGUAUUGGAUUUGUUCUCUCAAUAGUGCUAUGAGCGUCAUAAGUUGGAAAACGCAAAAAAUCUUCUACGAAGCGGACGUAGCCGUUCCCAUUGGCCCUGACCUCGGUGGGCUGCGCGCUCCUAUCAUGACGGACUCUUUGCUAAUCCUUCUCAGACGCGUCUCACCGCGGCCAUUCCCAACGAUGUCGGGGCGUGGGACUAAUGAAAGUAACAUGCGGGAUGAAAAAAAGUAUUAGAAUUUGUGCAGGUGGAGGAAUCACAUAUGUCUAUCGAUAUGUGGGAAGACUAAUCACUUUUAGGUCGGAGCAUAGUGAUAGAAGAGAACGAUGGGUUAUAUAAUAAGGAAUGAUCUUAUGGUAACUCUUUAAGUAGCUAAGCCGCUGUACUUUCAUGAACACGUUCAGAUGACUAAGUCACAUCCUGACUUGAUCAUAAUAGAUAAGUACCAGAUGAGGCCUUAUGCAAAUUGGUGUUGGACUUCCGGUGUCCUAUUAGUUGGCUAAUCUGGAAGGCUCAUGGGUCCGGUUCGAAUUCGCUCUAGUGUGAGAAUUCUGCUUGAGUUUGGAUGUACGUGUCCCAGGAAGACAACGCUGCGUGGUGAGUGAGUGCCCCUGUAACGGGAAGCAAGAUGGCG