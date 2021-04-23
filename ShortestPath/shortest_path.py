from typing import List


class FindPath:

	def __init__(self, matrix: List[List[int]]) -> None:
		self.matrix = matrix
		self.row = len(matrix)
		self.col = len(matrix[0])
		self.direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

	def shortest_path(self) -> int:
		left, right = 1, max(self.row, self.col)
		while left < right:
			mid = (left + right) // 2

		return 1

	def validate_path(self, ):