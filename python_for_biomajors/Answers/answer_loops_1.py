'''
read in the a line of genetic code 3 nucleotides at a time
print the codon along with the number of condons
exit the loop as soon as a stop codon is located (TAG)

'''
DNA = "GCTTGACCACGATGACTAGATACGTAGCTGAGAGGAGAGTT"
length = len(DNA)
for i in range(0,length-3):
    if(DNA2[i:i+3]=="TAG"):
        print("reached:",DNA2[i:i+3]," stopping at codon", math.ceil(i/3))
        break
    else:
        if(i%3==0):
            print(DNA[i:i+3],i)
        
