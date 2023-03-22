#########################################################################################            

def tunesByDevinMain(mainMenu):

    print("Welcome to Tunes By Devin")
    for i in range(0, len(mainMenu)):
        print(f'{i+1}. {mainMenu[i]}')
        

#########################################################################################            

def menuSelection(mainMenu):

    tunesByDevinMain(mainMenu)
    selection = input("Please choose an option: ")

    while selection not in mainMenu:
        print("Invalid Choice. Please Try Again.")
        print("\n" * 20)

        tunesByDevinMain(mainMenu)
        selection = input("Please choose an option: ")

    return selection

#########################################################################################       

def end():
    import sys
    print("Thankyou for using Tunes By Devin. Hope you enjoyed. Please return soon!")
    sys.exit()
    
#########################################################################################       

def home(homeMenu):

    print("\n" * 5)
    for x in range(0, len(homeMenu)):
        print(f'{x+1}. {homeMenu[x]}')

#########################################################################################

def homeSelection(homeMenu):

    home(homeMenu)
    homeChoice = input("What is your next option? ")

    while homeChoice not in homeMenu:
        print("Invalide Choice. Please Try Again.")
        print("\n" * 20)

        home(homeMenu)
        homeChoice = input("What is your next option? ")

    return homeChoice

#########################################################################################

def browse(songGenres):
    print("\n" * 5)
    for y in range(0, len(songGenres)):
        print(f'{y+1}. {songGenres[y]}')

    genre = input("Please choose a genre. If you would like to go back to the main menu, please type 'Back': ")

    return genre

#########################################################################################

def printListSongs(genre, listClassical, listRap, listSoul, listPop):   
    print("\n" * 5)
    if genre == 'Classical':
        for classical in range(0, len(listClassical)):
            print(f'{classical+1}. {listClassical[classical]}')
        return listClassical
    elif genre == 'Rap':
        for rap in range(0, len(listRap)):
            print(f'{rap+1}. {listRap[rap]}')
        return listRap
    elif genre == 'Soul':
        for soul in range(0, len(listSoul)):
            print(f'{soul+1}. {listSoul[soul]}')
        return listSoul
    elif genre == 'Pop':
        for pop in range(0, len(listPop)):
            print(f'{pop+1}. {listPop[pop]}')
        return listPop
##    elif genre == 'Back':
##        main()

#########################################################################################

def listSongsSelection(currentList, playlist, recentlyPlayed, musicNotes):
    import time
    sSelection = int(input("Please choose the number of a song you would like to listen to: "))

    if sSelection in range(0, len(currentList)):
        print(f'{currentList[sSelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        sSelection2 = input("If you would like to save this song, please type 'Save'. If you do not want to save this song, please hit the 'Enter' or 'Return' key: ")
        if sSelection2 == "Save":
            playlist.append(currentList[sSelection -1])
            recentlyPlayed.append(currentList[sSelection -1])
        else:
            recentlyPlayed.append(currentList[sSelection -1])
    else:
        print("Invalid Choice.")
        
#########################################################################################

def popularAlbums(listTopAlbums):
    print("\n" * 5)
    for pAS in range(0, len(listTopAlbums)):
        print(f'{pAS+1}. {listTopAlbums[pAS]}')

    popularAlbumChoice = int(input("Please choose the number of a song you would like to listen to. If you would like to go back to the main menu, please type '777': "))

    return popularAlbumChoice

#########################################################################################        
    
def printAlbumSongs(popularAlbumChoice, listFreeSpiritSongs, listEilishAlbumSongs, listThankUNextSongs, listDeathRaceForLoveSongs, listVictoryLapSongs):
    print("\n" * 5)
    if popularAlbumChoice == 1:
        for fS in range(0, len(listFreeSpiritSongs)):
            print(f'{fS+1}. {listFreeSpiritSongs[fS]}')
        return listFreeSpiritSongs
    elif popularAlbumChoice == 2:
        for eilishAlbum in range(0, len(listEilishAlbumSongs)):
            print(f'{eilishAlbum+1}. {listEilishAlbumSongs[eilishAlbum]}')
        return listEilishAlbumSongs
    elif popularAlbumChoice == 4:
        for tUN in range(0, len(listThankUNextSongs)):
            print(f'{tUN+1}. {listThankUNextSongs[tUN]}')
        return listThankUNextSongs
    elif popularAlbumChoice == 5:
        for dRFL in range(0, len(listDeathRaceForLoveSongs)):
            print(f'{dRFL+1}. {listDeathRaceForLoveSongs[dRFL]}')
        return listDeathRaceForLoveSongs
    elif popularAlbumChoice == 3:
        for vL in range(0, len(listVictoryLapSongs)):
            print(f'{vL+1}. {listVictoryLapSongs[vL]}')
        return listVictoryLapSongs
##    elif popularAlbumChoice == 777:
##        main()

#########################################################################################
    
def popularAlbumSelection(currentPopularAlbumList, playlist, recentlyPlayed, musicNotes):
    import time
    pASelection = int(input("Please choose the number of a song you would like to listen to: "))

    if pASelection in range(0, len(currentPopularAlbumList)):
        print(f'{currentPopularAlbumList[pASelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)
        
        pASelection2 = input("If you would like to save this song, please type 'Save'. If you do not want to save this song, please hit the 'Enter' or 'Return' key: ")
        if pASelection2 == "Save":
            playlist.append(currentPopularAlbumList[pASelection -1])
            recentlyPlayed.append(currentPopularAlbumList[pASelection -1])
        else:
            recentlyPlayed.append(currentPopularAlbumList[pASelection -1])
    else:
        print("Invalid Choice.")
        
#########################################################################################

def podcasts(podcastGenres):
    print("\n" * 5)
    for pG in range(0, len(podcastGenres)):
        print(f'{pG+1}. {podcastGenres[pG]}')

    podGenre = input("Please choose a genre. If you would like to go back to the main menu, please type 'Back': ")

    return podGenre

#########################################################################################

def printListPodcasts(podGenre, listMusicPod, listEducationalPod, listFictionalPod, listSportsPod):
    print("\n" * 5)
    if podGenre == 'Music':
        for music in range(0, len(listMusicPod)):
            print(f'{music+1}. {listMusicPod[music]}')
        return listMusicPod
    elif podGenre == 'Educational':
        for educational in range(0, len(listEducationalPod)):
            print(f'{educational+1}. {listEducationalPod[educational]}')
        return listEducationalPod
    elif podGenre == 'Fictional':
        for fictional in range(0, len(listFictionalPod)):
            print(f'{fictional+1}. {listFictionalPod[fictional]}')
        return listFictionalPod
    elif podGenre == 'Sports':
        for sports in range(0, len(listSportsPod)):
            print(f'{sports+1}. {listSportsPod[sports]}')
        return listSportsPod
##    elif podGenre == 'Back':
##        main()

###########################################################################################
        
def listPodcastsSelection(currentPodList, savedPodcasts, talking):
    import time
    podSelection = int(input("Please choose the number of a podcast you would like to listen to: "))

    if podSelection in range(0, len(currentPodList)):
        print(f'{currentPodList[podSelection -1]} is playing: ')
        time.sleep(0.25)
        for talk in talking * 6:
            print(talk * 10)
            time.sleep(0.15)

        podSelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if podSelection2 == "Save":
            savedPodcasts.append(currentPodList[podSelection -1])
    else:
        print("Invalid Choice.")
        
#########################################################################################
                             
def recommended(recommendedGenres):
    print("\n" * 5)
    for r in range(0, len(recommendedGenres)):
        print(f'{r+1}. {recommendedGenres[r]}')

    rGenre = input("Please choose a genre. If you would like to go back to the main menu, please type 'Back': ")

    return rGenre

#########################################################################################

def printListRecommendedSongs(rGenre, listRClassical, listRRap, listRSoul, listRPop):
    print("\n" * 5)
    if rGenre == 'Classical':
        for rClassical in range(0, len(listRClassical)):
            print(f'{rClassical+1}. {listRClassical[rClassical]}')
        return listRClassical
    elif rGenre == 'Rap':
        for rRap in range(0, len(listRRap)):
            print(f'{rRap+1}. {listRRap[rRap]}')
        return listRRap
    elif rGenre == 'Soul':
        for rSoul in range(0, len(listRSoul)):
            print(f'{rSoul+1}. {listRSoul[rSoul]}')
        return listRSoul
    elif rGenre == 'Pop':
        for rPop in range(0, len(listRPop)):
            print(f'{rPop+1}. {listRPop[rPop]}')
        return listRPop
##    elif rGenre == 'Back':
##        main()       
    
#########################################################################################

def listRecommendedSongsSelection(currentRecommendedList, playlist, recentlyPlayed, musicNotes):
    import time
    rSelection = int(input("Please choose the number of a song you would like to listen to: "))

    if rSelection in range(0, len(currentRecommendedList)):
        print(f'{currentRecommendedList[rSelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        rSelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if rSelection2 == "Save":
            playlist.append(currentRecommendedList[rSelection -1])
            recentlyPlayed.append(currentRecommendedList[rSelection -1])
        else:
            recentlyPlayed.append(currentRecommendedList[rSelection -1])
    else:
        print("Invalid Choice.")

#########################################################################################
        
def library(libraryMenu):
    print("\n" * 5)
    for l in range(0, len(libraryMenu)):
        print(f'{l+1}. {libraryMenu[l]}')
    libraryChoice = input("Please choose an option ")

    while libraryChoice not in libraryMenu:
        print("Invalide Choice. Please Try Again.")
        print("\n" * 20)

        library(libraryMenu)
        libraryChoice = input("Please choose an option ")

    return libraryChoice

#########################################################################################

def artists(artistGenres):
    print("\n" * 5)
    for a in range(0, len(artistGenres)):
        print(f'{a+1}. {artistGenres[a]}')

    aGenre = input("Please choose a genre. If you would like to go back to the main menu, please type 'Back': ")

    return aGenre

#########################################################################################

def printListArtists(aGenre, listClassicalArtists, listRapArtists, listSoulArtists, listPopArtists):
    print("\n" * 5)
    if aGenre == 'Classical':
        for aClassical in range(0, len(listClassicalArtists)):
            print(f'{aClassical+1}. {listClassicalArtists[aClassical]}')
        return listClassicalArtists
    elif aGenre == 'Rap':
        for aRap in range(0, len(listRapArtists)):
            print(f'{aRap+1}. {listRapArtists[aRap]}')
        return listRapArtists
    elif aGenre == 'Soul':
        for aSoul in range(0, len(listSoulArtists)):
            print(f'{aSoul+1}. {listSoulArtists[aSoul]}')
        return listSoulArtists
    elif aGenre == 'Pop':
        for aPop in range(0, len(listPopArtists)):
            print(f'{aPop+1}. {listPopArtists[aPop]}')
        return listPopArtists
##    elif aGenre == 'Back':
##        main()

#########################################################################################

def printClassicalArtistsSongs(cS, listBach, listBeethoven, listMozart, listTchaikovsky, listChopin, listBrahms, listSchubert, listVivaldi, listDebussy, listHandel):
    print("\n" * 5)
    cS = int(input("Please choose a number to select an artist: "))
    if cS == 1:
        print("Most Popular Songs-")
        for ba in range(0, len(listBach)):
            print(f'{ba+1}. {listBach[ba]}')
        return listBach
    elif cS == 2:
        print("Most Popular Songs-")
        for be in range(0, len(listBeethoven)):
            print(f'{be+1}. {listBeethoven[be]}')
        return listBeethoven
    elif cS == 3:
        print("Most Popular Songs-")
        for m in range(0, len(listMozart)):
            print(f'{m+1}. {listMozart[m]}')
        return listMozart
    elif cS == 4:
        print("Most Popular Songs-")
        for t in range(0, len(listTchaikovsky)):
            print(f'{t+1}. {listTchaikovsky[t]}')
        return listTchaikovsky
    elif cS == 5:
        print("Most Popular Songs-")
        for c in range(0, len(listChopin)):
            print(f'{c+1}. {listChopin[c]}')
        return listChopin
    elif cS == 6:
        print("Most Popular Songs-")
        for br in range(0, len(listBrahms)):
            print(f'{br+1}. {listBrahms[br]}')
        return listBrahms
    elif cS == 7:
        print("Most Popular Songs-")
        for s in range(0, len(listSchubert)):
            print(f'{s+1}. {listSchubert[s]}')
        return listSchubert
    elif cS == 8:
        print("Most Popular Songs-")
        for v in range(0, len(listVivaldi)):
            print(f'{v+1}. {listVivaldi[v]}')
        return listVivaldi
    elif cS == 9:
        print("Most Popular Songs-")
        for d in range(0, len(listDebussy)):
            print(f'{d+1}. {listDebussy[d]}')
        return listDebussy
    elif cS == 10:
        print("Most Popular Songs-")
        for h in range(0, len(listHandel)):
            print(f'{h+1}. {listHandel[h]}')
        return listHandel

#########################################################################################

def listClassicalSelection(currentClassicalList, playlist, recentlyPlayed, musicNotes):
    import time
    cASelection = int(input("Please choose the number of a song you would like to listen to: "))

    if cASelection in range(0, len(currentClassicalList)):
        print(f'{currentClassicalList[cASelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        cASelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if cASelection2 == "Save":
            playlist.append(currentClassicalList[cASelection -1])
            recentlyPlayed.append(currentClassicalList[cASelection -1])
        else:
            recentlyPlayed.append(currentClassicalList[cASelection -1])
    else:
        print("Invalid Choice.")
        
#########################################################################################
    
def printRapArtistsSongs(rS, listEminem, listLamar, listCole, listLucas, listDrake, listX, listScott, listRocky, listLogic, listMalone):
    print("\n" * 5)
    rS = int(input("Please choose a number to select an artist: "))
    if rS == 1:
        print("Most Popular Songs-")
        for e in range(0, len(listEminem)):
            print(f'{e+1}. {listEminem[e]}')
        return listEminem
    elif rS == 2:
        print("Most Popular Songs-")
        for la in range(0, len(listLamar)):
            print(f'{la+1}. {listLamar[la]}')
        return listLamar
    elif rS == 3:
        print("Most Popular Songs-")
        for c in range(0, len(listCole)):
            print(f'{c+1}. {listCole[c]}')
        return listCole
    elif rS == 4:
        print("Most Popular Songs-")
        for lu in range(0, len(listLucas)):
            print(f'{lu+1}. {listLucas[lu]}')
        return listLucas
    elif rS == 5:
        print("Most Popular Songs-")
        for d in range(0, len(listDrake)):
            print(f'{d+1}. {listDrake[d]}')
        return listDrake
    elif rS == 6:
        print("Most Popular Songs-")
        for x in range(0, len(listX)):
            print(f'{x+1}. {listX[x]}')
        return listX
    elif rS == 7:
        print("Most Popular Songs-")
        for s in range(0, len(listScott)):
            print(f'{s+1}. {listScott[s]}')
        return listScott
    elif rS == 8:
        print("Most Popular Songs-")
        for r in range(0, len(listRocky)):
            print(f'{r+1}. {listRocky[r]}')
        return listRocky
    elif rS == 9:
        print("Most Popular Songs-")
        for lo in range(0, len(listLogic)):
            print(f'{lo+1}. {listLogic[lo]}')
        return listLogic
    elif rS == 10:
        print("Most Popular Songs-")
        for m in range(0, len(listMalone)):
            print(f'{m+1}. {listMalone[m]}')
        return listMalone

#########################################################################################

def listRapSelection(currentRapList, playlist, recentlyPlayed, musicNotes):
    import time
    rASelection = int(input("Please choose the number of a song you would like to listen to: "))

    if rASelection in range(0, len(currentRapList)):
        print(f'{currentRapList[rASelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        rASelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if rASelection2 == "Save":
            playlist.append(currentRapList[rASelection -1])
            recentlyPlayed.append(currentRapList[rASelection -1])
        else:
            recentlyPlayed.append(currentRapList[rASelection -1])
            
    else:
        print("Invalid Choice.")
        
#########################################################################################
    
def printSoulArtistsSongs(sS, listTemptations, listJackson5, listBrown, listGaye, listKnight, listWonder, listCharles, listRedding, listGreen, listEarthWindFire):
    print("\n" * 5)
    sS = int(input("Please choose a number to select an artist: "))
    if sS == 1:
        print("Most Popular Songs-")
        for t in range(0, len(listTemptations)):
            print(f'{t+1}. {listTemptations[t]}')
        return listTemptations
    elif sS == 2:
        print("Most Popular Songs-")
        for j in range(0, len(listJackson5)):
            print(f'{j+1}. {listJackson5[j]}')
        return listJackson5
    elif sS == 3:
        print("Most Popular Songs-")
        for b in range(0, len(listBrown)):
            print(f'{b+1}. {listBrown[b]}')
        return listBrown
    elif sS == 4:
        print("Most Popular Songs-")
        for ga in range(0, len(listGaye)):
            print(f'{ga+1}. {listGaye[ga]}')
        return listGaye
    elif sS == 5:
        print("Most Popular Songs-")
        for k in range(0, len(listKnight)):
            print(f'{k+1}. {listKnight[k]}')
        return listKnight
    elif sS == 6:
        print("Most Popular Songs-")
        for w in range(0, len(listWonder)):
            print(f'{w+1}. {listWonder[w]}')
        return listWonder
    elif sS == 7:
        print("Most Popular Songs-")
        for c in range(0, len(listCharles)):
            print(f'{c+1}. {listCharles[c]}')
        return listCharles
    elif sS == 8:
        print("Most Popular Songs-")
        for r in range(0, len(listRedding)):
            print(f'{r+1}. {listRedding[r]}')
        return listRedding
    elif sS == 9:
        print("Most Popular Songs-")
        for gr in range(0, len(listGreen)):
            print(f'{gr+1}. {listGreen[gr]}')
        return listGreen
    elif sS == 10:
        print("Most Popular Songs-")
        for e in range(0, len(listEarthWindFire)):
            print(f'{e+1}. {listEarthWindFire[e]}')
        return listEarthWindFire

#########################################################################################

def listSoulSelection(currentSoulList, playlist, recentlyPlayed, musicNotes):
    import time
    sASelection = int(input("Please choose the number of a song you would like to listen to: "))

    if sASelection in range(0, len(currentSoulList)):
        print(f'{currentSoulList[sASelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        sASelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if sASelection2 == "Save":
            playlist.append(currentSoulList[sASelection -1])
            recentlyPlayed.append(currentSoulList[sASelection -1])
        else:
            recentlyPlayed.append(currentSoulList[sASelection -1])
                                  
                
    else:
        print("Invalid Choice.")
        
#########################################################################################
    
def printPopArtistsSongs(popS, listGrande, listVanderWaal, listEilish, listHalsey, listKhalid, listGomez, listDragons, listMars, listGaga, listPerry):
    print("\n" * 5)
    popS = int(input("Please choose a number to select an artist: "))
    if popS == 1:
        print("Most Popular Songs-")
        for gr in range(0, len(listGrande)):
            print(f'{gr+1}. {listGrande[gr]}')
        return listGrande
    elif popS == 2:
        print("Most Popular Songs-")
        for v in range(0, len(listVanderWaal)):
            print(f'{v+1}. {listVanderWaal[v]}')
        return listVanderWaal
    elif popS == 3:
        print("Most Popular Songs-")
        for e in range(0, len(listEilish)):
            print(f'{e+1}. {listEilish[e]}')
        return listEilish
    elif popS == 4:
        print("Most Popular Songs-")
        for h in range(0, len(listHalsey)):
            print(f'{h+1}. {listHalsey[h]}')
        return listHalsey
    elif popS == 5:
        print("Most Popular Songs-")
        for k in range(0, len(listKhalid)):
            print(f'{k+1}. {listKhalid[k]}')
        return listKhalid
    elif popS == 6:
        print("Most Popular Songs-")
        for go in range(0, len(listGomez)):
            print(f'{go+1}. {listGomez[go]}')
        return listGomez
    elif popS == 7:
        print("Most Popular Songs-")
        for d in range(0, len(listDragons)):
            print(f'{d+1}. {listDragons[d]}')
        return listDragons
    elif popS == 8:
        print("Most Popular Songs-")
        for m in range(0, len(listMars)):
            print(f'{m+1}. {listMars[m]}')
        return listMars
    elif popS == 9:
        print("Most Popular Songs-")
        for ga in range(0, len(listGaga)):
            print(f'{ga+1}. {listGaga[ga]}')
        return listGaga
    elif popS == 10:
        print("Most Popular Songs-")
        for p in range(0, len(listPerry)):
            print(f'{p+1}. {listPerry[p]}')
        return listPerry

#########################################################################################

def listPopSelection(currentPopList, playlist, recentlyPlayed, musicNotes):
    import time
    popASelection = int(input("Please choose the number of a song you would like to listen to: "))

    if popASelection in range(0, len(currentPopList)):
        print(f'{currentPopList[popASelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        popASelection2 = input("If you would like to save this podcast, please type 'Save'. If you do not want to save this podcast, please hit the 'Enter' or 'Return' key: ")
        if popASelection2 == "Save":
            playlist.append(currentPopList[popASelection -1])
            recentlyPlayed.append(currentPopList[popASelection -1])
        else:
            recentlyPlayed.append(currentPopList[popASelection -1])
            
    else:
        print("Invalid Choice.")

#########################################################################################
        
def visitPlaylist(playlist):
    print("Currently in your playlist-")
    for vP in range(0, len(playlist)):
            print(f'{vP+1}. {playlist[vP]}')

#########################################################################################

def playlistSongSelection(playlist, musicNotes):
    import time
    pSongSelection = int(input("Please choose the number of a song you would like to listen to: "))

    if pSongSelection in range(0, len(playlist)):
        print(f'{playlist[pSongSelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)

        pSongSelection2 = input("If you would like to listen to another song, please hit the 'Enter' or 'Return' key: ")
    else:
        print("Invalid Choice.")

#########################################################################################
        
def visitPodcasts(savedPodcasts):
    print("Currently in your saved podcasts-")
    for vP in range(0, len(savedPodcasts)):
            print(f'{vP+1}. {savedPodcasts[vP]}')

#########################################################################################

def savedPodcastSelection(savedPodcasts, talking):
    import time
    sPSelection = int(input("Please choose the number of a podcast you would like to listen to: "))

    if sPSelection in range(0, len(savedPodcasts)):
        print(f'{savedPodcasts[sPSelection -1]} is playing: ')
        time.sleep(0.25)
        for talk in talking * 6:
            print(talk * 10)
            time.sleep(0.15)

        sPSelection2 = input("If you would like to listen to another podcast, please hit the 'Enter' or 'Return' key: ")
    else:
        print("Invalid Choice.")

#########################################################################################
        
def visitRecentlyPlayed(recentlyPlayed):
    print("Recently played songs-")
    for vR in range(0, len(recentlyPlayed)):
        print(f'{vR+1}. {recentlyPlayed[vR]}')

#########################################################################################

def recentlyPlayedSelection(recentlyPlayed, musicNotes):
    import time
    rPSelection = int(input("Please choose the number of a song you would like to listen to: "))

    if rPSelection in range(0, len(recentlyPlayed)):
        print(f'{recentlyPlayed[rPSelection -1]} is playing: ')
        time.sleep(0.25)
        for music in musicNotes * 6:
            print(music * 10)
            time.sleep(0.15)
        
        rPSelection2 = input("If you would like to listen to another song, please hit the 'Enter' or 'Return' key: ")
    else:
        print("Invalid Choice.")

#########################################################################################

def getData(filename):

    newList = []
    
    fileIn = open(filename)

    for line in fileIn:
        newList.append(line.strip())

    fileIn.close()

    return newList

#########################################################################################            
    
def main():
    import time
    mainMenu = ["Home", "Recommended", "Library", "End"]
    homeMenu = ["Popular Albums", "Browse", "Podcasts"]
    songGenres = ["Classical", "Rap", "Soul", "Pop"]
    podcastGenres = ["Music", "Educational", "Fictional", "Sports"]
    recommendedGenres = ["Classical", "Soul", "Rap", "Pop"]
    libraryMenu = ["Recently Played", "Artists", "Playlists", "Podcasts"]
    artistGenres = ["Classical", "Rap", "Soul", "Pop"]
    playlist = []
    savedPodcasts = []
    recentlyPlayed = []
    musicNotes = ["|♩♪♫♬|"]
    talking = ["... "]
    
                   
    listClassical = getData("Classical.txt")
    listRap = getData("Rap.txt")
    listSoul = getData("Soul.txt")
    listPop = getData("Pop.txt")
    listTopAlbums = getData("Top 5 Albums.txt")
    listRClassical = getData("RClassical.txt")
    listRPop = getData("RPop.txt")
    listRRap = getData("RRap.txt")
    listRSoul = getData("RSoul.txt")
    listMusicPod = getData("Music Podcasts.txt")
    listEducationalPod = getData("Educational Podcasts.txt")
    listFictionalPod = getData("Fictional Podcasts.txt")
    listSportsPod = getData("Sports Podcasts.txt")
    listFreeSpiritSongs = getData("Free Spirit Songs.txt")
    listEilishAlbumSongs = getData("Eilish Album.txt")
    listVictoryLapSongs = getData("Victory Lap Songs.txt")
    listThankUNextSongs = getData("Thank U Next Songs.txt")
    listDeathRaceForLoveSongs = getData("Death Race For Love Songs.txt")
    listVictoryLapSongs = getData("Victory Lap Songs.txt")
    listClassicalArtists = getData("Popular Classical Artists.txt")
    listRapArtists = getData("Popular Rap Artists.txt")
    listSoulArtists = getData("Popular Soul Artists.txt")
    listPopArtists = getData("Popular Pop Artists.txt")
    listBach = getData("Bach.txt")
    listBeethoven = getData("Beethoven.txt")
    listMozart = getData("Mozart.txt")
    listTchaikovsky = getData("Tchaikovsky.txt")
    listChopin = getData("Chopin.txt")
    listBrahms = getData("Brahms.txt")
    listSchubert = getData("Schubert.txt")
    listVivaldi = getData("Vivaldi.txt")
    listDebussy = getData("Debussy.txt")
    listHandel = getData("Handel.txt")
    listEminem = getData("Eminem.txt")
    listLamar = getData("Lamar.txt")
    listCole = getData("Cole.txt")
    listLucas = getData("Lucas.txt")
    listDrake = getData("Drake.txt")
    listX = getData("X.txt")
    listScott = getData("Scott.txt")
    listRocky = getData("Rocky.txt")
    listLogic = getData("Logic.txt")
    listMalone = getData("Malone.txt")
    listTemptations = getData("Temptations.txt")
    listJackson5 = getData("Jackson 5.txt")
    listBrown = getData("Brown.txt")
    listGaye = getData("Gaye.txt")
    listKnight = getData("Knight.txt")
    listWonder = getData("Wonder.txt")
    listCharles = getData("Charles.txt")
    listRedding = getData("Redding.txt")
    listGreen = getData("Green.txt")
    listEarthWindFire = getData("EarthWindFire.txt")
    listGrande = getData("Grande.txt")
    listVanderWaal = getData("VanderWaal.txt")
    listEilish = getData("Eilish.txt")
    listHalsey = getData("Halsey.txt")
    listKhalid = getData("Khalid.txt")
    listGomez = getData("Gomez.txt")
    listDragons = getData("Dragons.txt")
    listMars = getData("Mars.txt")
    listGaga = getData("Gaga.txt")
    listPerry = getData("Perry.txt")
    
    s = menuSelection(mainMenu)
    while s != mainMenu:

        if s == "Home":
            homeChoice = homeSelection(homeMenu)
            #while homeChoice != homeMenu:

            if homeChoice == "Popular Albums":
                popularAlbumChoice = popularAlbums(listTopAlbums)
                currentPopularAlbumList = printAlbumSongs(popularAlbumChoice, listFreeSpiritSongs, listEilishAlbumSongs, listThankUNextSongs, listDeathRaceForLoveSongs, listVictoryLapSongs)
                popularAlbumSelection(currentPopularAlbumList, playlist, recentlyPlayed, musicNotes)
                print("Currently in your playlist-", playlist)
                time.sleep(1)
                
            elif homeChoice == "Browse":
                genre = browse(songGenres)
                currentList = printListSongs(genre, listClassical, listRap, listSoul, listPop)
                listSongsSelection(currentList, playlist, recentlyPlayed, musicNotes)
                print("Currently in your playlist-", playlist)
                time.sleep(1)
                
            elif homeChoice == "Podcasts":
                podGenre = podcasts(podcastGenres)
                currentPodList = printListPodcasts(podGenre, listMusicPod, listEducationalPod, listFictionalPod, listSportsPod)
                listPodcastsSelection(currentPodList, savedPodcasts, talking)
                print("Currently in your saved podcasts-", savedPodcasts)
                time.sleep(1)
                    
                    
        elif s == "Recommended":
            rGenre = recommended(recommendedGenres)
            currentRecommendedList = printListRecommendedSongs(rGenre, listRClassical, listRRap, listRSoul, listRPop)
            listRecommendedSongsSelection(currentRecommendedList, playlist, recentlyPlayed, musicNotes)
            print("Currently in your playlist-", playlist)
            time.sleep(1)
            
        elif s == "Library":
            libraryChoice = library(libraryMenu)
##            while libraryChoice != libraryMenu:

            if libraryChoice == "Recently Played":
                visitRecentlyPlayed(recentlyPlayed)
                recentlyPlayedSelection(recentlyPlayed, musicNotes)

            elif libraryChoice == "Artists":
                aGenre = artists(artistGenres)
                if aGenre == 'Classical':
                    cS = printListArtists(aGenre, listClassicalArtists, listRapArtists, listSoulArtists, listPopArtists)
                    currentClassicalList = printClassicalArtistsSongs(cS, listBach, listBeethoven, listMozart, listTchaikovsky, listChopin, listBrahms, listSchubert, listVivaldi, listDebussy, listHandel)
                    listClassicalSelection(currentClassicalList, playlist, recentlyPlayed, musicNotes)
                elif aGenre == 'Rap':
                    rS = printListArtists(aGenre, listClassicalArtists, listRapArtists, listSoulArtists, listPopArtists)
                    currentRapList = printRapArtistsSongs(rS, listEminem, listLamar, listCole, listLucas, listDrake, listX, listScott, listRocky, listLogic, listMalone)
                    listRapSelection(currentRapList, playlist, recentlyPlayed, musicNotes)
                elif aGenre == 'Soul':
                    sS = printListArtists(aGenre, listClassicalArtists, listRapArtists, listSoulArtists, listPopArtists)
                    currentSoulList = printSoulArtistsSongs(sS, listTemptations, listJackson5, listBrown, listGaye, listKnight, listWonder, listCharles, listRedding, listGreen, listEarthWindFire)
                    listSoulSelection(currentSoulList, playlist, recentlyPlayed, musicNotes)
                elif aGenre == 'Pop':
                    popS = printListArtists(aGenre, listClassicalArtists, listRapArtists, listSoulArtists, listPopArtists)
                    currentPopList = printPopArtistsSongs(popS, listGrande, listVanderWaal, listEilish, listHalsey, listKhalid, listGomez, listDragons, listMars, listGaga, listPerry)
                    listPopSelection(currentPopList, playlist, recentlyPlayed, musicNotes)
                print("Currently in your playlist:", playlist)
                time.sleep(1)

            elif libraryChoice == "Playlists":
                visitPlaylist(playlist)
                playlistSongSelection(playlist, musicNotes)

            elif libraryChoice == "Podcasts":
                visitPodcasts(savedPodcasts)
                savedPodcastSelection(savedPodcasts, talking)

        elif s == "End":
            end()

        s = menuSelection(mainMenu)

main()
