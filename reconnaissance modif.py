from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    im_b = image.binarisation(S)
    im_loc = im_b.localisation()
    simMax=0.0
    for i in range(len(liste_modeles)):
        newH=liste_modeles[i].H
        newW=liste_modeles[i].W
        im_res = im_loc.resizee(newH, newW)   
        taux_Sim = im_res.similitude(liste_modeles[i])         
        if taux_Sim > simMax :
            simMax=im_res.similitude(liste_modeles[i])   
            iMax = i
    return iMax

