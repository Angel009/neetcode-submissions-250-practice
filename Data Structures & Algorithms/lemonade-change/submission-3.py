class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_b = ten_b = 0

        for bill in bills:
            if bill == 20:
                if five_b > 0 and ten_b > 0:
                    five_b -= 1
                    ten_b -= 1
                elif five_b >= 3:
                    five_b -= 3
                else:
                    return False

            elif bill == 10:
                if five_b > 0:
                    five_b -= 1
                    ten_b += 1
                else:
                    return False
            
            else:
                five_b += 1
        
        return True