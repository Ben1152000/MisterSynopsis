
def determineAnswer(conj,pps,form):
	reference1 = {"singular":{"1st person":0,"2nd person":1,"3rd person":2},"plural":{"1st person":3,"2nd person":4,"3rd person":5}}
	reference2 = {"present":0,"imperfect":1,"future":2}
	reference3 = {"1":0,"2":1,"3":2,"3-io":3,"4":4}
	reference4 = {"active":0,"passive":1}
	reference5 = {"perfect":0,"pluperfect":1,"future perfect":2}

	personal1 = [["o","as","at","amus","atis","ant"],["abam","abas","abat","abamus","abatis","abant"],["abo","abis","abit","abimus","abitis","abunt"]]
	personal2 = [["eo","es","et","emus","etis","ent"],["ebam","ebas","ebat","ebamus","ebatis","ebant"],["ebo","ebis","ebit","ebimus","ebitis","ebunt"]]
	personal3 = [["o","is","it","imus","itis","unt"],["ebam","ebas","ebat","ebamus","ebatis","ebant"],["am","es","et","emus","etis","ent"]]
	personal3i = [["io","is","it","imus","itis","unt"],["iebam","iebas","iebat","iebamus","iebatis","iebant"],["iam","ies","iet","iemus","ietis","ient"]]
	personal4 = [["io","is","it","imus","itis","unt"],["iebam","iebas","iebat","iebamus","iebatis","iebant"],["iam","ies","iet","iemus","ietis","ient"]]
	active = [personal1,personal2,personal3,personal3i,personal4]

	passive1 = [["or","aris","atur","amur","amini","antur"],["abar","abaris","abatur","abamur","abamini","abantur"],["abor","aberis","abitur","abimur","abimini","abuntur"]]
	passive2 = [["eor","eris","etur","emur","emini","entur"],["ebar","ebaris","ebatur","ebamur","ebamini","ebantur"],["ebor","eberis","ebitur","ebimur","ebimini","ebuntur"]]
	passive3 = [["or","eris","itur","imur","imini","untur"],["ebar","ebaris","ebatur","ebamur","ebamini","ebantur"],["ar","eris","etur","emur","emini","entur"]]
	passive3i = [["ior","iris","itur","imur","imini","iuntur"],["iebar","iebaris","iebatur","iebamur","iebamini","iebantur"],["iar","ieris","ietur","iemur","iemini","ientur"]]
	passive4 = [["ior","iris","itur","imur","imini","iuntur"],["iebar","iebaris","iebatur","iebamur","iebamini","iebantur"],["iar","ieris","ietur","iemur","iemini","ientur"]]
	passive = [passive1,passive2,passive3,passive3i,passive4]

	complete = [active,passive]

	active_perfect = [["i","isti","it","imus","istis","erunt"],["eram","eras","erat","eramus","eratis","erant"],["ero","eris","erit","erimus","eritis","erint"]]
	passive_perfect = [["sum","es","est","sumus","estis","sunt"],["eram","eras","erat","eramus","eratis","erant"],["ero","eris","erit","erimus","eritis","erunt"]]

	conjugated = pps[1][:-3]

	if "perfect" in form[2]:
		if form[3]=="active":
			conjugated = pps[2][:-1] + active_perfect[reference5[form[2]]][reference1[form[1]][form[0]]]
		else:
			conjugated = pps[3] + " " + passive_perfect[reference5[form[2]]][reference1[form[1]][form[0]]]
	else:
		conjugated += complete[reference4[form[3]]][reference3[conj]][reference2[form[2]]][reference1[form[1]][form[0]]]

	return conjugated


def determineAnswer(conj,pps,form):
	reference = {"singular":{"1st person":0,"2nd person":1,"3rd person":2},"plural":{"1st person":3,"2nd person":4,"3rd person":5}}

	endings = {}
	endings["present"] = {}
	endings["present"]["active"] = {"1":["o","as","at","amus","atis","ant"],"2":["eo","es","et","emus","etis","ent"],"3":["o","is","it","imus","itis","unt"],"3-io":["io","is","it","imus","itis","unt"],"4":["io","is","it","imus","itis","unt"]}
	endings["present"]["passive"] = {"1":["or","aris","atur","amur","amini","antur"],"2":["eor","eris","etur","emur","emini","entur"],"3":["or","eris","itur","imur","imini","untur"],"3-io":["ior","iris","itur","imur","imini","iuntur"],"4":["ior","iris","itur","imur","imini","iuntur"]}
	endings["imperfect"] = {}
	endings["imperfect"]["active"] = {"1":["abam","abas","abat","abamus","abatis","abant"],"2":["ebam","ebas","ebat","ebamus","ebatis","ebant"],"3":["ebam","ebas","ebat","ebamus","ebatis","ebant"],"3-io":["iebam","iebas","iebat","iebamus","iebatis","iebant"],"4":["iebam","iebas","iebat","iebamus","iebatis","iebant"]}
	endings["imperfect"]["passive"] = {"1":["abar","abaris","abatur","abamur","abamini","abantur"],"2":["ebar","ebaris","ebatur","ebamur","ebamini","ebantur"],"3":["ebar","ebaris","ebatur","ebamur","ebamini","ebantur"],"3-io":["iebar","iebaris","iebatur","iebamur","iebamini","iebantur"],"4":["iebar","iebaris","iebatur","iebamur","iebamini","iebantur"]}
	endings["future"] = {}
	endings["future"]["active"] = {"1":["abo","abis","abit","abimus","abitis","abunt"],"2":["ebo","ebis","ebit","ebimus","ebitis","ebunt"],"3":["am","es","et","emus","etis","ent"],"3-io":["iam","ies","iet","iemus","ietis","ient"],"4":["iam","ies","iet","iemus","ietis","ient"]}
	endings["future"]["passive"] = {"1":["abor","aberis","abitur","abimur","abimini","abuntur"],"2":["ebor","eberis","ebitur","ebimur","ebimini","ebuntur"],"3":["ar","eris","etur","emur","emini","entur"],"3-io":["iar","ieris","ietur","iemur","iemini","ientur"],"4":["iar","ieris","ietur","iemur","iemini","ientur"]}
	endings["perfect"] = {}
	endings["perfect"]["active"] = {"1":["i","isti","it","imus","istis","erunt"],"2":["i","isti","it","imus","istis","erunt"],"3":["i","isti","it","imus","istis","erunt"],"3-io":["i","isti","it","imus","istis","erunt"],"4":["i","isti","it","imus","istis","erunt"]}
	endings["perfect"]["passive"] = {"1":["sum","es","est","sumus","estis","sunt"],"2":["sum","es","est","sumus","estis","sunt"],"3":["sum","es","est","sumus","estis","sunt"],"3-io":["sum","es","est","sumus","estis","sunt"],"4":["sum","es","est","sumus","estis","sunt"]}
	endings["pluperfect"] = {}
	endings["pluperfect"]["active"] = {"1":["eram","eras","erat","eramus","eratis","erant"],"2":["eram","eras","erat","eramus","eratis","erant"],"3":["eram","eras","erat","eramus","eratis","erant"],"3-io":["eram","eras","erat","eramus","eratis","erant"],"4":["eram","eras","erat","eramus","eratis","erant"]}
	endings["pluperfect"]["passive"] = {"1":["eram","eras","erat","eramus","eratis","erant"],"2":["eram","eras","erat","eramus","eratis","erant"],"3":["eram","eras","erat","eramus","eratis","erant"],"3-io":["eram","eras","erat","eramus","eratis","erant"],"4":["eram","eras","erat","eramus","eratis","erant"]}
	endings["future perfect"] = {}
	endings["future perfect"]["active"] = {"1":["ero","eris","erit","erimus","eritis","erint"],"2":["ero","eris","erit","erimus","eritis","erint"],"3":["ero","eris","erit","erimus","eritis","erint"],"3-io":["ero","eris","erit","erimus","eritis","erint"],"4":["ero","eris","erit","erimus","eritis","erunt"]}
	endings["future perfect"]["passive"] = {"1":["ero","eris","erit","erimus","eritis","erunt"],"2":["ero","eris","erit","erimus","eritis","erunt"],"3":["ero","eris","erit","erimus","eritis","erunt"],"3-io":["ero","eris","erit","erimus","eritis","erunt"],"4":["ero","eris","erit","erimus","eritis","erint"]}

	if form[2] in ["present", "imperfect", "future"]:
		stem = pps[1][:-3]
	if form[2] in ["perfect", "pluperfect", "future perfect"]:
		if form[3] in ["active"]:
			stem = pps[2][:-1]
		if form[3] in ["passive"]:
			if form[1] in ["singular"]:
				stem = pps[3] + " "
			if form[1] in ["plural"]:
				stem = pps[3][:-2] + "a "
	
	return stem + endings[form[2]][form[3]][conj][reference[form[1]][form[0]]]
