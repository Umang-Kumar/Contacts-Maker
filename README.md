# Contacts-Maker
 A simple Python code that takes input from a csv file and makes it into a vcf file.

Imagine a college or a large community where each year/semester new people join and people need to save their contacts for 
obvious reasons. Now I'm a college student, so I'll give you a simple example every year 400 students join in 4 
different streams. And it gets very hectic for teachers to save contacts of each and every student, and if by chance 
someone decides to go to another college, then they have to undo the process.

This is something I came up with we can circulate a Google form asking students/pupils to fill-in their contacts and 
when it's filled run this code with the correct path of the file. Name, E-mail, Phone Number and branch/stream/division
(optional) this is all we need.

Now, I don't think I need to define my code because it's already well-defined and pretty informative. But still, the 
part where people could get struck is " # i[0] = 'Aitian 21' " because in the csv file the first i[0] is Timestamp, and 
I've replaced it with "Aitian 21" why? My college is AIT, that's why. You can add whatever you want or can leave it 
blank. Now this one, "# if i[4].endswith('@aitpune.edu.in'):" was to verify that, contacts of only my college students
should get saved and no one else, you can replace it with your organisation email I'd.

That's all. Hope it was useful.