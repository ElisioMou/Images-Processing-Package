from images-processing-elisio.utils import io, plot 
from images-processing_elisio.processing import match, mutation

image1 = io.read_image('E:/Projetos Git/Criando-um-Pacote-de-Processamento-de-Imagens-com-Python/Images-Processing-Package/images/img1.jpg')
image2 = io.read_image('E:/Projetos Git/Criando-um-Pacote-de-Processamento-de-Imagens-com-Python/Images-Processing-Package/images/img2.jpg')

plot.plot_image(image1)
plot.plot_image(image2)