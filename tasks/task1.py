def f(s):
    count = 0
    height = 0
    min_height = 0
    rises = 0  # Счётчик подъёмов на текущем участке
    start = 0
    for i in range(len(s)):
        if s[i] == 'П':
            height += 1
            rises += 1
        else:
            height -= 1
        if height < min_height:
            min_height = height
        if height == 0:
            if min_height >= 0 and rises >= 1 and i > start + 1:  # Участок длиннее ПС
                count += 1
            start = i + 1
            min_height = 0
            rises = 0
    return count


print(f('ППСС'))  
print(f('ПС'))    
print(f('ПППССС'))  
print(f('ППСПСС'))  
print(f('ППС'))  

