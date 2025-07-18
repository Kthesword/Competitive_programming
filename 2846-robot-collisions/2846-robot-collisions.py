class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = {v: i for i, v in enumerate(positions)}
        # print(robots)
        stack =  []
        for p in sorted(positions):
            i = robots[p]
            if directions[i] == "L":
                while stack and healths[i]:
                    top = stack.pop()
                    if healths[i] == healths[top]:
                        healths[i] = healths[top] = 0
                        
                    elif healths[top] < healths[i]:
                        healths[top] = 0
                        healths[i] -= 1
                    else:
                        healths[top] -= 1
                        healths[i] = 0
                        stack.append(top)

            else:
                stack.append(i)
        # print(stack)
        return [h for h in healths if h]
                
            


        