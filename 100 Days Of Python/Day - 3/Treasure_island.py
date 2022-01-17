# Treasure Island Game


print('''
                                                                                                                                                                                                                                              
I8,        8        ,8I 88888888888 88          ,ad8888ba,   ,ad8888ba,   88b           d88 88888888888    888888888888 ,ad8888ba,      888888888888 88        88 88888888888      ,ad8888ba,        db        88b           d88 88888888888  
`8b       d8b       d8' 88          88         d8"'    `"8b d8"'    `"8b  888b         d888 88                  88     d8"'    `"8b          88      88        88 88              d8"'    `"8b      d88b       888b         d888 88           
 "8,     ,8"8,     ,8"  88          88        d8'          d8'        `8b 88`8b       d8'88 88                  88    d8'        `8b         88      88        88 88             d8'               d8'`8b      88`8b       d8'88 88           
  Y8     8P Y8     8P   88aaaaa     88        88           88          88 88 `8b     d8' 88 88aaaaa             88    88          88         88      88aaaaaaaa88 88aaaaa        88               d8'  `8b     88 `8b     d8' 88 88aaaaa      
  `8b   d8' `8b   d8'   88"""""     88        88           88          88 88  `8b   d8'  88 88"""""             88    88          88         88      88""""""""88 88"""""        88      88888   d8YaaaaY8b    88  `8b   d8'  88 88"""""      
   `8a a8'   `8a a8'    88          88        Y8,          Y8,        ,8P 88   `8b d8'   88 88                  88    Y8,        ,8P         88      88        88 88             Y8,        88  d8""""""""8b   88   `8b d8'   88 88           
    `8a8'     `8a8'     88          88         Y8a.    .a8P Y8a.    .a8P  88    `888'    88 88                  88     Y8a.    .a8P          88      88        88 88              Y8a.    .a88 d8'        `8b  88    `888'    88 88           
     `8'       `8'      88888888888 88888888888 `"Y8888Y"'   `"Y8888Y"'   88     `8'     88 88888888888         88      `"Y8888Y"'           88      88        88 88888888888      `"Y88888P" d8'          `8b 88     `8'     88 88888888888  
                                                                                                                                                                                                                                             
''')
print("Hey! What's your name?")
name = input()
choice = input("Which side you want to go, left or right: ")
if(choice == "left"):
    swim = input(("Hey, there is a river , you want to wait for the boat or want to swim: "))
    if(swim=="wait"):
        door = input(("Which door you will choose, yellow,red or blue: "))
        if(door=="red"):
            print("Crocodile is coming, Game Over!")
        elif(door == "blue"):
            print("The king of Jungle is there, Game Over!")
        else:
            print("You won!")
    else:
        print("River flow is high and is deep!, Game Over!")
else:
    print("Game Over!")
