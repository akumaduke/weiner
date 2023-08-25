
list_depart = [ "cuba," "canada", "france", "etats-unis", "republique dominicaine"]

list_destination = [" haiti, jamaique, porto rico, "]

list_route = []




def main():
    #User a bay Depart epi Destination
    get_info()

    #Program nan chèche tout Route disponib ki gen format sa: Depart -> X

    get_route( depart, destination)

    #if route
    display_route()







def get_info() -> dict:
    info= dict()
    info["depart"]= input("vous partez d'ou ?")
    info["destination"] = input(" vous souhaitez aller ou? ")

    return info


def get_route( X: str, Y : str ):


