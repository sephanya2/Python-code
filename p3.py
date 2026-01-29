#Display the result

sub1 = int(input("enter the marks of sub 1:"))
sub2 = int(input("enter the marks of sub 2:"))
sub3 = int(input("enter the marks of sub 3:"))
sub4 = int(input("enter the marks of sub 4:"))

total = (sub1+sub2+sub3+sub4)
percentage =int((sub1+sub2+sub3+sub4)/4)

print("Total:",total)
print("percentage:" ,percentage)

if percentage > 85:
   print("A+ grade")
elif percentage < 85 and percentage > 70 :
   print ("B+ grade")
elif percentage < 70 and percentage < 60 :
   print ("c+ grade")
elif percentage < 60 and percentage < 50 :
   print ("D+ grade")
elif percentage < 40:
   print("fail"); 
   


