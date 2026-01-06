class Solution:
    def crackSafe(self, n, k):
        
        seen = set()
        res = []
        start = "0" * (n - 1) 

        def dfs(node):
            for i in range(k):
                edge = node + str(i)
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    res.append(str(i))

        dfs(start)
        return start + "".join(res[::-1])



 // explaination is written in readme file , delete after coping the code  //
