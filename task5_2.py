def covid(name,body_temp=98):
    patient_details={ 'name':name,'body_temp':body_temp}
    print(patient_details)


name= input('enter the patients name')
temperature=int(input('enter the patients body tempratue'))
covid(name,temperature)