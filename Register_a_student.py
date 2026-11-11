import json
new_student={}
def register_a_student():
    a=input("Enter your roll no: ")
    b=input("Enter your name: ").strip()
    c=input("Enter your branch: ").strip()
    new_student[a]={
        "name":b,
        "branch":c,
    }
    with open("new_student.json", "w") as f:
        json.dump(new_student, f, indent=4)

register_a_student()