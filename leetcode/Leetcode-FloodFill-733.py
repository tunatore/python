
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        if image[sr][sc] == newColor:
            return image

        color = image[sr][sc]
        self.fillImage(image, sr, sc, color, newColor)
        return image

    def fillImage(self, image, sr, sc, color, newColor):
        if (sr < 0 or sr >= len(image)) or (sc < 0 or sc >= len(image[0])) or (image[sr][sc] != color):
            return

        image[sr][sc] = newColor
        self.fillImage(image, sr + 1, sc, color, newColor)
        self.fillImage(image, sr - 1, sc, color, newColor)
        self.fillImage(image, sr, sc + 1, color, newColor)
        self.fillImage(image, sr, sc - 1, color, newColor)


s = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc, newColor = 1, 1, 2
print(s.floodFill(image, sr, sc, newColor))
