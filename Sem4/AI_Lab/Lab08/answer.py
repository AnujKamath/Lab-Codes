use = [0] * 10  # Set to 1 when a character is assigned previously

def is_valid(node_dict, s1, s2, s3):
    val1 = sum(node_dict[ch] * 10 ** (len(s1) - i - 1) for i, ch in enumerate(s1) if node_dict[ch] !=-1)
    val2 = sum(node_dict[ch] * 10 ** (len(s2) - i - 1) for i, ch in enumerate(s2) if node_dict[ch] !=-1)
    val3 = sum(node_dict[ch] * 10 ** (len(s3) - i - 1) for i, ch in enumerate(s3) if node_dict[ch] !=-1)
    return val3 == val1 + val2

def permutation(node_dict, chars, n, s1, s2, s3):
    if n == len(chars):
        if is_valid(node_dict, s1, s2, s3):
            print(node_dict)
        return is_valid(node_dict, s1, s2, s3)
    if node_dict[chars[n]]!=-1:
        return permutation(node_dict, chars, n + 1, s1, s2, s3)
    for i in range(10):
        if not use[i]:
            ch = chars[n]
            node_dict[ch] = i
            use[i] = 1
            if permutation(node_dict, chars, n + 1, s1, s2, s3):
                return True
            use[i] = 0
            node_dict[ch] = -1
    return False

def solve_puzzle(s1, s2, s3):
    unique_chars = set(s1 + s2 + s3)
    if len(unique_chars) > 10:
        print("Invalid strings")
        return False
    node_dict = {ch: -1 for ch in unique_chars}
    if len(s1)==len(s2) and len(s1)<len(s3):
        node_dict[s3[0]]=1
        use[1]=1

    return permutation(node_dict, list(unique_chars), 0, s1, s2, s3)

def main():
    s1 = "MIT"
    s2 = "MANIPAL"
    s3 = "MITMAHE"
    
    if not solve_puzzle(s1, s2, s3):
        print("No solution")

if __name__ == "__main__":
    main()
