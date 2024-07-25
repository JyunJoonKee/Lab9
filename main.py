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

def main():
    while True:
        print("\nMenu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        selection = int(input("\nPlease enter an option: "))
        if selection == 3:
            exit()
        elif selection == 1:
            encodeline = input("Please enter the password to encode: ")
            encodedpassword = encode(encodeline)
            print("Your password has been encoded and stored!")
        elif selection == 2:
            print(f"The encoded password is {decode(encodedpassword)}, and the original password is {encodeline}.")
if __name__ == "__main__":
    main()
