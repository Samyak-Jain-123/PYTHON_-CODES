#Question 1 (Alphabetical Dictionary)                                                  ------ EXPERT 1
score = {
    "key": "value",
    "name": "Samyak",
    "subjects": "good",
    "apples": "fruit",
    "potato": "veg"
}
a=score.items()
sort1 = dict(sorted(a))

print("Alphabetical Dictionary:",sort1)
print(type(sort1))



#Question 2 (Phone Number)
conc={
    "usr1" : 91,
    "usr2" : 92,
    "usr3" : 66
}

a=input("Enter the name =")
b=int(input("Enter its phone no="))

conc.update({a:b})
print(conc)

a=input("Enter the name whose phone no should be deleted =")

del (conc[a])
print(conc)



#Question 3 (Store 9 & 9.0 as separate values in a set)
s={9,'9.0'}
print(s)



#Question 4 (Subjects and marks)                                                       ------ EXPERT 2
marks={
    "A":{"P":22,
         "C":29,
         "M":15} ,

    "B":{"P":30,
         "C":28,
         "M":23} ,

    "C":{"P":13,
         "C":19,
         "M":11}
}
print("Test Result")
print(marks)

#1
marks["A"].update({"E":24})
marks["B"].update({"E":27})
marks["C"].update({"E":14})

print("Test Result (Updated with english marks)")
print(marks)

#2
for i in marks:
    marks[i]["M"]+=1

print('One Question of Maths was marked wrong in this test\nDue to this reason, All students are awarded +1 in Maths')
print(marks)

#3
for i in marks:
    a = sum(marks[i].values())
    print(f"Total marks of {i}: {a}")
    print(f"Avg marks of {i}: {a/4}")

#4
high=0
for i in marks:
    a = sum(marks[i].values())

    if a>high:
        high=a
        top=i

print(f"Topper of this test is {top} with total mark of {high}")

#5
j=0
k=0
l=0
m=0
for i in marks:
    a = marks[i]["P"]
    b = marks[i]["C"]
    c = marks[i]["M"]
    d = marks[i]["E"]

    if a>j:
        j=a
        w=i

    if b>k:
        k=b
        x=i

    if c>l:
        l=c
        y=i

    if d>m:
        m=d
        z=i


print(f"Topper of 'P' is {w} with total mark of {j}")
print(f"Topper of 'C' is {x} with total mark of {k}")
print(f"Topper of 'M' is {y} with total mark of {l}")
print(f"Topper of 'E' is {z} with total mark of {m}")
'OR'

subjects = marks["A"].keys()

for j in subjects:
    highest = 0
    holder = ""

    for i in marks:
        if marks[i][j] > highest:
            highest = marks[i][j]
            holder = i

    print(f"{j}: {highest} ({holder})")


