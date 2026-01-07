# simple_demo.py

from utils.database import get_db

def simple_demo():
    # Get database connection
    db = get_db()
    
    # Create a collection (it's created automatically when you insert)
    students_collection = db['students']
    
    # Single document insert
    student1 = {
        "name": "Rahul Sharma",
        "age": 20,
        "course": "Computer Science",
        "marks": 85
    }
    
    result = students_collection.insert_one(student1)
    print(f"✅ Inserted 1 student, ID: {result.inserted_id}")
    
    # Multiple documents insert
    more_students = [
        {"name": "Priya Patel", "age": 21, "course": "IT", "marks": 92},
        {"name": "Amit Kumar", "age": 22, "course": "Computer Science", "marks": 78},
        {"name": "Sneha Desai", "age": 20, "course": "IT", "marks": 88}
    ]
    
    result2 = students_collection.insert_many(more_students)
    print(f"✅ Inserted {len(result2.inserted_ids)} more students")
    
    # Read data back
    print("\n📚 All Students:")
    all_students = students_collection.find()
    for student in all_students:
        print(f"   - {student['name']}: {student['marks']} marks")
    
    # Count total documents
    total = students_collection.count_documents({})
    print(f"\n📊 Total students: {total}")

if __name__ == '__main__':
    simple_demo()
