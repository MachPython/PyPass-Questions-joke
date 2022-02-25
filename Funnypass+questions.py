Correct = True
while Correct:
    pw = input('what is the passsword> ')
    if pw == "gamerga".lower():
        print('you may progress to the questions')
    if pw != "gamer":
      quit('get the **** out no password no service')

    name = input("what is your name? ")
    print("Your name is" + name)
    print("now how about you tell me your home address")
    home_adress = input(">>")
    print(home_adress)

    print('willing to give up your IPv4??? ')
    IPv4 = input('>>')
    print(IPv4)

    print('now i just need your credit card number, CVV, and expiration')
    credit_card = input('>>')
    print('Thank you, we arent saving your info i swear look at the code')
    quit()



