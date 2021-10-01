def majority(elements):
    thisdict = {}
    for i in elements:
        if i not in thisdict:
            thisdict[i]=1
        else:
            thisdict[i]+=1
    for i in thisdict.values():
        if i > len(elements)/2:
            return 1
    return 0

def main():
    num_elements = int(input())
    elemets = [int(x) for x in input().split()]
    assert len(elemets) == num_elements
    print(majority(elemets))
main()