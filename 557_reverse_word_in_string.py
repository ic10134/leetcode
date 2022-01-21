#Given a string s, reverse the order of characters in each word within a 
# sentence while still preserving whitespace and initial word order.

def reverseWords(s: str) -> str:
    tokens = list(s.split(" "))
    s_reversed =[]
    for i in range(len(tokens)):
        if i == 0:
            s_reversed = tokens[i][::-1]
        else:
            s_reversed += " " + tokens[i][::-1]

    return s_reversed

s = "Let's take LeetCode contest"
print(reverseWords(s))