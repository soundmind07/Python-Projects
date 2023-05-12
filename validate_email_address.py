""""

Project Learnings:
1- used string functions like isalpha,count,isspace,upper,digit to validate the conditions
2- used for loop for performing iteration
3- used and and xor operators for checking two statements inside the if statement

"""
email=input("Enter your email: ")  #g@g.in
k=0
d=0
j=0
if len(email)>=6:                                        #since minimum length of an email is supposed to be 6 so to check that we have used this condition.
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):     # this condition ensures that @ is present and present only once in our email.
          if (email[-4]==".") ^ (email[-3]=="."):        # this condition checks whether . is present at correct location or not.
              for i in email:
                  if i==i.isspace():                     #since emails can't have space so to check them we have used this condition
                      k=1
                  elif i.isalpha():
                      if i==i.upper():                   #since all alphabets are supposed to be present in lower case so we have used this condition.
                          j=1
                  elif i.isdigit():
                      continue
                  elif i=="_" or i=="." or i=="@":
                      continue
                  else:
                      d=1                                # if any character other than "_", ".", "@" are present so to check them we have used this condition.
              if(k==1) or (j==1) or (d==1):
                  print("wrong email 5 ")                #5 means your email failed at this condition.
              else:
                  print("Right email ")
          else:
              print("wrong email 4 ")                    # 4 means your email failed at this condition
        else:
            print("wrong email 3 ")                      # 3 means your email failed at this condition
    else:
        print("wrong email 2 ")                          # 2 means your email failed at this condition
else:
    print("wrong email 1 ")                              # 1 means your email failed at this condition

