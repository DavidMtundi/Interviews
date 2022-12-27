
# lambda functions
funcaddtwonumbers = lambda x ,y : x +y
print(funcaddtwonumbers(10 ,20))

valuearray = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
funcodd = list(filter(lambda x : x % 2==0 ,valuearray))

unsortednames = ["david","chacha","brian","brael","stepen","allan","mutundi"]
sortedwithoutlambda =sorted(unsortednames)
sortedounes = sorted(unsortednames,key=lambda x:x.split()[-1].lower())


unsortedlastnames = ["david zero","allan mutai","steve chacha","mike nganga"]
sortedlastnameswithlambda = sorted(unsortedlastnames,key=lambda x:x.split()[-1],reverse=True)

unsortedintegers=[[1,6],[2,7],[1,5],[3,9]]
sortedintegerswithlambda = sorted(unsortedintegers,key=lambda x:x[-1])

unsortedmap = {"a":5,"b":4,"c":7,"d":2,"t":20}
sortedmapwithlambda = sorted(unsortedmap.items(),key=lambda x:x[1])
print(funcodd)
print(sortedounes)
print(sortedwithoutlambda)
print(sortedmapwithlambda)
print(sortedlastnameswithlambda)
print(sortedintegerswithlambda)