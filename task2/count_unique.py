def count_char(word):
    word=word.lower()
    visited=[]
    char_count={}
    n=len(word)
    for i in range(n):
        visited.append(False)
    for i in range(n):
        count=1
        for j in range(i+1,n):
            if word[i]==word[j] and visited[j]!=True:
                visited[j]=True
                count+=1
        if visited[i]!=True:
           char_count[word[i]]=count
    return char_count
         
value=count_char(input())
print(value)