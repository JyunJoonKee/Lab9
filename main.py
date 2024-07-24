#Thomas's Main File

def encode(password):
    threestring = ""
    listofnumbers = list(password)
    for nums in range(len(listofnumbers)):
        addnum = int(listofnumbers[nums]) + 3
        if addnum>=10:
            addnum=addnum-10
        threestring += str(addnum)
    return threestring
#Alexa's Decoding
def decode(password):
    substring=''
    listnum=list(password)
    for i in range (len(listnum)):
        sub=int(listnum[i])-3
        if sub<0:
            sub=sub+10
        substring= substring+str(sub)
    return substring
