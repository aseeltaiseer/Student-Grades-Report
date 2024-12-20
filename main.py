
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades) 
    return round(average, 2)

def get_grade(average):
    if average >= 90:
        return 'Excellent'
    elif average >= 75:
        return 'Very Good'
    elif average >= 60:
        return 'Good'
    elif average >= 50:
        return 'Pass'
    else:
        return 'Fail'

def show_report(students):
    print("\nStudent Report:")
    print("{:<15} {:<15} {:<15} {:<15}".format('Name', 'Average', 'Grade', 'ID'))
    for student in students:
        print("{:<15} {:<15} {:<15} {:<15}".format(student['name'], student['average'], student['grade'], student['id']))

def main():
    students = [] 
    
    while True:
        print("\n1. Add a new student")
        print("2. Show student report")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student ID: ")
            
            grades_input = input("Enter grades (separate with spaces): ")
            grades = [int(grade) for grade in grades_input.split()]
            
            average = calculate_average(grades) 
            grade = get_grade(average) 
            
            student = {
                'name': name,
                'id': student_id,
                'grades': grades,
                'average': average,
                'grade': grade
            }
            
            students.append(student)
            
            print(f"\nStudent {name} has been added successfully.")
        
        elif choice == '2':
            if len(students) > 0:
                show_report(students)
            else:
                print("\nNo students to display in the report.")
        
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

main()
