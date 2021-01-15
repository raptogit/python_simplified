year=int(input("Give the year:\n"))
if year%4==0:
  if year%100==0:
      if year%400==0:
        print("This is leap year")
      else:
          print("This is not a leap year")  
  else:
      print(" leap year!")    
else:
    print("Not an leap year !")    