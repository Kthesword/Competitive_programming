class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if not maxDoubles:
            return target - 1
        
        moves = 0
        while target > 1:
            if not target % 2:
                if maxDoubles:
                    target //= 2
                    moves += 1
                    maxDoubles -= 1
                else:
                    break
            else:
                moves += 1
                target -= 1

        moves += target - 1

        return moves
     
    