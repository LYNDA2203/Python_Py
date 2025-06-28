#28/06/2025
#using list,tuple,set,dict,file_handling,exception_handling,map,filter and lambda funtion
#students details

file_name="students_data.txt"

#method to add the students details to the file
def read_students():
    try:
        with open(file_name, 'r') as f:
            return [parse_student(line) for line in f if len(line.strip().split('|')) == 5]
    except FileNotFoundError:
        return []

def parse_student(line):
    sid, name, age, courses, marks = line.strip().split('|')
    return {
        'ID_Name': (int(sid), name),
        'Age': int(age),
        'Courses': courses.split(','),
        'Marks': list(map(int, marks.split(',')))
    }

#method to store students details
def save_students(students):
    with open(file_name, 'w') as f:
        for s in students:
            line = f"{s['ID_Name'][0]}|{s['ID_Name'][1]}|{s['Age']}|{','.join(s['Courses'])}|{','.join(map(str, s['Marks']))}\n"
            f.write(line)
            
#method to add students details
def add_student():
    try:
        sid = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        courses = list({c.strip() for c in input("Courses (comma-separated): ").split(',')})
        marks = list(map(int, input("Marks (comma-separated): ").split(',')))
        with open(file_name, 'a') as f:
            f.write(f"{sid}|{name}|{age}|{','.join(courses)}|{','.join(map(str, marks))}\n")
        print("✅ Student added successfully!")
    except:
        print("❌ Invalid input.")

        
# method to show all student records
def show_all_students():
    students = read_students()
    
    #checking whether the students record present in file
    if not students:
        print("📭 no studnt records found.")#\U0001F4ED
        return
    
    print("📘 All Students Records: ")#\U0001F4D8
    for s in students:
        print(s)
        
 # filtering students with the marks about 40
def filter_passed_students():
    students = read_students()
    passed = list(filter(lambda s: all(mark > 50 for mark in s['Marks']), students))  
    
    print("✅ Students with marks > 40 in all subject:")#\u2705
    for s in passed:
        print(s)

def average_marks():
    students = read_students()
    print("📊 Average Marks:")#\U0001F4CA
    for  s in students:
        avg = sum(s['Marks']) / len(s['Marks']) if s['Marks'] else 0
        print(f"{s['ID_Name']}: {avg:.2f}")
        
def delete_student():
    sid = int(input("Enter Student ID to delete: "))
    name = input("Enter Student Name to delete: ")
    students = read_students()
    filtered = [s for s in students if s['ID_Name'] != (sid, name)]
    if len(filtered) == len(students):
        print("❌ Student not found.")
    else:
        save_students(filtered)
        print("🗑️ Student deleted successfully!")
        
def exit():
     print("👋 Exiting...")
    
      
menu = {
    '1': add_student,
    '2': show_all_students,
    '3': filter_passed_students,
    '4': average_marks,
    '5': delete_student,
    '6': exit
}

while True:
    print("\n📚 Student Record System")
    print("1. Add Student\n2. Show All Students\n3. Filter Passed Students\n4. Show Average Marks\n5. Delete Student\n6. Exit")
    choice = input("Enter choice: ")
    menu.get(choice, lambda: print("❌ Invalid choice!"))()
         