# bu yerda Slicing haqida gaplashamiz ya'ni listlarda biz xoxlagan elemtni chiqarish qayeridan qayerigacha 
# umuman indexi bilan ishlash, indexsi orqali ularni chqarib olish ya'ni shu elementni listda turgan tartib raqami asosida
# biz bilamizki indexsni sanash 1 dan emas aksincha 0 dan boshlanadi 0,1,2,3,4,5,.....
actors=["dilnoza","shohruxon","jeki chan","deniel redklif","karina kapur","arnold","angelica djoli"]
print(actors[0:4]) # bu degani 0 dan 4 gacha degani (4 ni o'zi kirmaydi) ya'ni 0=dilnoza,3=deniel redklif...

# buni endi turlicha o'zgartirishimiz mumkin masalan bizga 2 elementdan 5 gachasi kerak bo'lsin deylik
print(actors[2:5])

# yoki umuman listni o indexsidan ya'ni elon qilgan listimizni boshida turgan elementdan boshlab
#  masalan 4 chi indexsda turgan elementga cha kerak deylik
print(actors[:4]) # bu yerda listni boshidan boshlab ol lekin 4 - indexsgacha degani

# yoki agar indexni manfiy sonlar bilan yozsan listni oxiridan boshlab sananagan bo'lamz ya'ni teskaridan
# masalan bizga elon qilingan listdagi elementlarni oxirigi ikkitasi kerak bo'lsa
print(actors[-2:])