def search(input_text,pattern_string):
    N=len(input_text)
    M=len(pattern_string)
    # A loop to slide pat[] one by one
    for i in xrange(N - M):

        # For current index i, check for pattern match
        for j in xrange(M):
            if input_text[i + j] != pattern_string[j]:
                break
        if j == M - 1:  # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)
print("Enter your text")
input_text=raw_input()
print("Enter your pattern string")
pattern_string=raw_input()
search(input_text,pattern_string)
#
#GHGRRDBFHHBFFBFGGH



