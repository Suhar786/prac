weight=int (input("Weight: "))
unit=input("Kg OR Lb: ")
if \
      unit=="k" or "K":
      total= weight / 0.45
      print("Weight in lbs = ",total)
elif \
      unit=="L" or "l":
      total=weight * 0.45
      print("Weight in kgs = ",total)

