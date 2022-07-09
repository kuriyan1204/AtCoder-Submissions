from collections import defaultdict


class UnionFind:
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


n = int(input())
sx, sy, tx, ty = map(int, input().split())
xs = []
ys = []
rs = []
s_places = []
t_places = []
uf = UnionFind(n)

for i in range(n):
    x, y, r = map(int, input().split())
    xs.append(x)
    ys.append(y)
    rs.append(r)

for i in range(n):
    s_yes = False
    t_yes = False
    if (sx - xs[i]) ** 2 + (sy - ys[i]) ** 2 == rs[i] ** 2:
        s_yes = True
    if (tx - xs[i]) ** 2 + (ty - ys[i]) ** 2 == rs[i] ** 2:
        t_yes = True

    if s_yes and t_yes:
        print("Yes")
        exit()
    if s_yes:
        s_places.append(i)
    if t_yes:
        t_places.append(i)

    for j in range(i):
        d2 = (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2
        if (rs[i] - rs[j]) ** 2 <= d2 <= (rs[i] + rs[j]) ** 2:
            uf.unite(i, j)

for s_place in s_places:
    for t_place in t_places:
        if uf.same(s_place, t_place):
            print("Yes")
            exit()
print("No")
