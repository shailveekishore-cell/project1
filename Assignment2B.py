# Class: CSE 1321L
# Section:BW3
# Term:Fall Semester 2026
# Instructor:Akash Keshav Bharati
# Name:Shailvee Kishore
# Assigment 2
print("[Owl Airlines - Checked Bag Kiosk]")
while True:
    member = input("Are you a Hooty Hoo Preferred Member? (Y/N): ")

    if member == "Y":
        print("Welcome, and thank you for being a Hooty Hoo Preferred Member")
        print("As a perk for being awesome, your first 2 checked bags are free")
        print("Additional bags are $35.00 each")
    else:
        print("Checked Bag rates:")
        print("- First Checked bag: $35.00")
        print("- Second Checked bag: $50.00")
        print("- Third+ Checked bag: $150.00 each")

    print()
    checkingbags = input("Are you checking any bags? (Y/N): ")

    if checkingbags == "Y":
        numbags = int(input("How many bags are you checking in?: "))
        print()
        totalfee = 0.0

        if member == "Y":
            print("As a Hooty Hoo Preferred Member your first 2 bags are complimentary.")
            if numbags > 2:
                totalfee = (numbags - 2) * 35.00
                print(f"Checked Bag fees to pay: ${totalfee:.2f}")
        else:
            if numbags == 1:
                totalfee = 35.00
            elif numbags == 2:
                totalfee = 35.00 + 50.00
            elif numbags >= 3:
                totalfee = 35.00 + 50.00 + ((numbags - 2) * 150.00)

            print(f"Checked Bag fees to pay: ${totalfee:.2f}")

        print()

    if member == "Y":
        print("Have a safe flight and thank you for being a Hooty Hoo Preferred Member")
        print()
    elif checkingbags != "Y":
        print()

