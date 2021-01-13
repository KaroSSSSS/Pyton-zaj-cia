db = {
    "Ganjalf" : '123',
    "admin" : 'admin',
    "Gerwazy" : '123456',
    "Krystian" : '321',
    "Johnny_Sins" : 'C0cKs',
    "KolegaMariana" : '32123'
}
while True:
    login = input("Login: ")
    password = input("Password: ")
    if password == db.get(login):
        if 'admin' != db.get(login):
            print("Zalogowano jako użyszkodnik ")
            break;
        else:
            print("Zalogowano jako admin admin ")
            break;
    else:
        print("Cos zepsulesi")