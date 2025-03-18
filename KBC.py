import time #using this to avoid termination of programme for normal ppl
ques=[
    "Which planet is known as the Red Planet?",
      "Who was the first President of India?",
      "What is the capital of Japan",
      "Which is the largest continent by area?",
      "Who wrote the national anthem of India?",
      ]


opt=[
    ["earth","jupiter","mars","venus"],
     ["rajendra prasad","jawaharlal nehru","bhimrao ambedkar","vallabhbhai patel"],
     ["beijing","seoul","tokyo","bangkok"],
     ["africa","asia","north america","europe"],
     ["rabindranath tagore","bankimchandra chatterjee","mahatma gandhi","subhash chandra bose"]
     ]


ans=["mars","rajendra prasad","tokyo","asia","rabindranath tagore",]

no=['Pahla','Dusra','Teesra','Chautha','Paanchwa']

prize=["$0","$1000",'$2000',"$4000","$10000","$2000"]

print('\n')
print('DEVIO/SAJJANO AAPKA KBC KE KHEL ME SWAGAT H')
print('AASHA H AAP DHER SAARI DHAN RAASH JEET KE JAYENGE!!!\n')
print("TO CHALIYE SHURU KRTE H........","\n")
print('\n')


alp=0
count=0
for i in range(len(ques)):
    
    print(no[i],"prashna aapki computer screen pe ye rha !!",'\n')
    
    print(ques[i],'\n')
    o=opt[i]
    
    while True:
        
        print(o[count])
        count+=1
        if count==(len(o)):
            break
    print('\n')
    count=0
    a=input("uttar kare :- ")
    print('\n')

    if a.lower() == ans[i]:
        print("Sahi jawab!!")
        print('aap jeette hai',prize[i+1])
        print('\n')
        print('agle prashna ki or badhte ha')
        alp+=1
    
    else:
        print('galat jawab aur aap haar gye')
        print('sahi jawab hai',ans[i])
        break
       
print("aapki jeeti hui total rashi hai :- ",prize[alp])
time.sleep(9999)