class Solution:
    def minMoves(
        self,
        classroom: List[str],
        energy: int
    ) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = []
        sr = sc = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        if k == 0:
            return 0

        id = [[-1] * n for _ in range(m)]

        for i, (r, c) in enumerate(litter):
            id[r][c] = i

        total_mask = 1 << k
        cells = m * n

        best = [-1] * (total_mask * cells)

        q = deque()
        q.append((sr, sc, 0, energy))

        best[sr * n + sc] = energy

        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == total_mask - 1:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    if id[nr][nc] != -1:
                        nmask |= 1 << id[nr][nc]

                    pos = nr * n + nc
                    idx = nmask * cells + pos

                    if best[idx] >= ne:
                        continue

                    best[idx] = ne
                    q.append((nr, nc, nmask, ne))

            moves += 1

        return -1