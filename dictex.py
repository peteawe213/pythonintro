phone_number = input('Phone: ')
digits_mapping = {
    '0':'공',
    '1':'일',
    '2':'이',
    '3':'삼',
    '4':'사',
    '5':'오',
    '6':'육',
    '7':'칠',
    '8':'팔',
    '9':'구'
}
output = ''
for number in phone_number:
    output += digits_mapping.get(number) + ' '
print(output)
