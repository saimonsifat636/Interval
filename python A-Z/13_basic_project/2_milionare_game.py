questions=[
   [ "What is the brain of a computer?", "A) RAM", "B) CPU", "C) ROM", "D) HDD", "B"
],["Which language is mainly used for web page structure?", "A) Python", "B) C++", "C) HTML", "D) Java", "C"
],["What does CPU stand for?", "A) Central Processing Unit", "B) Computer Personal Unit", "C) Central Program Utility", "D) Control Processing User", "A"
],["Which data type stores True or False in Python?", "A) int", "B) str", "C) bool", "D) list", "C"
],["Which symbol is used for comments in Python?", "A) //", "B) #", "C) /*", "D) &", "B"
],["What is the output of print(2 ** 3) in Python?", "A) 6", "B) 8", "C) 9", "D) 5", "B"
],["Which device is used to input text into a computer?", "A) Monitor", "B) Printer", "C) Keyboard", "D) Speaker", "C"
],["Which Python collection stores key-value pairs?", "A) List", "B) Tuple", "C) Set", "D) Dictionary", "D"
],["What does RAM stand for?", "A) Read Access Memory", "B) Random Access Memory", "C) Run Active Memory", "D) Rapid Action Module", "B"
],["Which loop is commonly used to iterate over a sequence in Python?", "A) for", "B) switch", "C) repeat-until", "D) do-while", "A"
]]


prize=[10000,20000,30000,40000,50000,60000,70000,80000,90000,10000000000]
sum=0
i=0
for question in questions:
    print(f"{question[0]}\n{question[1],question[2],question[3],question[4]}")
    answer=input("please enter the answer: ")
    if answer.upper()==question[5]:
        sum+=prize[i]
        print("you current prize money is : ",sum)
        i+=1
    else:
        print("wrong answer !!!!!!!")
        print("you are eliminated!!!")
        break