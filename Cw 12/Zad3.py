stopy = int(input("Podaj długość w stopach: "))
def stopy_metry(stopy):
    metry = stopy * 0.3048
    return global metry
def metry_kilometry(metry):
    kilometry = metry / 1000
    return kilometry
def metry_centymetry(metry):
    centymetry = metry * 100
    return centymetry
def metry_milimetry(metry):
    milimetry = metry * 1000
    return milimetry
print("Stopy na metry: ", stopy_metry(stopy))
print("Stopy na kilometry: ", metry_kilometry(metry))
print("Stopy na centymetry: ", metry_centymetry(metry))
print("Stopy na milimetry: ", metry_milimetry(metry))