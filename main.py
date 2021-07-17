import json
jsonfile = json.load(open("datafile.json"))

Val = True
while Val == True:
    word = input("Enter The Word : ")
   
    def check(para):
        para = para.lower()
        if para in jsonfile:
            return jsonfile[para]
        else:
            return "Please Enter Correct Word"

    print(check(word))
   
    again = input("Continue ? 'y' or 'n' : ")
   
    if again.lower() == 'n':
        Val = False


