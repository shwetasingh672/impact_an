from collections import OrderedDict
import sys

class Cardboard(object):
    def __init__(self, inp):
        self.inp = inp

    def find_intersect(self):
        od = OrderedDict()
        for item in self.inp:
            height = int(item[2])
            for i in range(int(item[0]), int(item[1])):
                if i not in od:
                    od[i] = height
                else:
                    if height > od[i]:
                        od[i] = height
            if int(item[1]) not in od:
                od[int(item[1])] = 0
                
        output = []

        prev_height = -1

        for i, item in enumerate(od.items()):
            if i == 0:
                output.append(item)
                prev_height = item[1]
            else:
                if item[1] != prev_height:
                    output.append(item)
                    prev_height = item[1]
                else:
                    continue
                
        return output
        
def main():
    inp = []
    line = input("Enter the list of tuples:\n")
    while(line != ''):
        inp.append(tuple(line.split())) 
        line = input() 

    rec = Cardboard(inp)
    print(rec.find_intersect())


if __name__ == '__main__':
    sys.exit(main())
            
