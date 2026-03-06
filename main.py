
# 21-m
def eng_katta(a, b, c):
    if a >= b and a >= c:
        return "Eng katta: " + str(a)
    elif b >= a and b >= c:
        return "Eng katta: " + str(b)
    else:
        return "Eng katta: " + str(c)

print(eng_katta(5, 8, 3))


# 22-m
def fasl(oy):
    if oy in [3,4,5]:
        return "Bahor"
    elif oy in [6,7,8]:
        return "Yoz"
    elif oy in [9,10,11]:
        return "Kuz"
    elif oy in [12,1,2]:
        return "Qish"
    else:
        return "Noto‘g‘ri oy"

x = fasl(12)
print(x)


# 23-m
def bolinish(n):
    if n % 2 == 0 and n % 3 == 0:
        return "6 ga karrali"
    elif n % 2 == 0 or n % 3 == 0:
        return "Qisman mos"
    else:
        return "Mos emas"

x = bolinish(10000002345678910)
print(x)


# 24-m
def matn_tekshir(text):
    if any(c.isupper() for c in text) and any(c.islower() for c in text) and any(c.isdigit() for c in text):
        return "Murakkab matn"
    else:
        return "Oddiy matn"

x = matn_tekshir("Aqwertyuuiplkjhgfdsazxzcvbnmnbvcxzasdfghjlllllpoiuytrewqasdfghjklllllllllllllllllmnbvcxzaqerrtyuuiio0987654321")
print(x)


# 25-m
def farq(a, b):
    if a - b > 10:
        return "Ancha katta"
    else:
        return "Farq kichik"

x = farq(25,2)
print(x)


# 26-m
def parol(p):
    if len(p) < 6:
        return "Juda zaif"
    elif 6 <= len(p) <= 10:
        return "O‘rtacha"
    elif len(p) > 10 and any(c.isdigit() for c in p):
        return "Kuchli"

x = parol('123455678900987654321123456789009876543211111123456789000000000')
print(x)

# 27-m
def harf(h):
    unlilar = "aeiouAEIOU"
    if h.isalpha():
        if h in unlilar:
            return "Unli"
        else:
            return "Undosh"
    else:
        return "Harf emas"

x = harf('aeiouAEIOU')
print(x)


# 28-m
def bosh_joy(matn):
    if matn.startswith(" ") or matn.endswith(" "):
        return "Keraksiz bo‘sh joy bor"
    else:
        return "Toza matn"

x = bosh_joy('salom')
print(x)


# 29-m
def son_holat(a, b):
    if a == 0 or b == 0:
        return "Nol mavjud"
    elif a > 0 and b > 0:
        return "Ikkalasi musbat"
    else:
        return "Boshqa holat"

x = son_holat(2, 5)
print(x)


# 30-m
def oraliq(n):
    if 1 <= n <= 100 and n % 2 == 0:
        return "Mos juft"
    elif 1 <= n <= 100 and n % 2 != 0:
        return "Mos toq"
    else:
        return "Oraliqdan tashqarida"

x = oraliq(99)
print(x)
