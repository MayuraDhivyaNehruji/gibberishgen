suffix = "osyob"
print 'Gibberish generator'
# Start coding here!
playerName= raw_input("Enter your name and press Enter:")
print "Hello %s \n let's get started" %(playerName)
initialWord = raw_input("Feed me a word:")

if (len(initialWord)>0 and initialWord.isalpha()):
  print "Hmm! %s is it ! uniformity is important!" %(initialWord)
  smallWord = initialWord.lower()
  alpha1 = initialWord[0].lower();
  reword = smallWord + alpha1 + suffix;
  print reword[1:len(reword)]
else:
    print "You trying to fool me ? Nothing is free! I said feed me! and make sure its just alphabets! Numbers and Symbols poison me"
