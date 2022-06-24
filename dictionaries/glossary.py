# a dictionary 
glossary = {
    "glossary":"a list of technical or special words, especially those in a particular text, explaining their meanings",
    "indent":"to start a line of print or block of text further away from the edge of the page than the other lines",
    "key-value":"is a set of values associated with each other",
    "dictionary":"in Python is a collection of key-value pairs",
    "falsifiable":"capable of being tested (verified or falsified) by experiment or observation"
}

for word in glossary:
    print(f"{word.title()}:\n\t{glossary[word]}\n")