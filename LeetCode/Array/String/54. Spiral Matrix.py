class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        res = []

        m_start, m_end = 0, m - 1
        n_start, n_end = 0, n - 1

        while m_start <= m_end and n_start <= n_end:
            for j in range(n_start, n_end + 1):
                res.append(matrix[m_start][j])
            m_start += 1

            for i in range(m_start, m_end + 1):
                res.append(matrix[i][n_end])
            n_end -= 1

            for j in range(n_end, n_start - 1, -1):
                res.append(matrix[m_end][j])
            m_end -= 1

            for i in range(m_end, m_start - 1, -1):
                res.append(matrix[i][n_start])
            n_start += 1

        return res[:size]
