class Solution(object):
    def twoSum(self, nums, target):
        ah = []
        def cek(nums, target):
            cuy = [None, None]
            for index, value in enumerate(nums):
                hasil = abs(target - value)
                if hasil in nums[index + 1:]:
                    kanan = nums.index(hasil, index + 1)
                    kiri = index
                    cuy.append(kiri)
                    cuy.append(kanan)
                    break
            else:
                raise ValueError("data di list ga bisa nyampe target")

            return kiri, kanan
        try:
            satu, dua = cek(nums, target)
        except ValueError as e:
            print(f"Error: {e}")
            return ah
        ah.append(satu)
        ah.append(dua)
        return ah
