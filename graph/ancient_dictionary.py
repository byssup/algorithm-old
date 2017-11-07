
ALPHABET_SIZE = 26
START_VAL = 97


class Solver():

    def __init__(self, words):
        self.words = words
        self.visited = [False] * ALPHABET_SIZE
        self.graph = [[0 for _ in range(ALPHABET_SIZE)] for _ in range(ALPHABET_SIZE)]
        self.order = []

    def solve(self):
        self.create_graph()
        for i in range(ALPHABET_SIZE):
            if not self.visited[i]:
                self.dfs(i)
        self.order.reverse()
        for i in range(ALPHABET_SIZE):
            for j in range(i + 1, ALPHABET_SIZE):
                if self.graph[self.order[j]][self.order[i]] == 1:
                    return 'INVALID HYPOTHESIS'
        return ''.join([chr(START_VAL + num) for num in self.order])

    def create_graph(self):
        for i, pre_word in enumerate(self.words[:-1]):
            cur_word = self.words[i+1]
            for j in range(min(len(pre_word), len(cur_word))):
                if cur_word[j] != pre_word[j]:
                    ii = ord(pre_word[j]) - START_VAL
                    jj = ord(cur_word[j]) - START_VAL
                    self.graph[ii][jj] = 1
                    break

    def dfs(self, i):
        self.visited[i] = True
        for j in range(ALPHABET_SIZE):
            if self.graph[i][j] == 1 and not self.visited[j]:
                self.dfs(j)
        self.order.append(i)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        words = []
        for _ in range(int(raw_input())):
            words.append(raw_input())
        solver = Solver(words)
        print solver.solve()