def biggest_denominator(Aden, Bden):
    if Aden != Bden:
        multiplication = Aden * Bden
        return multiplication
    elif Aden == Bden:
        final_denominator = Aden
        return final_denominator
def addition(tu, tv):
    if Aden != Bden:
        final_numerator = tu * Bden + tv * Aden
    elif Aden == Bden:
        final_numerator = tu + tv
    return final_numerator
def visual (a, b):
    if a>b:
        return len(str(a)) * '-'
    else:
        return len(str(b)) * '-'

Anum = int(input("Enter number`s A numerator: "))
Aden = int(input("Enter number`s A denominator: "))
Bnum = int(input("Enter number`s B numerator: "))
Bden = int(input("Enter number`s B denominator: "))
denominator = biggest_denominator(Aden, Bden)
numerator = addition(Anum, Bnum)

print("""
%i   %i   %i
%s + %s = %s
%i   %i   %i
""" % (Anum, Bnum, numerator , visual(Anum, Aden), visual(Bnum, Bden), visual(numerator, denominator), Aden, Bden, denominator))