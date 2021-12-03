from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np
path_to_assets = '../assets/'

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")
		

    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    
    def binarisation(self, S):
        # creation d'une image vide
        im_bin = Image()
        
        # affectation a l'image im_bin d'un tableau de pixels de meme taille
        # que self dont les intensites, de type uint8 (8bits non signes),
        # sont mises a 0
        im_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        # TODO: boucle imbriquees pour parcourir tous les pixels de l'image im_bin
        # et calculer l'image binaire
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j] >= S:
                    im_bin.pixels[i][j] = 255
                else:
                    im_bin.pixels[i][j] = 0
        return im_bin

    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        lim_gauche = self.W
        lim_haut = self.H
        lim_droite = 0
        lim_bas = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.pixels[i][j] == 0 and i < lim_gauche:
                    lim_gauche = i
                if self.pixels[i][j] == 0 and i > lim_droite:
                    lim_droite = i
                if self.pixels[i][j] == 0 and j < lim_haut:
                    lim_haut = j
                if self.pixels[i][j] == 0 and j > lim_bas:
                    lim_bas = j
        im = Image()
        im.set_pixels(self.pixels[lim_gauche:lim_droite,lim_haut:lim_bas])
        return im        
            

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resizee(self, new_H, new_W):                    
        pixels_resized = resize(self.pixels, (new_H,new_W), 0)
        im_resized = np.uint8(pixels_resized*255)
        im = Image()
        im.set_pixels(im_resized)
        return im

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        similitude = 0
        if self.H != im.H or self.W != im.W:
            print('Les images n ont pas la meme taille')
        else:
            for i in range(self.H):
                for j in range(self.W):
                    if self.pixels[i][j] == im.pixels[i][j]:
                        similitude += 1
        taux = similitude/(self.H*self.W)
        return taux
      

if __name__ == '__main__':
    image = Image()
    image.load(path_to_assets + 'test2.JPG')
    image_localisee = image_binarisee.localisation()
    print(image.similitude(image_localisee))
    