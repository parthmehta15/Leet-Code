class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        pixels = set()
        init_color = image[sr][sc]
        pixels.add((sr,sc))

        m,n = len(image), len(image[0])

        if image[sr][sc] == color:
            return image

        while len(pixels)!=0:
            # print(pixels)
            
            sr, sc = pixels.pop()

            if sr-1>=0:
                if image[sr-1][sc] == image[sr][sc]:
                    pixels.add((sr-1,sc))

            if sr+1<m:
                if image[sr+1][sc]== image[sr][sc]:
                    pixels.add((sr+1,sc))

            if sc-1>=0:
                if image[sr][sc-1]== image[sr][sc]:
                    pixels.add((sr,sc-1))
            
            if sc+1<n:
                if image[sr][sc+1]== image[sr][sc]:
                    pixels.add((sr,sc+1))

            image[sr][sc] = color
            # print(image)

        return image
