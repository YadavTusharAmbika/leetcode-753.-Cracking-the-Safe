step 1

create empty memory
store combination we already used
final answer being built
starting node like 0,00,00
if n=3 the start from 00*


step 2 dfs function
we are trying all didgit from 0 to k-1
cause if we don't 
then n=3,k=10
total possib 
000,001,002 etc 
we also used for overlapping to avoid wasting times 
n=2,k=2 (n-1)
4
4+2-1
5
(01100)


step 3 create newpassword piece
if node is 01 and i = 1
then edge =011

sreep 4 if not used before
we dont repetat same pass again

step 5 move forward
we drop the first didgit to keeep length n-1

step 6 add digit after exploring deeper

step 7 :- start dfs

step 8 build final ans

we reverse the result list and attach the starting string
during dfs e keep doing
res.append str (i
instead of 0,1,1,0 we store 0,0,1,1, (backtracking order
res[::-1
reverse the list reverse (0,0,1,1
then 1,1,0,0,
.join (1,1,0,0,
1100

start +.....
if n = 2 n-1
start from 0 +0+1100+"01100
