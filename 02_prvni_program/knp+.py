from random import randint

# Tohle je verze s pokrocilimi konstrukcemi, podivej se na ni az ke konci kurzu.

moznosti = ["kámen", "nůžky", "papír"]
tah_pocitace = moznosti[randint(0, 2)]
tah_cloveka = input("kámen, nůžky nebo papír? ")

# if tah_cloveka == 'kámen':
#     if tah_pocitace == 'kámen':
#         print('Plichta.')
#     elif tah_pocitace == 'nůžky':
#         print('Vyhrála jsi!')
#     elif tah_pocitace == 'papír':
#         print('Počítač vyhrál.')
# elif tah_cloveka == 'nůžky':
#     if tah_pocitace == 'kámen':
#         print('Počítač vyhrál.')
#     elif tah_pocitace == 'nůžky':
#         print('Plichta.')
#     elif tah_pocitace == 'papír':
#         print('Vyhrála jsi!')
# elif tah_cloveka == 'papír':
#     if tah_pocitace == 'kámen':
#         print('Vyhrála jsi!')
#     elif tah_pocitace == 'nůžky':
#         print('Počítač vyhrál.')
#     elif tah_pocitace == 'papír':
#         print('Plichta.')
# else:
#     print('Nerozumím, takhle se to nehraje.')
print(tah_pocitace)
if tah_cloveka == tah_pocitace:
    print("Plichta.")
elif ((tah_pocitace == "nůžky" and tah_cloveka == "papír") or
      (tah_pocitace == "kámen" and tah_cloveka == "nůžky") or
      (tah_pocitace == "papír" and tah_cloveka == "kámen")):
    print("Počítač vyhrál.")
elif tah_cloveka in moznosti:
    print("Vyhral jsi, gratuluji!")
else:
    print('Nerozumím, takhle se to nehraje.')

