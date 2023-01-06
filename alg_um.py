# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
import math
import random

def busca_binaria(lista, num):
    comeco_lista = 0
    meio_lista = math.floor(len(lista)/2)
    fim_lista = len(lista)
    cont = 0

    while num != meio_lista: # vai fazer o programa rodar bastante pra achar o número
        if num == meio_lista:
            print('ACHOU DE PRIMEIRA!')
            break

        if num > meio_lista:
            print('num > meio da lista')
            cont+=1
            comeco_lista = meio_lista
            meio_lista = math.floor(fim_lista - (fim_lista-meio_lista)/2) # Limitando os 'universos' onde o número pode existir
            # print(f'Começo : {comeco_lista}\nMeio : {meio_lista}\nFim : {fim_lista}')
            if meio_lista == num:
                print(f'Achou o número! {num}')
                print(f'Qntd de vezes que o código rodou = {cont}')
        
        if num < meio_lista:
            print('num < meio da lista')
            cont+=1
            fim_lista = meio_lista
            meio_lista = math.floor(fim_lista - (fim_lista-meio_lista/2))
            # print(f'Começo : {comeco_lista}\nMeio : {meio_lista}\nFim : {fim_lista}')
            if meio_lista == num:
                print(f'Achou o número! {num}')
                print(f'Qntd de vezes que o código rodou = {cont}')
            
    

# print(f'Começo : {comeco_lista}\nMeio : {meio_lista}\nFim : {fim_lista}')

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
busca_binaria(lista, random.choice(lista))




























    # print(f'{comeco_lista}\n{meio_lista}\n{fim_lista}\n')

# busca_binaria(lista, 3)

# comeco_lista = 0
# fim_lista = 100
# meio_lista = fim_lista/2
# print(f'Antes do IF\nComeço : {comeco_lista}\nMeio : {meio_lista}\nFim : {fim_lista}')

# comeco_lista = meio_lista
# meio_lista = fim_lista - (fim_lista-meio_lista)/2
# print(f'Depois do IF\nComeço : {comeco_lista}\nMeio : {meio_lista}\nFim : {fim_lista}')