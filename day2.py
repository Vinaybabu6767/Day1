total = input("what is the total bill $")
split = input("How many members want to split:")
percentage=input("how much percentage do you want?")

result = float(total)/int(split)
per = int(percentage)/100
per+=1
final = result * per
print(f"Here is the bill per person need to pay $ {final}")