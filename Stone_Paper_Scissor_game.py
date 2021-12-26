# Hello everyone welcome to the game

welcome = '''
 _    _        _                                  _             _    _                                             
| |  | |      | |                                | |           | |  | |                                            
| |  | |  ___ | |  ___   ___   _ __ ___    ___   | |_   ___    | |_ | |__    ___     __ _   __ _  _ __ ___    ___  
| |/\| | / _ \| | / __| / _ \ | '_ ` _ \  / _ \  | __| / _ \   | __|| '_ \  / _ \   / _` | / _` || '_ ` _ \  / _ \ 
\  /\  /|  __/| || (__ | (_) || | | | | ||  __/  | |_ | (_) |  | |_ | | | ||  __/  | (_| || (_| || | | | | ||  __/ 
 \/  \/  \___||_| \___| \___/ |_| |_| |_| \___|   \__| \___/    \__||_| |_| \___|   \__, | \__,_||_| |_| |_| \___| 
                                                                                     __/ |                         
                                                                                    |___/                          

'''

e = """
     ____ __                      ___                           ____      _                    
  / __// /_ ___   ___  ___     / _ \ ___ _ ___  ___  ____    / __/____ (_)___  ___ ___   ____
 _\ \ / __// _ \ / _ \/ -_)   / ___// _ `// _ \/ -_)/ __/   _\ \ / __// /(_-< (_-</ _ \ / __/
/___/ \__/ \___//_//_/\__/   /_/    \_,_// .__/\__//_/     /___/ \__//_//___//___/\___//_/   
                                        /_/                                                                                                                                                                                                                                                                                                                                             
"""
print(welcome, "\n", e)
import random
stone ="""
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissor ="""
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
final = [stone,paper,scissor]

l = len(final)

while True:
    ask = input('Do you want to play the game type \'y\' for yes and \'n\' for no : ')
    if ask == 'y':
        comp = random.randint(0, 2)
        user = int(input("What do you choose? Type 0 for stone,1 for paper or 2 for scissor. : "))
        if user <= 2:
            print("user choice", final[user])
            print("comp choice", final[comp])
            if user == 1 and comp == 1:
                print("user choosed paper and computer choosed paper")
                print("Nobody won game draw")
            elif user == 1 and comp == 0:
                print("user choosed paper and computer choosed stone")
                print("user won")
            elif user == 1 and comp == 2:
                print("user choosed paper and computer choosed scissor")
                print("computer won")
            elif user == 0 and comp == 0:
                print("user choosed stone and computer choosed stone")
                print("Nobody won game draw")
            elif user == 0 and comp == 1:
                print("user choosed stone and computer choosed paper")
                print("computer won")
            elif user == 0 and comp == 2:
                print("user choosed stone and computer choosed scissor")
                print("you won")
            elif user == 2 and comp == 2:
                print("user choosed scissor and computer choosed scissor")
                print("Nobody won game draw")
            elif user == 2 and comp == 1:
                print("user choosed scissor and computer choosed paper")
                print("user won")
            elif user == 2 and comp == 0:
                print("user choosed scissor and computer choosed stone")
                print("computer won")
            else:
                print("try again")
        else:
            print("invalid number")

    else:
        print('bye bye')
        break