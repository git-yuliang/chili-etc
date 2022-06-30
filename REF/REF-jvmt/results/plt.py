import matplotlib.pyplot as plt
from astropy.io import fits

fig, axes = plt.subplots(4,1,figsize=(20/2,40/2))
axes = axes.ravel()

inpu1=fits.open('mg_ell_17_30020_blue.fits')
inpu2=fits.open('mg_ell_18_30020_blue.fits')
inpu3=fits.open('mg_ell_19_30020_blue.fits')

axes[1].set_title('elliptical galaxy',fontsize=15)
axes[1].plot(inpu1[1].data,inpu1[10].data,color='skyblue')
axes[1].plot(inpu1[1].data,inpu1[3].data,color='b')
axes[1].plot(inpu2[1].data,inpu2[10].data,color='greenyellow')
axes[1].plot(inpu2[1].data,inpu2[3].data,color='g')
axes[1].plot(inpu3[1].data,inpu3[10].data,color='lightsalmon')
axes[1].plot(inpu3[1].data,inpu3[3].data,color='r')
axes[1].set_ylim(0.)
axes[1].set_xlabel('$\lambda$ (A)',fontsize=12)
axes[1].set_ylabel('$10^{-17}$ erg/s/A/$cm^{2}$',fontsize=12)

inpu1=fits.open('mg_agn_17_30020_blue.fits')
inpu2=fits.open('mg_agn_18_30020_blue.fits')
inpu3=fits.open('mg_agn_19_30020_blue.fits')

axes[0].set_title('type I AGN',fontsize=15)
axes[0].plot(inpu1[1].data,inpu1[10].data,color='skyblue')
axes[0].plot(inpu1[1].data,inpu1[3].data,color='b')
axes[0].plot(inpu2[1].data,inpu2[10].data,color='greenyellow')
axes[0].plot(inpu2[1].data,inpu2[3].data,color='g')
axes[0].plot(inpu3[1].data,inpu3[10].data,color='lightsalmon')
axes[0].plot(inpu3[1].data,inpu3[3].data,color='r')
axes[0].set_ylim(0.)
axes[0].set_xlabel('$\lambda$ (A)',fontsize=12)
axes[0].set_ylabel('$10^{-17}$ erg/s/A/$cm^{2}$',fontsize=12)

inpu1=fits.open('mg_weak_17_30020_blue.fits')
inpu2=fits.open('mg_weak_18_30020_blue.fits')
inpu3=fits.open('mg_weak_19_30020_blue.fits')
i=2
axes[i].set_title('weak emission line galaxy',fontsize=15)
axes[i].plot(inpu1[1].data,inpu1[10].data,color='skyblue')
axes[i].plot(inpu1[1].data,inpu1[3].data,color='b')
axes[i].plot(inpu2[1].data,inpu2[10].data,color='greenyellow')
axes[i].plot(inpu2[1].data,inpu2[3].data,color='g')
axes[i].plot(inpu3[1].data,inpu3[10].data,color='lightsalmon')
axes[i].plot(inpu3[1].data,inpu3[3].data,color='r')
axes[i].set_ylim(0.)
axes[i].set_xlabel('$\lambda$ (A)',fontsize=12)
axes[i].set_ylabel('$10^{-17}$ erg/s/A/$cm^{2}$',fontsize=12)

inpu1=fits.open('mg_strong_17_30020_blue.fits')
inpu2=fits.open('mg_strong_18_30020_blue.fits')
inpu3=fits.open('mg_strong_19_30020_blue.fits')
i=3
axes[i].set_title('strong emission line galaxy',fontsize=15)
axes[i].plot(inpu1[1].data,inpu1[10].data,color='skyblue')
axes[i].plot(inpu1[1].data,inpu1[3].data,color='b')
axes[i].plot(inpu2[1].data,inpu2[10].data,color='greenyellow')
axes[i].plot(inpu2[1].data,inpu2[3].data,color='g')
axes[i].plot(inpu3[1].data,inpu3[10].data,color='lightsalmon')
axes[i].plot(inpu3[1].data,inpu3[3].data,color='r')
axes[i].set_ylim(0.)
axes[i].set_xlabel('$\lambda$ (A)',fontsize=12)
axes[i].set_ylabel('$10^{-17}$ erg/s/A/$cm^{2}$',fontsize=12)

axes[i].text(4000,600,'target mag =17 mag/$arcsec^{2}$',color='b',fontsize=15)
axes[i].text(4000,500,'target mag =18 mag/$arcsec^{2}$',color='g',fontsize=15)
axes[i].text(4000,400,'target mag =19 mag/$arcsec^{2}$',color='r',fontsize=15)

plt.show()