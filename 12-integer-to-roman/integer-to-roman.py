class Solution:
    def intToRoman(self, num: int) -> str:
        # Map of Roman numerals in descending order
        val_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        roman = ""
        
        # Iterate through the values from largest to smallest
        for value, symbol in val_to_roman:
            if num == 0:
                break
            count = num // value  # How many times the symbol fits
            roman += symbol * count
            num -= value * count  # Reduce the number
            
        return roman