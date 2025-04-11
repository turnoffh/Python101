'''while True:
  print("se ejecutó")

counter = 0
while counter < 10:
  counter += 1
  print(counter)
  
  #
    #continue
    #pass
    #break
    #exit()
    #return
    #raise
    #assert
    #del
    #exec
    #eval
    #execfile
    #exit
    #help
    #id
    #input
    #isinstance
    #issubclass

counter = 0
while counter < 20:
  counter += 1
  print(counter)
  if counter == 15:
    break #rompe el ciclo
'''
counter = 0
while counter < 20:
  counter += 1
  
  if counter < 15:
    continue #salta a la siguiente iteracion
  print(counter)