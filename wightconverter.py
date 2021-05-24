weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kgs")
else:
    converted = weight / 0.45
    print(f"You are {converted} lbs")

#무게 파운드/킬로그램 변환기 ㅋ^^ (8/apr)
