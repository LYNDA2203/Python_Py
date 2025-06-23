import random
class CounponCollector:
    def get_random_coupon(self,n):
        #generate a random number between 0 to n-1
        return random.randint(0,n-1)
    
    def collect_coupons(self,n):
        collected =set()
        count = 0
        while len(collected) < n:
            new_coupon = self.get_random_coupon(n)
            count += 1
            collected.add(new_coupon)
        return count
    
if __name__ == "__main__":
    n=int(input("Enter the number of distinct coupon numbers: "))
    collector = CounponCollector()
    total_random_numbers = collector.collect_coupons(n)
    print(f"Total random numbers generated to collect all {n} coupons:{total_random_numbers}")
    