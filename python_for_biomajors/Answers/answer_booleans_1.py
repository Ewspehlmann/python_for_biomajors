'''
BMI = Weight(KG)/Height(M)^2
convert np array into bmi then use boolean expressions to show
weather someone is under,normal, or over
lets use these arbitrary classifications 
under = BMI<20
Normal = BMI>20 | BMI <30
Over = BMI >30 

Loop through your list printing the BMI and printing its classification

'''

heightCM = np.array([172,180,150,190,200]) # use these numbers to calculate the BMI
KG = np.array([70,98,75,100,70])

BMI  = KG/(heightCM*.01)**2

for x in BMI:
    x = round(x)
    if(x<=20):
        print(str(x)+" = UnderWeight")
    elif(x>20 and x <= 30):
        print(str(x)+" = Healthy")
    elif(x>30):
        print(str(x)+" = OverWeight")