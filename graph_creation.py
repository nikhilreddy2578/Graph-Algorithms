#Dictionary Creation
import pandas as pd
from unidecode import unidecode



class TitleDictionary:

    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df["primaryTitle"] = self.df["primaryTitle"].apply(unidecode)
        self.title_dict = self._create_title_dict()
        self.profession_dict = self._create_profession_dict()

    def _create_title_dict(self):
        # Dictionary structure:
            # key: nconst
            # value: list of movie_names(primaryTitle's) actors/directors involved in
        #Create a dictionary in the format:
        #{nconst:[movie_names actors/directors involved in], here the actor/director is determined by id: nconst}
        #example dictionary looks like:
        # {'nm6551690': ['The Dreaded Hong Kong SneezeThe Great Bank Robbery',
        #   'The Reluctant RobotThe Royal Foil',
        #   'Theres No Business Like Snow Business'],
        #
        #   'nm8002705': ['The Awful Awakening of Claudius Brodequin',
        #   'The Dreaded Arrival of Captain Tardivaux',
        #   'The Glorious Triumph of Barthelemey Piechut',
        #   'The Magnificent Idea of Barthelemey Piechut the Mayor',
        #   'The Painful Infliction of Nicholas the Beadle',
        #   'The Scandalous Outcome of a Night of Destruction',
        #   'The Spirited Protest of Justine Pulet',
        #   'The Triumphant Inauguration of a Municipal Amenity']}
        title_dict = {}

        for _, row in self.df.iterrows():
            nconst = row['nconst']
            primary_title = row['primaryTitle']

            if nconst in title_dict:
                title_dict[nconst].append(primary_title)
            else:
                title_dict[nconst] = [primary_title]

        return title_dict

    def _create_profession_dict(self):
        profession_dict = {}
        for index, row in self.df.iterrows():
            nconst = row['nconst']
            primary_name = row['primaryName']
            primary_profession = row['primaryProfession']
            name_suffix = '_d' if primary_profession == 'director' else '_a'
            name = primary_name + name_suffix
            profession_dict[nconst] = name
        return profession_dict

#Graph Network Creation
class MovieNetwork:
    def __init__(self, name_movie_dict, nconst_ar_dr):
        self.graph = {} #graph dictionary initialization
        self.name_movie_dict = name_movie_dict #name_movie_dict is nothing but "title_dict" dictionary refer to above example in TitleDictionary.
        self.nconst_ar_dr = nconst_ar_dr #it is "profession_dict" dictionary refer to above example in TitleDictionary.


    def add_node(self, node):
        #write code to add node to the graph (dictionary data-structure)
        pass

    def add_edge(self, node1, node2, nconst_ar_dr, weight=1):
        #node 1, node 2: nconst id's
        #nconst_ar_dr is nothing but "profession_dict" dictionary refer to above example in TitleDictionary.
        #weight is number of common movie titles exists in node1 and node2
        #Before adding Edge weights you must follow the below Instructions:
            #1. consider only the node1->node2 connection or edge, only if node1 and node2 have more than 2 movies in common.
            #2. Let node1="actor" and node2="director" then node1->node2 edge should not be taken implies {actor:{director:6}} must not be taken.
                # But node2->node1 should be taken implies {director:{actor:6}} must be taken.
            #3. if node1 and node2 are assigned with both actors or directors then bi-directional edge must be added implies
                #{actor1:{actor2:4}} and {actor2:{actor1:4}} or {director1:{director2:7}} and {director2:{director1:7}} both ways are true
                #and must consider in dictionary.
        #write code to add edge to the graph implies add weight between node1 and node 2
        #Example weight assignment looks like:
        # {'nm1172995': {'nm0962553': 7}} here the weight 7 is nothing but the number of common
        #movies between two persons either actor/director (nm1172995 and nm0962553)
        pass

    def create_graph(self):
        #By following the above conditions create a graph (use only dictionary datastructure: self.graph)
        #example graph looks like:
          # {'nm0962553': {'nm8630849': 3,
          #     'nm1172995': 7,
          #     'nm8742830': 16,
          #     'nm6225202': 4,
          #     'nm4366294': 4},
          #    'nm8630849': {},
          #    'nm1172995': {'nm0962553': 7},
          #    'nm8742830': {'nm0962553': 16},
          #    'nm6225202': {}}

        for nconst, primaryTitles in self.name_movie_dict.items():
            if nconst not in self.graph:
                self.graph[nconst] = {}
            for nc, titles in self.name_movie_dict.items():
                if nconst == nc:
                    continue
                titles1 = set(primaryTitles)
                titles2 = set(titles)
                common  = titles1.intersection(titles2)

                if (len(common) > 2):
                    prof1 = self.nconst_ar_dr[nconst]
                    prof2 = self.nconst_ar_dr[nc]
                    if (prof1[-1] == prof2[-1]):
                        self.graph[nconst][nc] = len(common)
                        if nc not in self.graph:
                            self.graph[nc] = {}
                        self.graph[nc][nconst] = len(common)

                    if (prof1.endswith("_d") and prof2.endswith("_a")):
                        self.graph[nconst][nc] = len(common)

        return self.graph
