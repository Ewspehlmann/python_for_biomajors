'''

Loop Exercise: Transform DNA into RNA
 
The string represents DNA coding for the gene VEGFA
Q)Your job is to be RNA polymerase. Convert the DNA into RNA. 
    A)create a dictionary that maps DNA to RNA
        *include '\n':"" into the dictionary, this takes care of linebreaks
    B)Use nested for loop to break the gene into lines then lines into individual chars
    c)store the string in a variable 

'''


textfile = "Data/VEGFA.txt"
gene = open(textfile,"r")
gene.readline()
transcribe=""
DNA_to_RNA = {'G':'C','C':'G','T':'A','A':'U','\n':''} #new line character is pesky 
#String Method
for line in gene: #loops through lines "AGCTAGATGATCTGAT"
    for n in line: #loops through chars 'A' 'G' 'C'.... so on
        transcribe+=DNA_to_RNA[n] #using the character as the key to the dictionary
print(transcribe)


'''
List Method:
Alternate way, arguably slightly faster 
RNA = []
for line in gene:
    for n in line:
        RNA.append(DNA_to_RNA[n])
print("".join(RNA))
'''
