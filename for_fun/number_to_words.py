def numberToWords(num):
    """
    Converts integer to string of the number written out in English. Submission to this LeetCode problem: https://leetcode.com/problems/integer-to-english-words/

    :type num: int
    :rtype: str
    """
    less_than_twenty = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    
    less_than_hundred = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    
    hundred_and_up = {
        100: 'Hundred',
        1000: 'Thousand',
        1000000: 'Million',
        1000000000: 'Billion'
        
    }
    

    if num == 0:
        return 'Zero'
    elif num < 20:
        return less_than_twenty.get(num)
    elif num < 100:
        word = less_than_hundred.get(num // 10)
        if num % 10 > 0:
            return ' '.join([word, less_than_twenty.get(num % 10)])
        else:
            return word   
    else:
        largest = 0
        for key in sorted(hundred_and_up):
            if num >= key:
                largest = key
            else:
                break

        rem = num % largest
        if rem > 0:
            return ' '.join([numberToWords(num // largest), hundred_and_up.get(largest), numberToWords(rem)])
        else:
            return ' '.join([numberToWords(num // largest), hundred_and_up.get(largest)])


