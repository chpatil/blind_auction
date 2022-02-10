from replit import clear
import art 
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
def biggest(bid_dict):
  #print(bid_dict)
  temp=0
  winner=""
  for i in bid_dict:
    if(bid_dict[i]>temp):
      winner=i
      temp=bid_dict[i]
  print(f"The winner is {winner} with the bid of ${temp}.")

print("Welcome, to the secret auction program!!")
start_flag=True
yes_flag=True
bid_dict={}
while(start_flag):
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: "))
  bid_dict[name]=bid
  while(yes_flag):
    other_bidders=input("Are there any other bidders?:").lower()
    if(other_bidders=="yes"):
      clear()
      break
    elif(other_bidders=="no"):
      biggest(bid_dict)
      start_flag=False
      break
    else:
      print("Please enter the proper input")


