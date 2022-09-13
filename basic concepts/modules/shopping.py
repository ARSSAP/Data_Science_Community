def product_list(rang):
    products=[]
    rate=[]
    for i in range(rang):
        takein=input("enter your product name:")
        ratein=int(input("enter your product rate:"))
        products.append(takein)
        rate.append(ratein)
    for j in range(len(products)):
        print("",j+1,"products: ", products[j]," rate: ", rate[j], "\n")        

    
product_list(3)