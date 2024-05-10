# Title
title = " SNAPCHAT LIST IN PYTHON "
title2 = title.center(35, "-")
print("-" * 35)
print(title2)
print("-" * 35)


# Admins Names

Admins = ['Alaowi556' , 'baga1' , 'uutt654' , 'rota89' , 'ciciic55']

# Users Names

Users = ['vngm' , 'Tamer' , 'yasin' , 'Riro' , 'samer']

# app

print(' ') # specing
print(' ') # specing

name = input('Write your Name : ').strip().capitalize()

if len(name) > 0 and name not in Users and name not in Admins: 
    print('You are not in this group')

elif len(name) > 0:

    if name in Admins :
        print('You Are Admin')
        Admin__option = input('Write edit to edit your admin name.\
        \n Or delete to delete your name from admin : ').strip().lower()

        # Update option
        if Admin__option == 'edit':
            newname = input('Write the new name : ').strip().capitalize()
            Admins[Admins.index(name)] = newname
            print(Admins)


        # Delete option
        elif Admin__option == "delete":
            Admins.remove(name)
            print(Admins)
            print("Deleted name succes")




        # Invalide option
        else : 
            print('Invalide option .')


    elif name in Users:

        print('You Are User')

        User__option = input('Write \'quit\' to quit this group.\
        \n Or \'view\' to see all users : ').strip().lower()

        # quit option
        if User__option == "quit":
            Users.remove(name)
            print(Users)
            print('your name was removed')

        elif User__option == "view":

            view = f"""

                ################
                ####  Users  ###
                ################

                {print(Users)}


            """

        # invalide option
        else : 

            print('Invalide option .')


# Invalide Name


else :
    print('Error in writing the name or you are not in this group ')