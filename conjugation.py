def determineConjugation(wordParts):
	verb = wordParts[0]
	infinitive = wordParts[1]
	verbEnding = verb[-2] + verb[-1]
	if verbEnding[-2] not in "ei":
		verbEnding = verbEnding[-1]
	infEnding = infinitive[-3] + infinitive[-2] + infinitive[-1]
	
	if infEnding == "are":
		return "1"

	if infEnding == "ire":
		return "4"

	if verbEnding == "io" and infEnding == "ere":
		return "3-io"

	if verbEnding == "eo" and infEnding == "ere":
		return "2"

	if verbEnding == "o" and infEnding == "ere":
		return "3"