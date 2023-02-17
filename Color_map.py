from matplotlib import pyplot as plt, image as mimg
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

img = mimg.imread(r'C:\Users\Gopal\Pictures\wallaper\608476.jpg')
lum_img = img[:, :, 0]

plt.imshow(lum_img, cmap=plt.cm.CMRmap)
''' cmap="hot","Blues",
'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r',
, 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 
'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r'
, 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r'
, 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r',Reds
, 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 
'''
plt.axis('off')

plt.show()
