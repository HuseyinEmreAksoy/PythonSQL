import sqlite3

connection = sqlite3.connect(":memory:")

c = connection.cursor()
c.execute('''CREATE TABLE workerInformation (SicilNo , nameSurname , adress, TCNo)''')
c.execute('''CREATE TABLE workInformation (workCode ,title , department) ''')
c.execute('''CREATE TABLE generalInformation (SicilNo , workCode , startTime , finTime )''')

worker_info = [
    (324141324, 'Ali CAN','Hacı Murat COŞAR mahallesi 16545 sokak Denizli',4536435645765),
    (132414231, "Namık KEMAL", "Havzan mahallesi 75435 sokak Konya",8567356734),
    (1342124124, "Aslı ÖZDEMİR","Mustafa Kemal mahallesi 2134 sokak İstanbul",7658458458),
    (6543259656, "Osman GÜLTEKİN","Aykut ELMAS mahallesi 245 sokak İstanbul",5432524356),
    (456645369, "Pelin SU" , "Kızılay mahallesi 85 sokak Ankara", 523452345),
    (3214145, "Fatmagül AKSOY" , "Silikon mahallesi 456 sokak Van",8435324523),
    (5342324523, "Mahmut UÇAR" , "Yeniköy mahallesi 435 sokak İzmir" , 243523452345 ),
    (143324124, "Arif IŞIK" , "TOBB mahallesi 8434 sokak Ankara" , 2542345234),
    (5685686, "Ayşegül EKİN" , "Fevzi ÇAKMAK mahallesi 543 sokak Giresun" , 456342345432 ),
    (99089067, "Muhittin ÇEVİK" , "Selçuklu mahallesi 4352 sokak Trabzon" , 45323245235)]

c.executemany('INSERT INTO workerInformation  VALUES (?,?,?,?)', worker_info)

work_info = [
    (123, "ElektirkElektronik Mühendisliği","Elektronik"),
    (456,  "Bilgisayar Mühendisliği","Robotik"),
    (789, "Bilgisayar Mühendisliği","İşaret, Görüntü ve Ses İşleme"),
    (453, "Bilgisayar Mühendisliği" ,"Bulut Bilişim ve Uygulamaları"),
    (741, "Bilgisayar Mühendisliği","Yapay Zeka Uygulamaları"),
    (852, "Bilgisayar Mühendisliği","Bulut Bilişim ve Uygulamaları"),
    (986, "Bilgisayar Mühendisliği","Bilgisayar Sistemleri, Mimarisi, Paralel İşleme"),
    (861, "Bilgisayar Mühendisliği","Robotik"),
    (951, "Bilgisayar Mühendisliği","Siber Güvenlik"),
    (159, "ElektirkElektronik Mühendisliği","Elektronik"),]

c.executemany('INSERT INTO  workInformation VALUES (?,?,?)', work_info)

general_info=[
    (324141324, 123, "02/11/2001", "*"),
    (132414231, 456, "21/03/2012", "22/06/2019"),
    (1342124124, 789, "13/06/2020", "*"),
    (6543259656, 453, "30/10/2011", "07/10/2014"),
    (456645369, 741, "06/02/2013", "*"),
    (3214145, 852, "09/01/2008", "05/06/2026"),
    (5342324523, 986, "30/12/2014", "*"),
    (143324124, 861, "23/12/2011", "*"),
    (5685686, 951, "03/07/2009", "20/02/2020"),
    (99089067, 159, "19/11/2017", "*")]

c.executemany("INSERT INTO  generalInformation VALUES (?,?,?,?) ", general_info)
connection.commit()

work_codes=[]

for row in c.execute("SELECT workCode FROM workInformation WHERE title ='Bilgisayar Mühendisliği'"):
    work_codes.append(row[0])

sicil_no1=[]
sicil_no2=[]

for row in c.execute("SELECT SicilNo , workCode , finTime FROM generalInformation "):
    for element in work_codes:
        if(row[1]==element):
            sicil_no1.append(row[0])
            if(row[2]=="*"):
                sicil_no2.append(row[0])

print("Firmada çalışmış ve çalışmaya devam eden çalışanların TC kimlik numaraları ve adresleri: \n")

for row in c.execute("SELECT SicilNo , TCNo , adress From workerInformation "):
    for element in sicil_no1:
        if(row[0]==element):
            print(row[1],row[2],"\n")
            break

print("\n Aktif olarak çalışanların TC kimlik numaraları ve adresleri : \n ")

for row in c.execute("SELECT SicilNo , TCNo , adress From workerInformation "):
    for element in sicil_no2:
        if(row[0]==element):
            print(row[1] , row[2] , "\n")
            break