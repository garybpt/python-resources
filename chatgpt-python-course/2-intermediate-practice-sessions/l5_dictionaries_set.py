# Create a dictionary called student_scores to store the scores of three students

student_scores = {"Alice": 90, "Bob": 85, "Charlie": 78}

set1 = {"Gary", "Alex", "Ailish", "Anil"}
set2 = {"Gary", "John", "Alex", "Clare"}

# Find the union of set1 and set2

union_result = set1 | set2  # Union of set1 and set2
print(union_result)  # Output: {'Ailish', 'Alex', 'Anil', 'Clare', 'Gary', 'John'}

# Find the intersection of set1 and set2.

intersection_result = set1 & set2  # Intersection of set1 and set2
print(intersection_result)  # Output: {'Gary', 'Alex'}

# Find the elements that are unique to set1 (not in set2).

difference_result = set1 - set2  # Unique elements in set1
print(difference_result)  # Output: {'Ailish', 'Anil'}