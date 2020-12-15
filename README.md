The program is a web crawler that extracts email address and displays as a list. 
The program takes url as an input.
•	First, I import the needed libraries including the “re” for regular expression. 
•	Then, I added the url as argument for function “emails”.
•	The program uses regular expression to find the email address that contains @ sign. 
•	Re.findall finds all occurrences with such expression
•	I have also made a filtered email list that removes any duplicate emails that might be listed in email_list

