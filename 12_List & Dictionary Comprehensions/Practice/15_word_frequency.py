words = ["Python", "Java", "Machine", "Python", "C", "AI", "Python"]

frequency = {
    
    word: words.count(word)
    for word in set(words)
    
}

print(frequency)