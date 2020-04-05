rna = ''
DNA_to_RNA = {'G':'C','C':'G','T':'A','A':'U','\n':'','N':'N'} #N added because HERC2 has unknown bases 
with open('Data/HERC2.txt','r') as HERC2:
    HERC2.readline() #removes header 
    for line in HERC2:
        for nucleotide in line:
            rna = rna+ DNA_to_RNA[nucleotide]
    with open('Data/HERC2_RNA.txt','a') as HERC2_RNA: # using A to demonstrate Append mode 
        HERC2_RNA.writelines(rna)