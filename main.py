#Drill 2/ set operators
from pyscript import display, document

gr7 = {"Chesca Irinco", "Clarize Galang"}
gr8 = {"Kirche Segura", "Castor Ong"}
gr9 = {"Fia Riofrio", "Chelsea Coronado"}
gr10 = {"Julianne Canuday", "Niqa Agasi"} #sets for the members in each grade

all_members = gr7 | gr8 | gr9 | gr10 #combine every set

def add_members(e):
    document.getElementById('output').innerHTML = ' ' #to add new memeber

    first = document.getElementById('first').value
    last = document.getElementById('last').value #get the names in the html form

    new_member = f"{first} {last}" #combine first and last name

    all_members.add(new_member) #sheesh new member

    display("All Members:", target='output')
    display(*all_members, target='output')
    display(f"Total members: {len(all_members)}", target='output')