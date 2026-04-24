#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10. // tive dificuldade 


numero_impa = 0 

for i in range  (1,11): 
   if i %2 == 1:
        numero_impa = numero_impa+i
        print(f"{numero_impa}")