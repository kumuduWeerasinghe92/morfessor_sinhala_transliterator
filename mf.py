import morfessor






def evaluate_model(sin_eng_main,sin_eng_sub,word_list,model):
	fx = open("analyze.txt","a", encoding="utf-8")
	
	for word in word_list:
		t = model.viterbi_segment(word[1])
		
		rword = convert_word(sin_eng_main,sin_eng_sub,word[0],2)
		
		if(len(t) >1):
			cnt=0
			for fi in t:
				cnt+=1
				
				if(cnt ==1):
			
					if(len(fi)>1):
						for i in range(len(fi)):
							if(i == 0):
								fx.write(rword[0:len(fi[i])]+"+")
							elif(i>0 and i !=len(fi)-1 ):
								fx.write(rword[len(fi[i-1]):len(fi[i])+len(fi[i-1])]+"+")
							else:
								fx.write(rword[-len(fi[i]):]+"=>")
						
					else:
						fx.write(rword[:len(fi[0])]+"=>")
				if(cnt ==2):
					fx.write(str(fi)+"\n\n")

	fx.close()
	

def convert_word(sin_eng_main,sin_eng_sub,word,mode):
	if(len(word)>0):
		converted_word=""
		for ch in word:
			if(mode==1):
				if(ch in sin_eng_main):
					converted_word = converted_word+sin_eng_main[ch]
				elif(ch in sin_eng_sub):
					converted_word = converted_word+sin_eng_sub[ch].replace("α","")
					
				else:
					s =u''+ch+''
					
						
					if(s=='\u200d'):
						converted_word = converted_word+"¤"
					elif(s=='\n' or s=='\u200c'):
						converted_word = converted_word
					else:
						converted_word=""
						break
			elif(mode==2):
				if(ch in sin_eng_main):
					converted_word = converted_word+ch
				elif(ch in sin_eng_sub):
					converted_word = converted_word+ch
					
				else:
					s =u''+ch+''
					
						
					if(s=='\u200d'):
						converted_word = converted_word+ch
					elif(s=='\n' or s=='\u200c'):
						converted_word = converted_word
					else:
						converted_word=""
						break
				
		return converted_word 		
		
	else:
		return ""
		
		
def convert_word_alpha(sin_eng_main,sin_eng_sub,word):
	if(len(word)>0):
		converted_word_alpha =""
		for ch in word:
			if(ch in sin_eng_main):
				converted_word_alpha = converted_word_alpha+sin_eng_main[ch]
			elif(ch in sin_eng_sub):
				converted_word_alpha = converted_word_alpha+sin_eng_sub[ch]
			else:
				s =u''+ch+''
				
				if(s=='\u200d'):
					converted_word_alpha = converted_word_alpha+"¤"
				elif(s=='\n' or s=='\u200c'):
					converted_word_alpha = converted_word_alpha
				else:
					converted_word_alpha=""
					break
		return converted_word_alpha 		
		
	else:
		return ""

def develop_training_set(sin_eng_main,sin_eng_sub,wordlist_file):
	fword = open("converted_word.txt","a", encoding="utf-8")
	fword_a = open("converted_word_alpha.txt","a", encoding="utf-8")
	
	
	incorrect_char ={}
	with open(wordlist_file,"r", encoding="utf-8-sig") as fa:  
		line = "start"
		cnt = 1
		
		
		
		while line:
			arraix=[]
			if(cnt !=1):
				line = fa.readline()
				single_word_arr = line.split(" ")
				if(single_word_arr):
					if(len(single_word_arr) ==2):
						word = single_word_arr[1]
						frequency = single_word_arr[0]
						converted_word = ""
						converted_word_alpha =""
						
						for ch in word:
							if(ch in sin_eng_main):
								converted_word = converted_word+sin_eng_main[ch]
								converted_word_alpha = converted_word_alpha+sin_eng_main[ch]
							elif(ch in sin_eng_sub):
								converted_word = converted_word+sin_eng_sub[ch].replace("α","")
								converted_word_alpha = converted_word_alpha+sin_eng_sub[ch]
							else:
								s =u''+ch+''
								if(s not in incorrect_char):
									incorrect_char[s]=1
								else:
									incorrect_char[s]=incorrect_char[s]+1
									
								if(s=='\u200d'):
									converted_word = converted_word+"¤"
									converted_word_alpha = converted_word_alpha+"¤"
								elif(s=='\n' or s=='\u200c'):
									converted_word = converted_word
									converted_word_alpha = converted_word_alpha
								else:
									converted_word=""
									converted_word_alpha=""
									break
						if(converted_word !="" and converted_word_alpha !=""):
							fword.write(frequency+" "+converted_word+"\n");
							fword_a.write(frequency+" "+converted_word_alpha+"\n");
						
						
			cnt += 1

	fword.close()
	fword_a.close()

def construct_test_array(test_file):
	word_array =[]
	with open(test_file,"r", encoding="utf-8-sig") as fa:  
		line = "start"
		cnt = 1
		while line:
			arraix=[]
			if(cnt !=1):
				line = fa.readline().strip()
				if(len(line)>1):
					word_array.append(line)		
			cnt += 1
	return word_array

# Driver code 
if __name__ == '__main__':
	io = morfessor.MorfessorIO()
	model = io.read_binary_model_file('model1.bin')
	
	wordlist_file="unique_word.txt"
	sin_eng_main ={
	"අ":"a",
	"ආ":"A",
	"ඇ":"æ",
	"ඈ":"Æ",
	"ඉ":"i",
	"ඊ":"I",
	"උ":"u",
	"ඌ":"U",
	"ඍ":"R",
	"ඎ":"H",
	"ඏ":"î",
	"ඐ":"Î",
	"එ":"e",
	"ඒ":"E",
	"ඓ":"X",
	"ඔ":"o",
	"ඕ":"O",
	"ඖ":"Y",
	"ක":"k",
	"ඛ":"K",
	"ග":"g",
	"ඝ":"G",
	"ඞ":"F",
	"ඟ":"ß",
	"ච":"c",
	"ඡ":"C",
	"ජ":"j",
	"ඣ":"J",
	"ඤ":"ñ",
	"ඥ":"Ñ",
	"ඦ":"ç",
	"ට":"t",
	"ඨ":"T",
	"ඩ":"d",
	"ඪ":"D",
	"ණ":"N",
	"ඬ":"W",
	"ත":"q",
	"ථ":"Q",
	"ද":"v",
	"ධ":"V",
	"න":"n",
	"ඳ":"µ",
	"ප":"p",
	"ඵ":"P",
	"බ":"b",
	"භ":"B",
	"ම":"m",
	"ඹ":"M",
	"ය":"y",
	"ර":"r",
	"ල":"l",
	"ව":"w",
	"ශ":"S",
	"ෂ":"x",
	"ස":"s",
	"හ":"h",
	"ළ":"L",
	"ෆ":"f"
	}
	
	eng_sin_main = dict([(value, key) for key, value in sin_eng_main.items()]) 
	
	sin_eng_sub ={
	"ං":"αz",
	"ඃ":"αZ",
	"්":"αø",
	"ා":"αA",
	"ැ":"αæ",
	"ෑ":"αÆ",
	"ි":"αi",
	"ී":"αI",
	"ු":"αu",
	"ූ":"αU",
	"ෘ":"αR",
	"ෲ":"αH",
	"ෟ":"αî",
	"ෳ":"αÎ",
	"ෙ":"αe",
	"ේ":"αE",
	"ෛ":"αX",
	"ො":"αo",
	"ෝ":"αO",
	"ෞ":"αY"
	}
	
	eng_sin_sub = dict([(value, key) for key, value in sin_eng_sub.items()]) 
	
	
	test_words = construct_test_array("testdata.txt")
	test_converted_words =[]
	
	for i in range(len(test_words)):
		wordr= convert_word(sin_eng_main,sin_eng_sub,test_words[i],1)
		test_converted_words.append([test_words[i],wordr])
	
	
	evaluate_model(sin_eng_main,sin_eng_sub,test_converted_words,model)
	
	
	

