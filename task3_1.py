ages1 = {
    'nanda':18,
    'mahesh':22,
    'sai':25
}
ages2 ={
    'nani':14,
    'ashok':16
}
ages ={
    **ages1,
    **ages2
}
print(ages)