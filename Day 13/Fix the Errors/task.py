def input_no():
    try:
        global age
        age = int(input("How old are you?"))
    except ValueError:
        print("You have typed in a an invalid number. PLease try again with a numerical number")
        input_no()

age = 0
input_no()
if age > 18:
    print(f"You can drive at age {age}.")
