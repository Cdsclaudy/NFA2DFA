'''
TITLE            : CONVERSION OF A NFA TO A DFA.
DESCRIPTION      : The given program converts an NFA to a DFA, by taking in symbols of input and number of nodes of the DFA, and outputs a DFA.
'''

#1. INITIAL INPUT
n=int(input("ENTER THE NUMBER OF NODES: "))
s1=input("ENTER THE INPUT CHARACTER 1: ")
s2=input("ENTER THE INPUT CHARACTER 2: ")


#2. CREATION OF AN NFA MODEL-WITH INPUTS FROM q0 to qn
d=dict()
for i in range(n):
    d['q'+str(i)]={s1:{},s2:{}}

#3. INPUT OF THE NFA FOR EACH NODE OVER EACH SYMBOL
for i in d:
    ch=' '
    ch2=input("Is "+i+" a final state? Y/any ")
    d[i]['f']=1 if(ch2=='Y') else 0
    print("THE FOLLOWING ENTRY IS FOR NODE ",i)
    while(ch!='-1'):
        ch=input("Enter the nodes for movement over "+s1+" else enter -1 for end of input ")
        if(ch in d.keys()):
            s=set(d[i][s1])
            s.add(ch)
            d[i][s1]=s
        elif(ch!='-1'):
            print("INVALID INPUT ENTER AGAIN ")
    print("Movement for node ",i," through",s1," is done")
    print()
    ch=' '
    print("THE FOLLOWING ENTRY IS FOR NODE",i)
    while(ch!='-1'):
        ch=input("Enter the nodes for movement over "+s2+" else enter -1 for end of input ")
        if(ch in d.keys()):
            s=set(d[i][s2])
            s.add(ch)
            d[i][s2]=s
        elif(ch!='-1'):
            print("INVALID INPUT ENTER AGAIN")
    print("Movement for node ",i," through ",s2," is done")
    print()
print()
print()

#4. DISPLAY OF THE NFA
print("YOUR NFA LOOKS LIKE THIS")
for i in d:
    if(d[i]['f']==1):
        print("||",i,"||*",end='')
    else:
        print("|",i,"|",end='')
    print("(",s1,")----->","|",d[i][s1],"|")

    if(d[i]['f']==1):
        print("||",i,"||*",end='')
    else:
        print("|",i,"|",end='')
    print("(",s2,")----->","|",d[i][s2],"|")
    print()
    print()
print()

#5. CONVERSION OF NFA TO DFA
dfa=dict()
dfa[frozenset({'q0'})]=d['q0']
s=set(d['q0'][s1])

def createnull():   #CREATES NEW NODES FROM TRANSITION TABLE
    c=0
    s=[]
    for i in dfa:
        if not(frozenset(dfa[i][s1]) in dfa):      
            s.append(frozenset(dfa[i][s1]))
            c+=1
        
        if not(frozenset(dfa[i][s2]) in dfa):      
            s.append(frozenset(dfa[i][s2]))
            c+=1
    for i in s:
        dfa[i]=2
    return s

def countnull():    #COUNTS THE NUMBER OF NODES FOR WHICH INPUT HAS NOT BEEN COMPLETED
    c=0
    for i in dfa:
        if(type(dfa[i]) is int):
            c+=1
    return(c)
a=createnull()
while(countnull()!=0):
    for i in a:
        dfa[i]={s1:{},s2:{}}
        fincheck=0
        if(len(set(i))==0):
            dfa[i]['f']=0
            dfa[i][s1]={}
            dfa[i][s2]={}
        for j in i:
            if not('f' in dfa[i]):
                dfa[i]['f']=0
            if(d[j]['f']==1 and fincheck==0):
                dfa[i]['f']=1
                fincheck=1

            S=set(d[j][s1])
            S1=set(dfa[i][s1])
            S1.update(S)
            dfa[i][s1]=S1

            S=set(d[j][s2])
            S1=set(dfa[i][s2])
            S1.update(S)
            dfa[i][s2]=S1
    a=createnull()

#6. DISPLAY OF THE CONVERTED DFA 
print("DESIGN YOUR DFA LIKE THIS:")
for i in dfa:
    if(dfa[i]['f']==1):
        print("||",set(i),"||*",end='')
    elif(len(set(i))==0):
        print("|{}|",end='')
    else:
        print("|",set(i),"|",end='')
    if(dfa[frozenset(dfa[i][s1])]['f']==1):
        print("(",s1,")----->","||",dfa[i][s1],"||*")
    elif(len(set(dfa[i][s1]))==0):
        print("(",s1,")----->|{}|")
    else:
        print("(",s1,")----->","|",dfa[i][s1],"|")

    if(dfa[i]['f']==1):
        print("||",set(i),"||*",end='')
    elif(len(set(i))==0):
        print("|{}|",end='')
    else:
        print("|",set(i),"|",end='')
    if(dfa[frozenset(dfa[i][s2])]['f']==1):
        print("(",s2,")----->||",dfa[i][s2],"||*")
    elif(len(set(dfa[i][s2]))==0):
        print("(",s2,")----->|{}|")
    else:
        print("(",s2,")----->","|",dfa[i][s2],"|")

    print()
    print()

'''

PROCEDURE FOR OUTPUT
STEP 1: INPUT NUMBER OF NODES IN NFA.
STEP 2: INPUT THE ENTRY SYMBOLS.
STEP 3: INPUT IF THE STATE IS A FINAL STATE OR NOT.
STEP 4: INPUT EACH TRANSITION MOVEMENT OVER NODES BASED ON SYMBOL, IF DONE WITH INPUTS ENTER -1. NODE CONVENTION: q<number> e.g. q1
STEP 5: IF INVALID REPEAT STEP 3.
STEP 6: ONCE ALL INPUTS ARE DONE, DISPLAY OF NFA AND DFA WILL BE SHOWN.

OUTPUT SAMPLE:
ENTER THE NUMBER OF NODES: 3
ENTER THE INPUT CHARACTER 1: a
ENTER THE INPUT CHARACTER 2: b
Is q0 a final state? Y/any N
THE FOLLOWING ENTRY IS FOR NODE  q0
Enter the nodes for movement over a else enter -1 for end of input q0
Enter the nodes for movement over a else enter -1 for end of input q1
Enter the nodes for movement over a else enter -1 for end of input -1
Movement for node  q0  through a  is done

THE FOLLOWING ENTRY IS FOR NODE q0
Enter the nodes for movement over b else enter -1 for end of input q1
Enter the nodes for movement over b else enter -1 for end of input -1
Movement for node  q0  through  b  is done

Is q1 a final state? Y/any Y
THE FOLLOWING ENTRY IS FOR NODE  q1
Enter the nodes for movement over a else enter -1 for end of input q2
Enter the nodes for movement over a else enter -1 for end of input -1
Movement for node  q1  through a  is done

THE FOLLOWING ENTRY IS FOR NODE q1
Enter the nodes for movement over b else enter -1 for end of input q2
Enter the nodes for movement over b else enter -1 for end of input -1
Movement for node  q1  through  b  is done

Is q2 a final state? Y/any N
THE FOLLOWING ENTRY IS FOR NODE  q2
Enter the nodes for movement over a else enter -1 for end of input -1
Movement for node  q2  through a  is done

THE FOLLOWING ENTRY IS FOR NODE q2
Enter the nodes for movement over b else enter -1 for end of input q2
Enter the nodes for movement over b else enter -1 for end of input -1
Movement for node  q2  through  b  is done



YOUR NFA LOOKS LIKE THIS
| q0 |( a )-----> | {'q1', 'q0'} |        
| q0 |( b )-----> | {'q1'} |


|| q1 ||*( a )-----> | {'q2'} |
|| q1 ||*( b )-----> | {'q2'} |


| q2 |( a )-----> | {} |
| q2 |( b )-----> | {'q2'} |



DESIGN YOUR DFA LIKE THIS:
| {'q0'} |( a )-----> || {'q1', 'q0'} ||*
| {'q0'} |( b )----->|| {'q1'} ||*


|| {'q1', 'q0'} ||*( a )-----> || {'q2', 'q0', 'q1'} ||*
|| {'q1', 'q0'} ||*( b )----->|| {'q2', 'q1'} ||*


|| {'q1'} ||*( a )-----> | {'q2'} |
|| {'q1'} ||*( b )-----> | {'q2'} |


|| {'q2', 'q0', 'q1'} ||*( a )-----> || {'q1', 'q0', 'q2'} ||*
|| {'q2', 'q0', 'q1'} ||*( b )----->|| {'q2', 'q1'} ||*


|| {'q2', 'q1'} ||*( a )-----> | {'q2'} |
|| {'q2', 'q1'} ||*( b )-----> | {'q2'} |


| {'q2'} |( a )----->|{}|
| {'q2'} |( b )-----> | {'q2'} |


|{}|( a )----->|{}|
|{}|( b )----->|{}|

'''
