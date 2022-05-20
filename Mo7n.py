class Ghada:
    def love(self, gold):

        engagement = len(gold) - 1 # n - 1 = 4
        mwasem = len(gold) - 1 # n - 2 = 3
        idx = 0

        while idx <= engagement:
            for i in range(mwasem):
                if gold[i] > gold[i+1]:
                    gold[i], gold[i+1] = gold[i+1], gold[i]
                else:
                    i += 1
            idx += 1
        return gold
                    




print(Ghada().love([1,2,3,4]))
print(Ghada().love([5,6,2,3,1]))
print(Ghada().love([5,8]))
print(Ghada().love([5,6,2,3]))
print(Ghada().love([5]))
print(Ghada().love([]))



