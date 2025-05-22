def count_students_unable_to_eat(students, sandwiches):
    from collections import Counter
    student_counts = Counter(students)

    for sandwich in sandwiches:
        print(student_counts[sandwich])
        print(student_counts)
        if student_counts[sandwich] > 0:
            student_counts[sandwich] -= 1
        else:
            break
    
    return sum(student_counts.values())

# Example:
students = [1,1,0,0]
sandwiches = [0,1,0,1]
print(count_students_unable_to_eat(students, sandwiches))  # Output: 2
