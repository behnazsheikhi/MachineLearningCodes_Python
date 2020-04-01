def maskify(cc):
    output=''
    length=len(cc)
    if length>=4:
       lask_char=length-4
       for i in range(0,length):
           if (i>=lask_char):
             output=output+cc[i]
           else:
             output=output+'#'
    else:
        output=cc
    print(output)
a=input('Enter input')
maskify(a)
