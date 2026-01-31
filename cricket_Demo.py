import string
import random
import time


print("\n\n\t\t\t\t##################################")
print("\t\t\t\t🏏Welcome To this Cricket match🏏")
print("\t\t\t\t##################################\n\n\n")

TeamA_input=input(f"Enter Team A: ")
TeamB_input=input(f"Enter Team B: ")

toss=random.randint(1,6)
if toss%2==0:
    TeamA=TeamA_input
    TeamB=TeamB_input
    choice=random.randint(1,2)
    if choice==1:
        print(f"\n{TeamA} choose to Bat first\n")
    else:
        print(f"\n{TeamB} choose to Bowl first\n")
    Total_score_A = 0
    Total_score_B = 0
    Turn_Finish = True
    Ball = True
    ball = int(0)
    Total_Out = int(0)
    print("\n\nPlayer Name                  Run")
    print("_________________________________\n")
    while Turn_Finish and Ball:
        """this part is to generate player first name and last name"""
        first_name = random.randint(3, 6)
        last_name = random.randint(3, 6)
        player_f_name = ""
        player_l_name = ""
        for i in range(first_name):
            y = random.choice(string.ascii_uppercase)
            player_f_name += y
        for i in range(last_name):
            x = random.choice(string.ascii_uppercase)
            player_l_name += x
        player = player_f_name + ' ' + player_l_name
        """this part is to generate player first name and last name"""
        """this part is to generate player individual runs"""
        player_run = int(0)
        Not_Out = True
        while Not_Out:
            run = random.randint(3, 8)
            ball += 3
            if run <= 6:
                player_run = player_run + run
            else:
                player_name_length = len(player)
                """This part is to print player run after out in 1 sec delay"""
                if player_name_length == 13:
                    print(f"\r{Total_Out + 1}| {player}               {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 12:
                    print(f"{Total_Out + 1}| {player}                {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 11:
                    print(f"{Total_Out + 1}| {player}                 {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 10:
                    print(f"{Total_Out + 1}| {player}                  {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 9:
                    print(f"{Total_Out + 1}| {player}                   {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 8:
                    print(f"{Total_Out + 1}| {player}                    {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 7:
                    print(f"{Total_Out + 1}| {player}                     {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 6:
                    print(f"{Total_Out + 1}| {player}                      {player_run}\n", end="", flush=True)
                    time.sleep(2)
                """This part is to print player run after out in 1 sec delay"""
                Not_Out = False
                Total_Out += 1
        """this part is to generate player individual runs"""
        """this part is to check team overall score and out"""
        Total_score_A += player_run
        if Total_Out > 10 or ball >= 120:
            Ball = False
            Turn_Finish = False

        """this part is to check team overall score and out"""
    print(f"\nTotal Score of {TeamA}: {Total_score_A}/{Total_Out - 1}\n")

    print(f"Target for {TeamB} is {Total_score_A+1}")

    Turn_Finish = True
    Ball = True
    ball = int(0)
    Total_Out = int(0)
    print("\n\nPlayer Name                  Run")
    print("_________________________________\n")
    while Turn_Finish and Ball:
        """this part is to generate player first name and last name"""
        first_name = random.randint(3, 6)
        last_name = random.randint(3, 6)
        player_f_name = ""
        player_l_name = ""
        for i in range(first_name):
            y = random.choice(string.ascii_uppercase)
            player_f_name += y
        for i in range(last_name):
            x = random.choice(string.ascii_uppercase)
            player_l_name += x
        player = player_f_name + ' ' + player_l_name
        """this part is to generate player first name and last name"""
        """this part is to generate player individual runs"""
        player_run = int(0)
        Not_Out = True
        while Not_Out and Total_score_B <= Total_score_A:
            run = random.randint(3, 7)
            ball += 3
            if run <= 6:
                player_run = player_run + run
            else:
                player_name_length = len(player)
                """This part is to print player run after out in 1 sec delay"""
                if player_name_length == 13:
                    print(f"\r{Total_Out + 1}| {player}               {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 12:
                    print(f"{Total_Out + 1}| {player}                {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 11:
                    print(f"{Total_Out + 1}| {player}                 {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 10:
                    print(f"{Total_Out + 1}| {player}                  {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 9:
                    print(f"{Total_Out + 1}| {player}                   {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 8:
                    print(f"{Total_Out + 1}| {player}                    {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 7:
                    print(f"{Total_Out + 1}| {player}                     {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 6:
                    print(f"{Total_Out + 1}| {player}                      {player_run}\n", end="", flush=True)
                    time.sleep(2)
                """This part is to print player run after out in 1 sec delay"""
                Not_Out = False
                Total_Out += 1
        """this part is to generate player individual runs"""
        """this part is to check team overall score and out"""
        Total_score_B += player_run
        if Total_Out > 10 or ball >= 120 or Total_score_B >= Total_score_A:
            Ball = False
            Turn_Finish = False

        """this part is to check team overall score and out"""
    print(f"Total Score of {TeamB}: {Total_score_B}/{Total_Out - 1}")

    if Total_score_A > Total_score_B:
        print(f"{TeamA} Win")
    else:
        print(f"{TeamB} Win")


else:
    TeamB=TeamB_input
    TeamA=TeamA_input

    choice=random.randint(1,2)
    if choice == 1:
        print(f"\n{TeamB} choose to Bat first\n")
    else:
        print(f"\n{TeamA} choose to Bowl first\n")

    Total_score_A=0
    Total_score_B=0
    Turn_Finish=True
    Ball=True
    ball=int(0)
    Total_Out=int(0)
    print("\n\nPlayer Name                  Run")
    print("_________________________________\n")
    while Turn_Finish and Ball:
        """this part is to generate player first name and last name"""
        first_name=random.randint(3,6)
        last_name=random.randint(3,6)
        player_f_name=""
        player_l_name=""
        for i in range(first_name):
            y = random.choice(string.ascii_uppercase)
            player_f_name+=y
        for i in range(last_name):
            x = random.choice(string.ascii_uppercase)
            player_l_name+=x
        player=player_f_name+' '+player_l_name
        """this part is to generate player first name and last name"""
        """this part is to generate player individual runs"""
        player_run=int(0)
        Not_Out=True
        while Not_Out:
            run = random.randint(3, 8)
            ball+=3
            if run<=6:
                player_run=player_run+run
            else:
                player_name_length = len(player)
                """This part is to print player run after out in 1 sec delay"""
                if player_name_length == 13:
                    print(f"\r{Total_Out + 1}| {player}               {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 12:
                    print(f"{Total_Out + 1}| {player}                {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 11:
                    print(f"{Total_Out + 1}| {player}                 {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 10:
                    print(f"{Total_Out + 1}| {player}                  {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 9:
                    print(f"{Total_Out + 1}| {player}                   {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 8:
                    print(f"{Total_Out + 1}| {player}                    {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 7:
                    print(f"{Total_Out + 1}| {player}                     {player_run}\n",end="",flush=True)
                    time.sleep(2)
                elif player_name_length == 6:
                    print(f"{Total_Out + 1}| {player}                      {player_run}\n",end="",flush=True)
                    time.sleep(2)
                """This part is to print player run after out in 1 sec delay"""
                Not_Out=False
                Total_Out+=1
        """this part is to generate player individual runs"""
        """this part is to check team overall score and out"""
        Total_score_B += player_run
        if Total_Out>10 or ball>=120:
            Ball=False
            Turn_Finish=False

        """this part is to check team overall score and out"""
    print(f"\nTotal Score of {TeamB}: {Total_score_B}/{Total_Out-1}\n")

    print(f"Target for {TeamA} is {Total_score_B+1}")


    Turn_Finish=True
    Ball=True
    ball=int(0)
    Total_Out=int(0)
    print("\n\nPlayer Name                  Run")
    print("_________________________________\n")
    while Turn_Finish and Ball:
        """this part is to generate player first name and last name"""
        first_name=random.randint(3,6)
        last_name=random.randint(3,6)
        player_f_name=""
        player_l_name=""
        for i in range(first_name):
            y = random.choice(string.ascii_uppercase)
            player_f_name+=y
        for i in range(last_name):
            x = random.choice(string.ascii_uppercase)
            player_l_name+=x
        player=player_f_name+' '+player_l_name
        """this part is to generate player first name and last name"""
        """this part is to generate player individual runs"""
        player_run=int(0)
        Not_Out=True
        while Not_Out and Total_score_A<=Total_score_B:
            run = random.randint(3, 7)
            ball+=3
            if run<=6:
                player_run=player_run+run
            else:
                player_name_length=len(player)
                """This part is to print player run after out in 1 sec delay"""
                if player_name_length == 13:
                    print(f"\r{Total_Out + 1}| {player}               {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 12:
                    print(f"{Total_Out + 1}| {player}                {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 11:
                    print(f"{Total_Out + 1}| {player}                 {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 10:
                    print(f"{Total_Out + 1}| {player}                  {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 9:
                    print(f"{Total_Out + 1}| {player}                   {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 8:
                    print(f"{Total_Out + 1}| {player}                    {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 7:
                    print(f"{Total_Out + 1}| {player}                     {player_run}\n", end="", flush=True)
                    time.sleep(2)
                elif player_name_length == 6:
                    print(f"{Total_Out + 1}| {player}                      {player_run}\n", end="", flush=True)
                    time.sleep(2)
                """This part is to print player run after out in 1 sec delay"""
                Not_Out=False
                Total_Out+=1
        """this part is to generate player individual runs"""
        """this part is to check team overall score and out"""
        Total_score_A += player_run
        if Total_Out>10 or ball>=120 or Total_score_A>=Total_score_B:
            Ball=False
            Turn_Finish=False

        """this part is to check team overall score and out"""
    print(f"Total Score of {TeamA}: {Total_score_A}/{Total_Out-1}")

    if Total_score_A>Total_score_B:
        print(f"{TeamA} Win")
    else:
        print(f"{TeamB} Win")