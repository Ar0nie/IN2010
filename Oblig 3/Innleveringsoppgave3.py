from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

class Movie:

    def __init__(self, ttID, tittel, rating):
        self._ID = ttID
        self._tittel = tittel
        self._rating = rating
        self._actors = []
    
    def add(self, actor):
        if actor not in self._actors:
            self._actors.append(actor)

    def hentRating(self):
        return self._rating
    
    def __repr__(self):
        return self._ID + ":" + self._tittel + "-->"

class Actor :

    def __init__(self, nmID, navn):
        self._ID = nmID
        self._navn = navn
        self._filmer = []
    
    def add(self, film) :
        if film not in self._filmer:
            self._filmer.append(film)
    
    def __repr__(self) :
        return self._ID + ":" + self._navn + "-->"

    def hentFilmer(self):
        return self._filmer

movieDict = {}
actorDict = {}
graph = {}
actorValueDict = {}

def byggGrafen(movies, actors) :

    m = open(movies, 'r', encoding="utf-8")

    for line in m:
        arg = line.split("\t")
        ttID = arg[0]
        tittel = arg[1]
        rating = float(arg[2])
        nyMovie = Movie(ttID, tittel, rating)
        movieDict[str(ttID)] = nyMovie
    

    m.close()

    e = open(actors, 'r', encoding="utf-8")

    for a in e:
        arg = a.strip().split("\t")
        nmID = arg[0]
        navn = arg[1]
        nyActor = Actor(nmID, navn)
        actorDict[nmID] = nyActor
        actorValueDict[nmID] = nyActor

        for i in arg[2:]:
                if i in movieDict:
                    nok = movieDict.get(i)
                    graph.setdefault(i, [])       
                    nyActor.add(movieDict.get(i))
                    graph[i].append(nyActor)        

        filmer = nyActor.hentFilmer()
        actorNok = nyActor._ID
        actorDict.setdefault(actorNok, filmer)
        actorDict[actorNok] = filmer     

    #Her legges de filmene inn, der ingen skuespillere vi kjenner til har spilt i filmen.
    for key in movieDict:
        if key not in graph:
            graph[key] = None
    

    graph.update(actorDict)
    #dict pa formen G = {actor: [film...], film: [actor...]}
    
    e.close()

    V = set()
    E = defaultdict(set)
    w = dict()

    for key in graph:
        V.add(key)
        verdier = graph.get(key)
   
        if verdier != None:
                for verdi in verdier:
                        E[key].add(verdi)
                        E[verdi].add(key)

                        if isinstance(verdi, Movie):
                            w[(key, verdi)] = float(movieDict[verdi._ID]._rating)
                            w[(verdi, key)] = float(movieDict[verdi._ID]._rating)                     

    return V, E, w

def sort(array) :
    if len(array) > 1:
        venstre_arr = array[:len(array)//2]
        hoyre_arr = array[len(array)//2:]
    
        #Rekursivt kall for aa slice hoyre og venstre del av arrayet til der har len 1
        sort(venstre_arr)
        sort(hoyre_arr)

        #Merge
        i = 0 #Venstre array index
        j = 0 #Hoyre array index
        g = 0 #global merged array index
        
        while i < len(venstre_arr) and j < len(hoyre_arr) :
            if venstre_arr[i] < hoyre_arr[j]:
                array[g] = venstre_arr[i]
                i += 1
            else :
                array[g] = hoyre_arr[j]
                j += 1
            
            g += 1
        
        while i < len(venstre_arr):
            array[g] = venstre_arr[i]
            i += 1
            g += 1
        
        while j < len(hoyre_arr):
            array[g] = hoyre_arr[j]
            j += 1
            g += 1

def bfs_komponeter(G, s):
    _, E, _ = G
    visited = set([s])
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        result.append(v)
        for u in E[v]:
            if u not in visited:
                visited.add(u)
                queue.append(u)
    index = 0
    for e in result:
        if isinstance(e, str):
            ...
        else:
            result[index] = e._ID
            ...
        index += 1

    return result

def komponenter(G):

    visited = set()
    utskrift = []

    for g in G[0]:
        if g not in visited:
            result = bfs_komponeter(G, g)
            visited.update(result)
            noder = len(result)
            utskrift.append(noder)
    
    sort(utskrift)

    tallSomSjekkes = utskrift[0]
    forekomster = -1
    indexSomSjekkes = 0

    for element in utskrift:
        forekomster += 1
        if element != tallSomSjekkes:
            print("Det finnes " + str(forekomster) + " komponenter med storrelse " + str(tallSomSjekkes) + ".")
            tallSomSjekkes = utskrift[indexSomSjekkes]
            indexSomSjekkes += 1
            forekomster = 0
            if indexSomSjekkes == len(utskrift):
                forekomster += 1
                print("Det finnes " + str(forekomster) + " komponenter med storrelse " + str(tallSomSjekkes) + ".")
            
        elif element == tallSomSjekkes: 
            indexSomSjekkes += 1
    

def bfs_shortest_path_between(G, s, t):
    parents = bfs_shortest_paths_from(G, s)
    v = t
    path = []

    if t not in parents:
        return path

    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]


def bfs_shortest_paths_from(G,s):
    _, E, _ = G
    parents = {s : None}
    queue = deque([s])
    result = []

    while queue:
        v = deque.popleft(queue)
        for u in E[v]:
            if u not in parents:
                parents[u] = v
                queue.append(u)
    
    return parents

def utskrift(liste):
    utskrift = []
    vekt = 0
    
    for i in liste:
        if isinstance(i, str):
            verdi = actorValueDict[i] 
            utskrift.append(verdi)
        else : 
            vekt += (10 - i._rating)
            utskrift.append(i)

    utskrift.append("Vekt: " + str(vekt))
    return utskrift

def shortest_paths_from(G, s):
    V, E, w = G
    Q = [(0, 0, s)]
    D = defaultdict(lambda: float('inf'))
    parents = {s : None}
    D[s] = 0

    i = 0
    while Q:
        cost, _, v = heappop(Q)
        for u in E[v]:
            c = cost + 10 - w[(v, u)]
            if c < D[u]:
                D[u] = c
                i += 1
                heappush(Q, (c ,i,u))
                parents[u] = v 

    return parents

def dijkstra_shortest_path_between(G, s, t):
    parents = shortest_paths_from(G, s)
    v = t
    path = []

    if t not in parents:
        return path

    while v:
        path.append(v)
        v = parents[v]
    return path[::-1]


movies = 'movies.tsv'
actors = 'actors.tsv'

G = byggGrafen(movies, actors)

print("Oppgave 1")
print()
print("Antallet noder i grafen: " + str(len(G[0])))
print("Antallet kanter i grafen: " + str(len(G[1])//2))
print()

print("Oppgave 2")
print()
print("Donald Glover")
donald = bfs_shortest_path_between(G, "nm2255973","nm0000460")
print(utskrift(donald))
print()

print("Scarlett Johansen")
scarlett = bfs_shortest_path_between(G, "nm0424060","nm0000243")
print(utskrift(scarlett))
print()

print("Carrie Coon")
carrie = bfs_shortest_path_between(G, "nm4689420","nm0000365")
print(utskrift(carrie))
print()

print("Christian Bale")
christian = bfs_shortest_path_between(G, "nm0000288","nm0001401")
print(utskrift(christian))
print()

print("Atle Antonsen")
atle = bfs_shortest_path_between(G, "nm0031483","nm0931324")
print(utskrift(atle))
print()

print("Oppgave 3")
print()
print("Donald Glover")
donald = dijkstra_shortest_path_between(G, "nm2255973","nm0000460")
print(utskrift(donald))
print()

print("Scarlett Johansen")
scarlett = dijkstra_shortest_path_between(G, "nm0424060","nm0000243")
print(utskrift(scarlett))
print()

print("Carrie Coon")
carrie = dijkstra_shortest_path_between(G, "nm4689420","nm0000365")
print(utskrift(carrie))
print()

print("Christian Bale")
christian = dijkstra_shortest_path_between(G, "nm0000288","nm0001401")
print(utskrift(christian))
print()

print("Atle Antonsen")
atle = dijkstra_shortest_path_between(G, "nm0031483","nm0931324")
print(utskrift(atle))
print()

print("Oppgave 4")
print()
komponenter(G)