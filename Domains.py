def domain_name(url):
    pieces = url.split('.')
    print(pieces)
    if pieces[0].find('www') != -1:
        return pieces[1]
    elif pieces[0].find('//') != -1:
        return pieces[0][pieces[0].find('//') + 2 :]
    else:
        return pieces[0]


print(domain_name('https://www.google.com'))
print(domain_name('http://youtube.co.jp'))
print(domain_name('https://youtube.co.jp'))
print(domain_name('www.xakep.ru'))
print(domain_name('http://www.codewars.com/kata/'))
print(domain_name('icann.org'))
print(domain_name('9p6jhi0ra6.br/index.php'))

# return url.split("//")[-1].split("www.")[-1].split(".")[0]