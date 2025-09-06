import matplotlib.pyplot as plt  #Alias


def generate_bar_chart(labels, values):

  fig, ax = plt.subplots()  #Figura y coordenadas
  ax.bar(labels, values)
  plt.show() #para verlo en pantalla
  plt.savefig('./imgs/barchart.png')


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)  #Piechart toca asignarle asi los labels
  ax.axis('equal')  #Para que se vea como un circulo
  plt.show() #para verlo en pantalla
  plt.savefig('./imgs/piechart.png')


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
