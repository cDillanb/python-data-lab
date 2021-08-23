cupcake_invoices = open('CupcakeInvoices.csv')

total = 0

chocolate = 0
vanilla = 0
strawberry = 0


for line in cupcake_invoices:
    print(line)

    line = line.split(",")
    print(line[2])

    number = 0
    number += float(line[3]) * float(line[4])
    print(number)

    total += float(line[3]) * float(line[4])

    if line[2] == 'Chocolate':
        chocolate += float(line[3]) * float(line[4])
    elif line[2] == 'Vanilla':
        vanilla += float(line[3]) * float(line[4])
    else:
        strawberry += float(line[3]) * float(line[4])
    
print(total)

print(chocolate, vanilla, strawberry)

cupcake_invoices.close()