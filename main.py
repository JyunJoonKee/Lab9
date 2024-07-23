#Thomas's Main File

def encode(password):
    threestring = ""
    listofnumbers = list(password)
    for nums in range(len(listofnumbers)):
        addnum = int(listofnumbers[nums]) + 3
        threestring += str(addnum)
    return threestring
