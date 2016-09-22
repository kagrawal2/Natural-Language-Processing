
class Test:
    """Example Test Usage
    t = Test(ncd)
    t.direct()
    t.paraphrase()
    t.paste()
    """

    def __init__(self, func):
        self.function = func
        # paraphrase()
        # direct()
        # paste()
        self.oxford()
        self.paraphrase()
        self.direct()
        self.paste()
        print()
        

    def paraphrase(self):
        #Test for paraphrasing
        print("Testing for paraphrasing...")
        e = "How important is our power of non-analytical thought to the practice of science? It's the most important thing we have, declares the Princeton physicist historian Thomas Kuhn who argues that major breakthroughs occur only after scientists finally concede that certain physical phenomena cannot be explained by extending the logic of old theories. Consider the belief that the sun and the planets move around the earth, which reigned prior to 1500. This idea served nicely for a number of centuries, but then became too cumbersome to describe the motions of heavenly bodies. So the Polish astronomer Copernicus invented a new reality that was based on a totally different ‘paradigm’ or model - that the earth and planets move around the sun."
        d = "Non-analytic thought is considered very important to the practice of science by Princeton physicist historian Thomas Kuhn who claims that major breakthroughs happen only when scientists finally concede that some physical phenomena defy explanation by extending the logic of old theories. One idea which served nicely for many centuries but then became too cumbersome was the belief that the sun and planets revolved around the earth. This was held prior to 1500 until Copernicus invented a new reality: the earth and planets move around the sun."
        print("Test 1: " + str(100 * self.function(e, d)))

        x = "From time to time this submerged or latent theater in Hamlet becomes almost overt. It is close to the surface in Hamlet’s pretense of madness, the “antic disposition” he puts on to protect himself and prevent his antagonists from plucking out the heart of his mystery. It is even closer to the surface when Hamlet enters his mother’s room and holds up, side by side, the pictures of the two kings, Old Hamlet and Claudius, and proceeds to describe for her the true nature of the choice she has made, presenting truth by means of a show. Similarly, when he leaps into the open grave at Ophelia’s funeral, ranting in high heroic terms, he is acting out for Laertes, and perhaps for himself as well, the folly of excessive, melodramatic expressions of grief."
        y = "Almost all of Shakespeare’s Hamlet can be understood as a play about acting and the theater. For example, in Act 1, Hamlet pretends to be insane in order to make sure his enemies do not discover his mission to revenge his father’s murder. The theme is even more obvious when Hamlet compares the pictures of his mother’s two husbands to show her what a bad choice she has made, using their images to reveal the truth. Also, when he jumps into Ophelia’s grave, hurling his challenge to Laertes, Hamlet demonstrates the foolishness of exaggerated expressions of emotion."
        print("Test 2: " + str(100 * self.function(x, y)))

    def direct(self):
        #Test for direct copy
        print("Testing for direct part copy...")
        f = "Those complexes that contain unpaired electrons are attracted into a magnetic field and are said to be paramagnetic, while those with no unpaired electrons are repelled by such a field and are called diamagnetic."
        g = "Complexes that contain unpaired electrons are those that are attracted to a magnetic field. These are called paramagnetic, while those with no unpaired electrons are repelled by a magnetic field and are said to be diamagnetic."
        print("Test 1: " + str(100 * self.function(f, g)))

        x = "From time to time this submerged or latent theater in Hamlet becomes almost overt. It is close to the surface in Hamlet’s pretense of madness, the “antic disposition” he puts on to protect himself and prevent his antagonists from plucking out the heart of his mystery. It is even closer to the surface when Hamlet enters his mother’s room and holds up, side by side, the pictures of the two kings, Old Hamlet and Claudius, and proceeds to describe for her the true nature of the choice she has made, presenting truth by means of a show. Similarly, when he leaps into the open grave at Ophelia’s funeral, ranting in high heroic terms, he is acting out for Laertes, and perhaps for himself as well, the folly of excessive, melodramatic expressions of grief."
        y = "Almost all of Shakespeare’s Hamlet can be understood as a play about acting and the theater. For example, in Act 1, Hamlet adopts a pretense of madness that he uses to protect himself and prevent his antagonists from discovering his mission to revenge his father’s murder. He also presents truth by means of a show when he compares the portraits of Gertrude’s two husbands in order to describe for her the true nature of the choice she has made. And when he leaps in Ophelia’s open grave ranting in high heroic terms, Hamlet is acting out the folly of excessive, melodramatic expressions of grief."
        print("Test 2: " + str(100 * self.function(x, y)))


    def paste(self):
        #Test for a copy and paste substring
        print("Testing for copy and paste...")
        a = "Hello how are you today"
        b = "how are you"
        print("Test 1: " + str(100 * self.function(a, b)))

        d = "From time to time this submerged or latent theater in becomes almost overt. It is close to the surface in Hamlet’s pretense of madness, the “antic disposition” he puts on to protect himself and prevent his antagonists from plucking out the heart of his mystery. It is even closer to the surface when Hamlet enters his mother’s room and holds up, side by side, the pictures of the two kings, Old Hamlet and Claudius, and proceeds to describe for her the true nature of the choice she has made, presenting truth by means of a show. Similarly, when he leaps into the open grave at Ophelia’s funeral, ranting in high heroic terms, he is acting out for Laertes, and perhaps for himself as well, the folly of excessive, melodramatic expressions of grief."
        e = "Almost all of Shakespeare’s Hamlet can be understood as a play about acting and the theater. For example, there is Hamlet’s pretense of madness, the “antic disposition” that he puts on to protect himself and prevent his antagonists from plucking out the heart of his mystery. When Hamlet enters his mother’s room, he holds up, side by side, the pictures of the two kings, Old Hamlet and Claudius, and proceeds to describe for her the true nature of the choice she has made, presenting truth by means of a show. Similarly, when he leaps into the open grave at Ophelia’s funeral, ranting in high heroic terms, he is acting out for Laertes, and perhaps for himself as well, the folly of excessive, melodramatic expressions of grief."
        print("Test 2: " + str(100 * self.function(d, e)))


    def oxford(self):
        print("The following should return a higher value for copying (Plagiarized) in increasing value levels")
        source = "From a class perspective this put them [highwaymen] in an ambivalent position. In aspiring to that proud, if temporary, status of ‘Gentleman of the Road’, they did not question the inegalitarian hierarchy of their society. Yet their boldness of act and deed, in putting them outside the law as rebellious fugitives, revivified the ‘animal spirits’ of capitalism and became an essential part of the oppositional culture of working-class London, a serious obstacle to the formation of a tractable, obedient labour force. Therefore, it was not enough to hang them – the values they espoused or represented had to be challenged."
        
        a = "Although they did not question the inegalitarian hierarchy of their society, highwaymen became an essential part of the oppositional culture of working-class London, posing a serious threat to the formation of a biddable labour force."
        print("Test A: " + str(100 * self.function(a, source)))
        b = "Although they did not question the inegalitarian hierarchy of their society, highwaymen exercised a powerful attraction for the working classes. Some historians believe that this hindered the development of a submissive workforce."
        print("Test B: " + str(100 * self.function(b, source)))
        c = "Although they did not question the inegalitarian hierarchy of their society, highwaymen ‘became an essential part of the oppositional culture of working-class London [and] a serious obstacle to the formation of a tractable, obedient labour force’."
        print("Test C: " + str(100 * self.function(c, source)))
        d = "Highwaymen’s bold deeds ‘revivified the “animal spirits” of capitalism’ and made them an essential part of the oppositional culture of working-class London.1 Peter Linebaugh argues that they posed a major obstacle to the formation of an obedient labour force."
        print("Test D: " + str(100 * self.function(d, source)))
        e = "By aspiring to the title of ‘Gentleman of the Road’, highwaymen did not challenge the unfair taxonomy of their society. Yet their daring exploits made them into outlaws and inspired the antagonistic culture of labouring London, forming a grave impediment to the development of a submissive workforce. Ultimately, hanging them was insufficient – the ideals they personified had to be discredited."
        print("Test E: " + str(100 * self.function(e, source)))
        
        print("The following should return a lower value for copying (Not Plagiarized")
        x = "Peter Linebaugh argues that although highwaymen posed no overt challenge to social orthodoxy – they aspired to be known as ‘Gentlemen of the Road’ – they were often seen as anti-hero role models by the unruly working classes. He concludes that they were executed not only for their criminal acts, but in order to stamp out the threat of insubordinacy."
        print("Test X: " + str(100 * self.function(x, source)))
        y = "Peter Linebaugh argues that highwaymen represented a powerful challenge to the mores of capitalist society and inspired the rebelliousness of London’s working class."
        print("Test Y: " + str(100 * self.function(y, source)))





