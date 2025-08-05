from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_length = len(image)
        column_length = len(image[0])
        start = image[sr][sc]
        if color == start:
            return image
        self.fourDirectionalCheck(image, sr, sc, start, color, row_length, column_length)
        image[sr][sc] = color
        return image

    def isValidRow(self, row_idx: int, row_length: int):
        print(row_idx, row_length)
        return row_idx < row_length and row_idx >=0

    def isValidColumn(self, column_idx: int, column_length: int):
        return column_idx < column_length and column_idx >=0

    def fourDirectionalCheck(self, image: List[List[int]], sr, sc, start, color, row_length, column_length):
        # sr+1, sc; sr-1, sc; sr, sc+1; sr, sc-1
        print(image)
        if self.isValidRow(sr+1, row_length):
            if image[sr+1][sc] == start:
                image[sr+1][sc] = color
                self.fourDirectionalCheck(image, sr+1, sc, start, color, row_length, column_length)
        if self.isValidRow(sr-1, row_length):
            if image[sr-1][sc] == start:
                image[sr-1][sc] = color
                self.fourDirectionalCheck(image, sr-1, sc, start, color, row_length, column_length)
        if self.isValidColumn(sc+1, column_length):
            if image[sr][sc+1] == start:
                image[sr][sc+1] = color
                self.fourDirectionalCheck(image, sr, sc+1, start, color, row_length, column_length)
        if self.isValidColumn(sc-1, column_length):
            if image[sr][sc-1] == start:
                image[sr][sc-1] = color
                self.fourDirectionalCheck(image, sr, sc-1, start, color, row_length, column_length)
        return

    def printAnswer(self, answer):
        print(answer)

    # DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        start_color = image[sr][sc]
        
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != start_color: return
            
            image[x][y] = color
            
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        
        flood_fill(sr, sc)
        return image

if __name__ == "__main__":
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    color = 0
    x = Solution()
    x.printAnswer(x.floodFill(image,sr,sc,color))