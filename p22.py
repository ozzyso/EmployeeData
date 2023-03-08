calisan = {
    'kod': 'HS01',
    'ad' : 'Özlem',
    'soyad': 'Söker'
}
print(calisan)

birlestir = f"{calisan['kod']} kodlu çalışanımız {calisan['ad']} {calisan['soyad']} izne ayrılmıştır."
print(birlestir)

print(50*'=')

print(calisan.get("ad"))

for i in calisan:
    print(i) #sadece key veriyor

for (key, value) in calisan.items():
    print(key, value)

print(50*'=')

for value in calisan.values():
    print(value)

calisan['maas'] = 15000
print(calisan)

calisan.pop('kod')
print(calisan)

#calisan.clear() btn elemanları siler
#print(calisan)

calisan.popitem()
print(calisan)

print(50*'=')

employees = {
    "özlem": {
        "yas": 38,
        "maas": 15000,
        "adsoyad": "Özlem Söker",
        "tel": "5325771155",
        "adres": "Miami USA"
    },
    "john": {
        "yas": 40,
        "maas": 45000,
        "adsoyad": "John Adams",
        "tel": "2016854578",
        "adres": "LA USA"
    },
    "summer": {
        "yas": 40,
        "maas": 500000,
        "adsoyad": "Summer Soker",
        "tel": "3303375471",
        "adres": "CA USA",
        "department": ["ik","it"]
    }
}
print(employees)

print(50*"=")
print(employees["summer"]["department"][1]) 