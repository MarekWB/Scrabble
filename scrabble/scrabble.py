scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),(4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

letter_score = {letter: score for score, letters in scrabble_scores for letter in letters.split()}
def wynik_komenda(word=input):
	word = input("Wprowadź słowo do przeliczenia: ").upper()
	wynik = sum(letter_score[i] for i in word)
	print (f"Wynik dla słowa {word} to {wynik}")

def ze_słownika():
	result=[]
	with open('dictionary.txt','r') as słownik:
		for line in słownik:
			word = line.strip()
			wynik = sum(letter_score[i] for i in word)
			result.append(wynik)
		best=max(result)
		print(f"Najlepszy wynik z dictionary.txt to {best}.")
def podana_wartość(wart=input):
	wart = input("Wprowadź wartość punktową: ")
	wart = int(wart)
	with open('dictionary.txt','r') as słownik:
		for line in słownik:
			word = line.strip()
			wynik = sum(letter_score[i] for i in word)
			if wynik == wart:
				print (word)
			else:
				pass
try:
	tryb = input("Wybierz tryb: 1. Najwyższy wynik z dictionary.txt; 2. Wynik dla słowa z linii komend; 3. Słowo o podanej wartości. 1/2/3?")
	tryb = int(tryb)
except ValueError:
	print ("Proszę wybrać tryb 1., 2. albo 3. poprzez podanie cyfry: 1, 2 albo 3.")	
else:
	if tryb == 1:
		ze_słownika()
	elif tryb ==2:
		wynik_komenda()
	elif tryb ==3:
		podana_wartość()
	else:
		print("Proszę wybrać tryb 1., 2. albo 3. poprzez podanie cyfry: 1, 2 albo 3.")

	

#def word_score(word):
#	points = 0
#	for letter in word.lower():
#		points += letter_score[letter]
#
#	return points
#
#rint (word_score("pupa"))