class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        num_satisfied = window = total_window = 0
        left = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                num_satisfied += customers[i]

        for right in range(len(grumpy)):
            
            while (right - left) + 1 > minutes:
                if grumpy[left] == 1:
                    window -= customers[left]
                left += 1

            if grumpy[right] == 1:
                window += customers[right]
            
            total_window = max(total_window, window)
        
        return num_satisfied + total_window
            