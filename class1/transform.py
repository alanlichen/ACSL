def transform(nstr, pos, dnum):
    # print(nstr, pos, dnum)
    # array of n
    newN = list(nstr)
    # get the digit at "pos" from last element of newN
    # (counting from last digit backwards)
    posIndex = len(newN) - pos
    posValue = int(newN[posIndex])
    # print(posValue, posIndex)

    if posValue in range(0, 4+1):
        # print('one')
        sum = posValue+dnum
        # make an array of sum
        s = list(str(sum))
        # find the ones place digit (last digit) of sum
        uniDig = s[len(s)-1]
        # set the digit at "pos" to the last digit of "sum"
        newN[posIndex] = uniDig
        # loop from the "pos" position from the right to the end of the array
        for digit in range(posIndex + 1, len(newN)):
            newN[digit] = '0'
        # join the new array of numbers and return it
        newVal = ''.join(newN)
        return newVal

    elif posValue in range(5, 9+1):
        # this check is not needed
        # print('two')
        # get absolute value
        abv = abs(posValue-dnum)
        # make an array of abv
        s = list(str(abv))
        # find the ones place digit (last digit) of sum
        firDig = s[0]
        # set the digit at "pos" to the last digit of "sum"
        newN[posIndex] = firDig
        # loop from the "pos" position from the right to the end of the array
        for digit in range(posIndex + 1, len(newN)):
            newN[digit] = '0'
        # join the new array of numbers and return it
        newVal = ''.join(newN)
        return newVal