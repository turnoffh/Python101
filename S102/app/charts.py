import matplotlib.pyplot as plt #Alias

def generate_bar_chart(labels, values):
  
  fig, ax = plt.subplots()#Figura y coordenadas
  ax.bar(labels, values)
  plt.show()
  #plt.savefig(f'./imgs/{name}.png')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  generate_bar_chart(labels, values)