def scheta_sort():
    debetSaldo =0
    creditSaldo =0
    dohuya_platezhek = [2000, 1000, 3000, 4000, -1000, -2000, -3000, -200, -300]

    for platezhka in dohuya_platezhek:
       if platezhka < 0:
           creditSaldo=creditSaldo+platezhka
       elif  platezhka > 0:
           debetSaldo =debetSaldo+platezhka
    print(debetSaldo)
    print(creditSaldo)

scheta_sort()
