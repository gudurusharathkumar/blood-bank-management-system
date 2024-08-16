import pickle 
def blood_options(): 
global dict 
global blood_opt 
global blood_grp 

while(1): 
print("Select blood group of the person plz Enter one option:") 
dict={1:"A+",2:"B+",3:"AB+",4:"O+",5:"A-",6:"B-",7:"AB-",8:"O- "}
 		for i in dict.keys(): 
print(" %d).%s"%(i,dict[i])) 
blood_opt=input("Enter blood number:") 
if(blood_opt.isdigit()): 
if(int(blood_opt)>0 and int(blood_opt)<9): 
break 
else: 
print("Enter only correct number")
else: 
print("Enter only digits") 
blood_grp=dict[int(blood_opt)] 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
def unlock(): 
xx=open("Blood_Encription","rb") 
yy=pickle.load(xx) 
i=3 
while(i>0): 
print("You have %d chances"%(i)) 
i=i-1 
password=input("Enter possword to Unlock::") 
if(yy[0]==password) :
if(yy[0]==password): 
print("You successfully
Unlocked\n*************************************") 
break 
else: 
print("Password is incorrect ...") 
else: 
print("If you forget your password Enter 1 else enter 0:") 
mmm=1 
while(1 and mmm): 
pass_forget=input("Enter your option:") 
if(pass_forget.isdigit()): 
pass_forget=int(pass_forget) 
if(pass_forget==1): 
nickname=input("Enter your nick name first to change password:") 
if(yy[1]==nickname): 
password1=input("Enter your new password:") 
mkm=open("Blood_Encription","wb") 	
pickle.dump([password1,nickname],mkm)
else: 
print("Enter only digits") 
def add(): 
while(1): 
state=input("ENTER STATE:") 
if(state.isalpha()): 
break 
else: 
print("Enter only Alphabets") 
district() 
mondal() 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
while(1): 
village=input("ENTER VILLAGE:") 
If(village.isalpha()): 
break 
else: 
print("Enter only Alphabets") 
village=village.capitalize() 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
while(1): 
o=0
name=input("ENTER NAME:")
for b in range(10):
if(name.startswith(str(b))): 
o=1 
if(o==1): 
print("Digits are not allowed at Starting") 
else: 
break 
name=name.capitalize() 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
while(1): 
ph_no=input("ENTER PH_NO:") 
if(ph_no.isdigit()): 
if(len(ph_no)==10): 
if(int(ph_no[0])<=5): 
print("Must be first digit is greatet than 5") 
else: 
break 
else: 
print("Enter 10 digits number") 
else: 
print("Enter only digits") 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*") 
if(s123==1): 
pass 
else: 
for i in m: 
for j in i: 
if(ph_no==j): 
print("*-*-*-*-*-*-*-*-*-*-*-*-*") 
print("The Record/Ph_no already exits") 
return 
while(1):
sta=input("Enter how many last records statement you want:") 
if(sta.isdigit()): 
if(int(sta)>0): 
if(nn>int(sta)): 
kkk+=(nn-int(sta) 
print("enter only digits") 
n=int(n) 
if(n==1): 
add() 
elif(n==2): 
search() 
elif(n==3): 
deletelast() 
elif(n==4): 
edit() 
elif(n==5): 
full_details() 
elif(n==6): 
blood_available() 
elif(n==7): 
all_bloods() 
elif(n==8): 
statement() 
else: 
print("enter correct option") 
