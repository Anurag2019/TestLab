import pytest
from lists import sum_of_elements,find_even,create_list
from dictionary import create_dict,exists, add_item,delete_item
def test_sum():
    assert sum_of_elements([2,3,5,7])==17
    
@pytest.fixture
def even_list():
    return [i for i in range(1,11) if i%2==0]
@pytest.fixture
def student_data():
    return [{
        "name":"Anurag Pattnaik",
        "degree":"MCA",
        "skills":{"Python","Flutter","Java","SQL"},
        "percentage":85
    },
      {
        "name":"Itishree Biswal",
        "degree":"BTech",
        "skills":{"Java","PHP","C++","HTML"},
        "percentage":90
    },      
      {
        "name":"Barnali Das",
        "degree":"MCA",
        "skills":{"Python","Dot Net","Java"},
        "percentage":74
    },
      {
        "name":"Manisha Mallick",
        "degree":"MSc",
        "skills":{"JavaScript","Flutter","C#","SQL","HTML"},
        "percentage":68
    },
            
        ]
def test_sum_of_even(even_list):
    assert sum_of_elements(even_list) == 30
    assert sum_of_elements(create_list(20,40,5)) == 150

def test_number_in_list(even_list):
    assert 4 in even_list
    assert 5 not in even_list
    assert not all(i in even_list for i in (2,4,5))
    assert 50  in create_list(30,50,2)
def test_compare(even_list):
    assert set(find_even(list(range(2,20)))).issuperset(set( even_list))
    assert 10 in set(create_list(10,20)).intersection(set(even_list))

def test_student_data(student_data):
    assert student_data[0]["name"]=="Anurag Pattnaik"
    assert "Python" in student_data[0]["skills"]
    assert student_data[0]["degree"].startswith("M")
    assert len(student_data)==4
    assert len([stud for stud in student_data if stud["percentage"]>80] )==2
@pytest.fixture
def student_grade(student_data):
    grade={}
    for i,student in enumerate(student_data):
        per=student["percentage"]
        grade[i]="A" if per >= 85 else "B" if 70 <= per < 85 else "C"
    return grade
def test_grade(student_grade):
    assert student_grade[0]=="A"
    assert student_grade[1] == "A"
    assert student_grade is not None
    assert "C"  in list(student_grade.values())
    assert student_grade[3]=="C"
    assert list(student_grade.values()).count("A")==2
    assert {"B","C"}.issubset(set(student_grade.values()))
def test_skills(student_data):
    assert "Flutter" not in student_data[1]["skills"]
    assert "Python"  in student_data[0]["skills"].intersection(student_data[2]["skills"])
    s0_skills=student_data[0]["skills"]
    s1_skills=student_data[1]["skills"]
    s2_skills=student_data[2]["skills"]
    s3_skills=student_data[3]["skills"]
    assert  s2_skills.isdisjoint(s3_skills)

@pytest.fixture
def employees():
    return create_dict(["Anurag","Karishma","Shalini","Pooja"],[32,29,31,30])
def test_employee_data(employees):
    assert exists("Karishma",employees)
    assert exists(32,employees.values())
    assert employees["Anurag"] ==32
    assert len([age for age in employees.values() if age >=30])==3
    assert [name for name in employees if employees[name] > 30]==["Anurag","Shalini"]
    assert exists("Pooja",[name for name in employees if employees[name] <= 30])

def test_add_employee(employees):
    add_item("Rohan",32,employees)
    
    assert exists("Rohan",employees)
    add_item("Manisha",30,employees)
    assert exists("Manisha",employees)
   
def test_delete_employee(employees):
   
    delete_item("Anurag",employees)
    assert not exists("Anurag",employees)
    # delete_item("Rohan",employees)
    assert not exists("Rohan",employees)
    