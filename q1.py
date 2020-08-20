print("*****************************************MAIN MENU*****************************************")
print("1. Create Rosters")
print("2. Create Teams")
print("3. Sort Team Members")
print("4. Delete a Team")
print("5. Quit")
print("********************************************************************************************")
students=[]
teams=[]
total=0
while True:
    print("")
    selection = input("Choose from menu: ")
    if selection == "1":
        u_input = input("How many students would you like to enter?")
        while u_input.isdigit()==False:
            u_input=input("Enter valid student number you would like to enter")

        for i in range (int(u_input)):
            user_input=input("Enter student "+str(i+1)+": ")
            students.append(user_input)

        print("Current Roster:")
        for j in range(int(u_input)):
            print(students[j])

    elif selection == "2":
        stu=[]
        u_input1 = input("What is the team size?")
        total = int(u_input)
        temp = int(u_input)%int(u_input1)
        temp1 = (int(u_input))/(int(u_input1))
        if temp != 0:
            temp1 = (int(u_input)-temp)/(int(u_input1)-1)

        for i in range (int(u_input1)):
            stu=[]
            print("Enter students for team "+str(i+1)+": ")
            if total>int(temp1):
                total = total - int(temp1)
                for k in range (int(temp1)):
                    stu.append(input(" "))
                teams.append(stu)
            elif total==int(temp):
                for j in range (temp):
                    stu.append(input(" "))
                teams.append(stu)



    elif selection == "3":
        lSort=[]
        lSortTeam=[]
        for i in range (len(teams)):
            for j in range (len(teams[i])):
                k = teams[i][j].split(" ")
                lSort.append(k[1])
                lSort.sort()
            lSortTeam.append(lSort)
            lSort=[]
        bool = False
        for i in range (len(lSortTeam)):
            for j in range (len(lSortTeam[i])):

                    for b in range (len(teams)):
                        for m in range (len(teams[b])):
                            z = teams[b][m].split(" ")
                            if lSortTeam[i][j] == z[1] and bool == False:
                                print(teams[b][m])
                                bool = True

            bool = False




    elif selection == "4":
        dele = int(input("Which team do you want to delete?"))
        dele=dele-1
        bool = False
        for i in range (len(teams)):
            if dele==i:
                teams.remove(teams[i])
                bool = True
        if bool == False:
            print("Enter valid team number")




    elif selection == "5":
        break
    else:
        print("Invalid selection")
