ones, tens, teens = { 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine" }, { 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety" },{ 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen" }
n = int(input("Enter a number: "))


print((ones[int(n/1000)] + " thousand " if(n >= 1000 and n/1000 > 0) else "") + (ones[int(n%1000/100)] + " hundred" if(n >= 100 and int(n%1000/100) > 0) else "") + (" and " if((n%1000/100 > 0 or n/1000 > 0) and (n%1000%100/10 > 0 or n%1000%100%10 > 0) and n >= 100) else "") + (tens[int(((n%1000)%100)/10)] if(n >= 10 and n%1000%100/10 >= 2) else "")  + (teens[int(((n%1000)%100))] if(n >= 10 and (n%1000%100/10 if(n >1000) else n%100/10 if(n > 100) else n/10) < 2 and (n%1000%100 if(n >1000) else n%100 if(n > 100) else n) > 9) else "") + (ones[int(n%1000%100%10)] if(n >= 1 and (n%1000%100/10 if(n >1000) else n%100/10 if(n > 100) else n/10) < 2 and (n%1000%100 if(n >1000) else n%100 if(n > 100) else n) < 10) else ""))

