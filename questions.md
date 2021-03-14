I forgot, we didnt have the actual lesson last time. So, I made an introductory assignment to the next chapter. If you have any questions, as always, let me know. Also, the **[O(n)]** is just an introduction to some advanced concepts, ignore when working on the problems. ***All functions must return the 'output' value***

__Write a function that returns the largest element in a list. If there is no largest, return float('-inf')__ *(loops, conditionals, lists)* **[O(n)]**
```
**Use function signature: def question1(list):**
Ex:
input: [1, 3, 6, 9, 3, 24, 64, 6]
output: 64

Ex2:
input: [1, 3, 44, 200, 200]
output: 200
```
__Write a function that checks whether an element occurs in a list.__ *(loops, conditionals, lists)* **[O(n)]**
```
**Use function signature: def question2(element, list):**
Ex:
input: 4, [1, 2, 3, 4]
output: 4 occurs in the list

Ex2:
input: 5, [1, 4, 6, 2]
output: 5 does not occur in the list
```
__Write a function that returns the elements on odd positions in a list.__ *(loops, conditionals, lists)* **[O(n)]**
```
**Use function signature: def question3(list):**
Ex:
input: [1, "jack", "boop"]
output: [1, "boop"]
```
__Write a function that takes two lists(of integers), listA and listB, and multiplies every number of listA with listB.__ *(loops, nested loops, lists)* **[O(n^2)]**
```
**Use function signature: def question4(listA, listB):**
Ex: 
input: [0, 1],[1, 2]
output: [0, 0, 1, 2]

Ex2:
input: [1, 2, 3], [4, 5, 6]
output: [4, 5, 6, 8, 10, 12, 12, 15, 18]
```
__Write function that reverses a list, preferably in place. "In place" means to use the same original (input) container as the output of the operation, without creating any more containers. Variables are permitted for "In place" functions. (this might be tough. You don't have to do it "in place" if you dont want)__ *(loops, nested loops, lists)* **[O(n)]**
```
**Use function signature: def question5(list):**
Ex: 
input: ["b", "o", "b", "b", "y"]
output: ["y", "b", "b", "o", "b"]
```