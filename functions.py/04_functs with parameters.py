def rectArea(length,width):
    print(f"Area of rectangle is {width*length} ")
def rectpara(length,width):
    print(f"parameter  of rectangle is {width*2+2*length} ")

length = int(input("Enter length of rectangle"))
width = int(input("Enter width of rectangle"))
rectArea(length ,width)
rectpara(length,width)