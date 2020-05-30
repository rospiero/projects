#box print function

"""
*******************
*                 *
*                 *
*                 *
*******************
"""
def boxPrint (symbol, width, height):
    if len(symbol)!=1:
        raise Exception('"symbol" needs to a string of lenght 1')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol+(' ' * (width - 2))+ symbol)

    print(symbol * width)

boxPrint("*", 5 , 5)
boxPrint("2",12,3)
