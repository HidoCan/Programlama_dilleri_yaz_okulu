metin = input('Metni Girin : \n')
ters=metin[::-1]
print('Girilen metin = %s' % (metin))
print('Girilen metnin tersi = %s' % (ters))
if ters == metin:
    print('Girilen metin palindrome')
else:
    print('Girilen metin palindrome değil.')
