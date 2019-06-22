""" 2) A Pen has inkQty (int), colour (string) and can be used to write and refill. A text must be given for it to write.
A quantity must be given to refill. If there is ink then the pen will write the text given to it (SOP).
Refill works by taking in the int qty to add to the existing inkQty. First as a class designer, on paper apply OOAD and arrive at the class design.
Then create the class implementation and create a tester class to create 2 pen objects, give it inkQty and ask it to write.
What dunders are you implementing?
"""

class Pen():
    def __init__(self,qty,col):
        self.inqty = qty
        self.color = col
    def write(self,txt:"str"):
        if self.inqty > 0:
            print(txt)
            self.inqty = self.inqty - 5
            print("after writing txt, ink qty decreased to {}".format(self.inqty))
        else:
            print("no ink, refill pls!!!")


    def refill(self,qty:"int"):
        self.inqty = self.inqty + qty
        print ("ink qty increased to {} barko eega!!!!".format(self.inqty))
class Test(Pen):
    pass

p1 = Test(10,"red")
p1.write("bala and smi are pythoneers")
#p1.refill(10)
print(p1.inqty)
p1.write("calling again to test quantity of ink left")
p1.write("lets see now")
p1.refill(10)