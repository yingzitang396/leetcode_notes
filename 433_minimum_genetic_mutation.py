class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        queue = deque ([startGene])
        visited = {startGene}
        step = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                cur = queue.popleft()
                if cur == endGene:  
                    return step
                gene = ['A', 'C', 'G', 'T']
                for i in range(len(cur)):
                    for j in gene:
                        if j != cur[i]:
                            gene_list = list(cur)
                            gene_list[i] = j
                            new_glist = "".join(gene_list) 
                            if new_glist in bank_set and new_glist not in visited:
                                visited.add(new_glist)
                                queue.append(new_glist)
            step += 1
        return -1



        """
        注意step是在一个for循环之后再加的，因为考虑到起步就是endGene，在这可能append进queue的有两个startGene变体，所以都是属于一层的最短路径
        其次要看那可能"".join()这个语法是拼起来之前修改的list注意一下
        如果是for j in gene其实就是字符可以直接用不用再用下标遍历
        """