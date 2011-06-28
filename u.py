import unicodedata, json
l = list()
#for codeptx in range(0xE01EF):
for codeptx in range(0x2400):
    try:
        c = chr(codeptx)
        n = unicodedata.name(c)
        cat = unicodedata.category(c)
        #if True: print('[{0:2}] {1:<60}{2:>4}'.format(cat, n, c))
        obj = {'cpt': codeptx, 'c': c, 'n': n, 'cat': cat}
        l.append(obj)
    except ValueError:
        pass
print(json.dumps(l, indent=1))
