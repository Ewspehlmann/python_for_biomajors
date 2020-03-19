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
gene = open(textfile,"r") #opening file in read mode
gene.readline()
transcribe=""
DNA_to_RNA = {'G':'C','':'','':'','':'','\n':''} #hint

#for loop time
#loops through lines "AGCTAGATGATCTGAT"
#loops through chars 'A' 'G' 'C'.... so on
#using the character as the key to the dictionary


