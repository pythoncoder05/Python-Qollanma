# "True" va "False" haqida qisqacha
# "and" va "or" haqida qisqacha
narh = 20000
# "True"ni bu 'rost' yoki 'Ha' degan so'zga qiyoslasa bo'ladi
# "False"ni esa 'yolg'on' yoki 'Yo'q' degan so'zga qiyoslasa bo'ladi
choy = True # "True" bu masalan mijoz {choy} sotib oldimi? 'True' < Ha > 
salat = False # "False" bu masalan mijoz {salat} sotib oldimi? 'False' < Yo'q >
if choy and salat: # "and" bu va degan manoni anglatadi
     # masalan mijoz 'choy' va 'salat' sotib oldimi [ "True" / "False ]
    narh = narh + 10000
elif choy or salat: # "or" esa 'yoki' degan manoni anglatadi
    # masalan mijoz 'choy' yoki 'salat' sotib oldimi [ "True" / "False" ]
    narh = narh + 5000
print(f"Jami {narh} so\'m")