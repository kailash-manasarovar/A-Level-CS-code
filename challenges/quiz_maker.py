# generates 30 quizzes with randomly ordered questions and answers
import random
# keywords and definitions are stored in key:value pairs in qadict
qadict = {'genes':'the basic units of biological information',
          'heredity':'the way genes transmit physiological and behavioural traits from parents to offspring',
          'genetics':'the science of heredity',
          'artificial selection':'purposeful control over mating by choice of parents for the next generation',
          'self-fertilization':'when egg and pollen come from the same plant',
          'cross-fertilization':'brushing pollen from one plant onto the female organ of another plant',
          'discrete traits':'"either-or" traits with no intermediary forms',
          'continuous traits':'traits which show intermediary forms',
          'pure-breeding lines':'families producing offspring carrying specific parental traits that remain constant across generations',
          'hybrids':'offspring of genetically dissimilar parents',
          'monohybrid cross':'cross between parents differing only in one trait',
          'monoybrids':'individuals having two different alleles for a single trait',
          'dominant trait':'the trait that appears in the offspring of pure-breeding parental strains with antagonistic phenotypes',
          'recessive trait':'the trait that remains hidden in the offspring of pure-breeding parental strains with antagonistic phenotypes',
          'gametes':'specialized cells which carry genes between generations',
          'law of segregation':'two alleles for a trait separate during gamete formation then reunite randomly at fertilization',
          'Punnett square':'a matrix used to predict all possible genotypes of the offspring of a genetic cross',
          'product rule':'the probability of two or more independent events occuring together is the product of their probabilities',
          'sum rule':'the probability of either of two mutually exclusive events occuring is the sum of their probabilities',
          'phenotype':'an observable characteristic',
          'genotype':'the actual alleles present in an individual'}
for i in range(1,31):
    fo = open("BIO_quiz"+str(i)+".txt","w")  # open a new file for a quiz
    fo2 = open("BIO_quiz_answers"+str(i)+".txt","w")  # open a new file for the answers
    rq = list(qadict.keys())  # get a list of all the keywords
    random.shuffle(rq)  # shuffle the words randomly
    fo.write("BIO QUIZ #"+str(i)+"\n\n\n")
    fo2.write("BIO QUIZ #"+str(i)+" ANSWERS\n\n")
    for j in range(len(rq)):
        fo.write(str(j+1)+". Define: "+rq[j].capitalize()+"\n")  # question number, keyword
        correctAnswer = qadict[rq[j]]  # find the keyword's definition in qadict
        answers = [correctAnswer]  # create a list containing the correct answer
        answerpool = list(qadict.values())  # get a list of all the definitions
        answerpool.remove(correctAnswer)  # remove the correct answer from the list
        answers += random.sample(answerpool,3) # randomly choose 3 incorrect answer and add them to the list
        random.shuffle(answers)  # shuffle the answers randomly so the correct one isn't always first
        fo2.write(str(j+1)+". "+"abcd"[answers.index(correctAnswer)]+"\n") # write the correct answer in the answers file
        for m in range(4):
            fo.write("    "+"abcd"[m]+") "+answers[m]+"\n")  # write all 4 possible answers in the quiz with a letter for each option
        fo.write("\n")
fo.close()
