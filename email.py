
#Pravin Bhandari
#Web_Crawler to extract email address

import urllib.request   #import lib
import re               #import for regular expression
def emails(str):        #argument for the function emails

    text=urllib.request.urlopen(str).read().decode(errors='replace')  

    regex=re.compile(r'[\w.-]+@[\w.-]+')   #finds emails with @ sign before and after words
    
    email_list=re.findall(regex,text)   #Finding all occurences
    
    
    filtered_email_list = list(dict.fromkeys(email_list))  #Filtered email lists to avoid duplications
    
    
    print("\n              EMAILS FOUND ON THE WEBSITE        \n \n",filtered_email_list)  #print results


    f=open("emails.txt","a+")  #Append

    f.write("Website_Name: "+str+"\n\n")
    for i in email_list:

        f.write(i+" ")

ask=input("Please enter the url to extract email ids: ")    #ask for input

emails(ask)