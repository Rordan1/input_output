#brother, sister, mom, dad, grandpa, grandma; add aunt and uncle later

parentes = ['irmão', 'irmã', 'mãe', 'Papai', 'Vovô', 'Avó']

amigos = ['curto', 'alta', 'gordo']

print(amigos + parentes)

not_going = 'Vovô'

parentes.remove(not_going)
print(amigos + parentes)

print(f"\n Unfortunately, {not_going} will no longer be able to attend " + "\n As well as")

popped = parentes.pop(-1)
print(popped)

#print(f"This is our new list of guests thus far " + "from the friends list" + amigos + "and from the relatives list" + parentes.pop())




