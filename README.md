# NFA2DFA
Convert a Non-Finite automata to a Definite Automata using CLI Python. (Limited to 2 characters)

## CODE EXECUTION
- `python src.py` (Windows)
- `python3 src.py` (Linux)
  
## PROCEDURE FOR EXECUTION
1. INPUT THE NUMBER OF NODES IN NFA.
2. INPUT THE ENTRY SYMBOLS.
3. INPUT IF THE STATE IS A FINAL STATE OR NOT.
4. INPUT EACH TRANSITION MOVEMENT OVER NODES BASED ON SYMBOL, 
   1. IF DONE WITH INPUTS ENTER -1.     
   2. NODE CONVENTION: q<number> e.g. q1
5. IF INVALID REPEAT STEP 3.
6. ONCE ALL INPUTS ARE DONE, DISPLAY OF NFA AND DFA WILL BE SHOWN.

## SAMPLE OUTPUT
```ENTER THE NUMBER OF NODES: 3
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
```
