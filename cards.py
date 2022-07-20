from tkinter import *
import random 
from PIL import Image, ImageTk


root = Tk()

root.title('Ganeshpokharel.com.np - Card Deck')
root.iconbitmap('arc.png')
root.geometry("1200x800")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
    # Open the image
    our_card_img = Image.open(card)

    # Resize the Image

    our_card_resize_image = our_card_img.resize((150,218))

    #output the card 
    global our_card_image   
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    # Return That Card
    return our_card_image

#Shuffle The Cards
def shuffle():
    # Clear all the old cards from previous Games
    
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')



    # suits = ["पान","इट्टा","चिडी","हुकुम"]
    suits = ["Hearts","Spades","Clubs","Diamonds"]
    #royals = ["J","Q","K","A"]
    values = range(2,15)
    # 11 = jack , 12 = queen....

    global deck 
    deck = []

    for suit in suits :
        for value in values:
            deck.append(f'{value}_of_{suit}')

    #create players
    global dealer,player, dealer_spot, player_spot
    dealer = []
    player = []
    dealer_spot = 0
    player_spot = 0 

    # Shuffle Two Cards for Player and dealer
    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

    

# put no of remaining card in title bar
    root.title(f'Ganeshpokharel.com.np - {len(deck)} Cards left')

def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
            try:
                # Get the Player Card 
                dealer_card = random.choice(deck)
                #remove card from deck 
                deck.remove(dealer_card)
                #Append card to Player List 
                dealer.append(dealer_card)
                #output card screen
                global dealer_image1,dealer_image2,dealer_image3,dealer_image4,dealer_image5

                if dealer_spot == 0:
                    # Resize Card
                    dealer_image1 = resize_cards(f'cards/{dealer_card}.png')
                    # Output Card To Scree
                    dealer_label_1.config(image=dealer_image1)
                    # Increament our player Spot Counter
                    dealer_spot += 1
                elif dealer_spot == 1:
                    # Resize Card
                    dealer_image2 = resize_cards(f'cards/{dealer_card}.png')
                    # Output Card To Scree
                    dealer_label_2.config(image=dealer_image2)
                    # Increament our player Spot Counter
                    dealer_spot += 1   
                elif dealer_spot == 2:
                    # Resize Card
                    dealer_image3 = resize_cards(f'cards/{dealer_card}.png')
                    # Output Card To Scree
                    dealer_label_3.config(image=dealer_image3)
                    # Increament our player Spot Counter
                    dealer_spor += 1
                elif dealer_spot == 3:
                    # Resize Card
                    dealer_image4 = resize_cards(f'cards/{dealer_card}.png')
                    # Output Card To Scree
                    dealer_label_4.config(image=dealer_image4)
                    # Increament our player Spot Counter
                    dealer_spot += 1
                elif dealer_spot == 4:
                    # Resize Card
                    dealer_image5 = resize_cards(f'cards/{dealer_card}.png')
                    # Output Card To Scree
                    dealer_label_5.config(image=dealer_image5)
                    # Increament our player Spot Counter
                    dealer_spot += 1
                

                #put the number of remaining cards in the title bar
                root.title(f'Ganeshpokharel.com.np - {len(deck)} Cards left')

            except:
                root.title(f'Ganesh.com.np - No Cards in Deck !!')

def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            # Get the Player Card 
            player_card = random.choice(deck)
            #remove card from deck 
            deck.remove(player_card)
            #Append card to Player List 
            player.append(player_card)
            #output card screen
            global player_image1,player_image2,player_image3,player_image4,player_image5

            if player_spot == 0:
                # Resize Card
                player_image1 = resize_cards(f'cards/{player_card}.png')
                # Output Card To Scree
                player_label_1.config(image=player_image1)
                # Increament our player Spot Counter
                player_spot += 1
            elif player_spot == 1:
                # Resize Card
                player_image2 = resize_cards(f'cards/{player_card}.png')
                # Output Card To Scree
                player_label_2.config(image=player_image2)
                # Increament our player Spot Counter
                player_spot += 1   
            elif player_spot == 2:
                # Resize Card
                player_image3 = resize_cards(f'cards/{player_card}.png')
                # Output Card To Scree
                player_label_3.config(image=player_image3)
                # Increament our player Spot Counter
                player_spot += 1
            elif player_spot == 3:
                # Resize Card
                player_image4 = resize_cards(f'cards/{player_card}.png')
                # Output Card To Scree
                player_label_4.config(image=player_image4)
                # Increament our player Spot Counter
                player_spot += 1
            elif player_spot == 4:
                # Resize Card
                player_image5 = resize_cards(f'cards/{player_card}.png')
                # Output Card To Scree
                player_label_5.config(image=player_image5)
                # Increament our player Spot Counter
                player_spot += 1
            

            #put the number of remaining cards in the title bar
            root.title(f'Ganeshpokharel.com.np - {len(deck)} Cards left')

        except:
            root.title(f'Ganesh.com.np - No Cards in Deck !!')


# Deal out CArds
def deal_cards():
    
    try:
        # Get the dealer Card
        card = random.choice(deck)
         #remove card from deck 
        deck.remove(card)
        #Append card to Dealer List 
        dealer.append(card)
        #output card screen
        global dealer_image
        dealer_image = resize_cards(f'cards/{card}.png')
        dealer_label.config(image=dealer_image)
       
       
        # Get the Player Card 
        card = random.choice(deck)
        #remove card from deck 
        deck.remove(card)
        #Append card to Player List 
        player.append(card)
        #output card screen
        global player_image
        player_image = resize_cards(f'cards/{card}.png')
        player_label.config(image=player_image)

        #put the number of remaining cards in the title bar
        root.title(f'Ganeshpokharel.com.np - {len(deck)} Cards left')


    except:
        root.title(f'Ganesh.com.np - No Cards in Deck !!')






my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer-Gunners",bd=0)
dealer_frame.grid(row=0,column=0,ipadx=20,padx=10)

player_frame = LabelFrame(my_frame, text="Player-You" , bd=0)
player_frame.grid(row=1,column=0,ipadx=20,padx=10,pady=10 )

# put the cards in the Frame 
dealer_label_1 = Label(dealer_frame,text='')
dealer_label_1.grid(row=0, column=0, padx=20,pady=20)

dealer_label_2 = Label(dealer_frame,text='')
dealer_label_2.grid(row=0, column=1, padx=20,pady=20)

dealer_label_3 = Label(dealer_frame,text='')
dealer_label_3.grid(row=0, column=2, padx=20,pady=20)

dealer_label_4 = Label(dealer_frame,text='')
dealer_label_4.grid(row=0, column=3, padx=20,pady=20)

dealer_label_5 = Label(dealer_frame,text='')
dealer_label_5.grid(row=0, column=4, padx=20,pady=20)


#Create Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1,column=0,pady=20,padx=20)

player_label_2 = Label(player_frame,text='')
player_label_2.grid(row=1,column=1,pady=20,padx=20)

player_label_3 = Label(player_frame,text='')
player_label_3.grid(row=1,column=2,pady=20,padx=20)

player_label_4 = Label(player_frame,text='')
player_label_4.grid(row=1,column=3,pady=20,padx=20)

player_label_5 = Label(player_frame,text='')
player_label_5.grid(row=1,column=4,pady=20,padx=20)

# Create Button Frame
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)


# Create Couple of Buttons 
shuffle_button = Button(button_frame, text="Shuffle Deck ", font = ("Helvetica",14), command=shuffle)
shuffle_button.grid(row=0,column=0)

card_button = Button(button_frame, text="Hit Me!! ", font = ("Helvetica",14), command=player_hit)
card_button.grid(row=0,column=1,padx=10)

stand_button = Button(button_frame, text="Stand ! ", font = ("Helvetica",14))
stand_button.grid(row=0,column=2,padx=10)


shuffle()


root.mainloop()
