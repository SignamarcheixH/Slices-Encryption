"""Programme qui code/décode un message suivant la méthode suivante:
	On construit le message avec les premiers caractères de chaque mot, puis des deuxièmes, et ainsi de suite
	Lorsqu'un mot est fini, après avoir écrit sa dernière lettre dans le message codé, on insère une lettre de la clé (nécessaire pour décoder)
	La clé doit être composée de caractères INEXISTANTS dans le message
	Il faut également donner le nombre de mots du message initial lors du décodage
Exemple : bonjour le monde -> blmoefonnjdoekurj avec la cle (fkj) """

import random

def tolist(s):
#fonction qui transforme un str s en sa liste de char correspondant : monde -> [m,o,n,d,e]
	L=[]
	for c in s:
		L.append(c)
	return(L)

def splitintegral(s):
#fonction qui renvoie le message s decoupé en liste de char : hello world -> [ [h,e,l,l,o],[w,o,r,l,d] ]
	L=s.split()  #on separe les mots : "hello world" -> ["hello","world"]
	j=0
	for i in L: #pour chaque mot
		i=tolist(i) 	#on en fait une liste de char
		L[j]=i		#que l'on replace dans la liste  : ["hello","world"] -> [ [h,e,l,l,o], "world"] à l'itération 0
		j=j+1
	return(L)



def strtocode(s,KEY):
#fonction qui code un message s avec la clé KEY
	L=splitintegral(s)  #on fabrique la liste de liste du message
	LCODE=[]  	    #le message codé
	indexl=0
	indexkey=0
	while len(L) != 0:   #tant qu'il reste des caractères dans le message a coder
		subl=L[indexl]   #subl= mot en cours
		LCODE.append(subl[0])   #on ajoute le premier caractère du mot en cours
		if len(subl)==1: #si on termine le mot en cours avec cet ajout
			indexl=indexl-1  #on recule d'un rang l'index du sous mot (ca gere le cas ou le sous-mot est pas en dernier )
			LCODE.append(KEY[indexkey])  #on place une lettre de la clé
			if indexkey==len(KEY)-1:     #on decale l'index de la clé modulo sa taille
				indexkey=0
			else:
				indexkey=indexkey+1
			if indexl==len(L)-2:         #si en reculant on arrive en -2, alors on était dans le dernier sous-mot, on doit donc réavancer l'indice car il sera mis à zero dans le if suivant
				indexl=indexl+1
		subl.remove(subl[0])		#on enleve du sous-mot le caractère ajouté
		if indexl==len(L)-1:		#on fait avancer l'indice du sous mot modulo len(L)
			indexl=0
		else:
			indexl=indexl+1
		L=[x for x in L if len(x)!=0] #on supprime de la liste les sous-mots vides si il y en ( crée un décalage des indices si le sous-mot vide est au milieu d'autres
	LCODE=''.join(LCODE)   #on join toute la liste de char codé
	return LCODE

def codetostr(s,key,n):
#fonction qui decode un message s de n mots avec la clé key
	MESSAGE=[]
	L=[]
	FLAGLIST=[]
	index=0
	for i in range(1,n+1):  #ajoute n listes vides a MESSAGE et L , et n True a FLAGLIST
		MESSAGE.append([])
		L.append([])
		FLAGLIST.append(True)  #FLAGLIST : True si ce sous-mot n'est pas complet
	for c in s:		#pour chaque caractère c du message codé
		if c not in key:	#si c n'appartient pas à la clé
			while FLAGLIST[index] != True:	#on parcourt les sous mots modulo n tant qu'ils sont complets
				if index==len(L)-1:
					index=0
				else:
					index=index+1
			L[index].append(c)  #on ajoute c au premier sous mot non plein
			if index==len(L)-1: #on passe au sous-mot suivant modulo n
				index=0
			else:
				index=index+1
		else: 			#si c appartient à la clé, le sous-mot précedent est complet
			if index==0:    # si on est en position 0, c'etait le dernier sous-mot de la liste
				index=len(L)-1
			else:
				index=index-1  #sinon c'était le sous-mot d'avant dans la liste
			MESSAGE[index]=L[index]	#on ajoute au message le sous-mot complet à la bonne place
			FLAGLIST[index]=False	#on declare ce sous-mot comme complet
	MESSAGE[index]=L[index]	#on ajoute le dernier mot (ie le plus long)
	for i in range(len(MESSAGE)):
		MESSAGE[i]=''.join(MESSAGE[i])	#on join les sous-mots
	return(' '.join(MESSAGE))		#on join le message


def keygen(s):
#fonction qui à partir d'un message s, renvoie une clé qui marche ( ie aucune lettre de la clé n'est présente dans le message)
	alphabet=['A','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
	KEY=[]
	for c in s:
		if c in alphabet:  #on elimine les lettres qui se trouvent dans le message
			alphabet.remove(c)
	taille=random.randint(4,10) #on genere une taille de clé entre 4 et 10
	for i in range(taille):
		idx=random.randint(0,len(alphabet)-1)  #on choisit une lettre aléatoire parmis les candidats restants de l'alphabet et on l'ajoute
		KEY.append(alphabet[idx])
	return(KEY)
