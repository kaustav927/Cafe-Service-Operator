tax = 1.13                                             # Tax rate is constant

name = input("Please input your name: ")
bev_type = input("Would you like coffee or tea?: ").lower()
bev_size = input("Please type in your preferred size from small, medium or large: ").lower()
bev_cost = 0
flv_cost = 0

#setting the base price of the beverage based on size alone
if bev_size = ("small" or "s"):
    bev_cost == 1.50
elif bev_size = ("medium" or "m"):
    bev_cost == 2.50
elif bev_size = ("large" or "l"):
    bev_cost == 3.25
else:
    print("Invalid Size")



if bev_type == ("coffee" or "c"):
    flavor = input("Please enter from the following flavours: None, Vanilla, Chocolate or Maple: ").lower()

         if flavor == ("vanilla" or "v"):
            flv_cost = bev_cost + 0.25
            #print("Coffee with Vanilla: $", flv_cost)
         elif flavor == ("chocolate" or "c"):
            flv_cost = bev_cost + 0.75
            #print("Coffee with Chocolate: $", flv_cost)
         elif flavor == ("maple" or "m"):
            flv_cost = bev_cost + 0.50
           # print("Coffee with Maple: $", flv_cost)
         elif flavor == ("none" or "n"):
            flv_cost = bev_cost
            #print("Coffee with no extra flavor: $", flv_cost)
         else:
            print("Invalid Flavor")

#having issues with indentation


elif bev_type == ("tea" or "t"):
    flavor = input("Please enter from the following flavours: None, Lemon or Mint: ").lower()

        if flavor == ("lemon" or "l"):
            flv_cost = bev_cost + 0.25
           # print("Tea with Lemon: $", flv_cost)
        elif flavor == ("mint" or "m"):
            flv_cost = bev_cost + 0.50
           # print("Tea with Mint: $", flv_cost)
        elif flavor == ("none" or "n"):
            flv_cost = bev_cost
           # print("Coffee with no extra flavor: $", flv_cost)
        else:
            print("Invalid Flavor")

else:
print("invalid beverage type")



tot_cost = flv_cost*tax

print("Total Cost after tax: " + "$"+ "%.2f" %tot_cost)               # Rounds to 2 decimal points
totalCost = str(round(tot_cost,2))         # Converts float to string so I can output on next line

print("For " + name + ", a " + bev_size + " " + bev_type + ", " + flavor + ", Cost: $" + tot_cost)

