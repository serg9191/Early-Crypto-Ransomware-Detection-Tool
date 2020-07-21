import json
import os

from matplotlib import pyplot as plt

def main():
  # The number of figure - i.e. number of files to display
  figure_counter = 1
  # Iterate through all files of specified directory
  for root, dirs, files in os.walk("entropy_archive"):
    for file in files:
      entropies = []
      avg = 0
      # read file
      with open(os.path.join(root, file)) as json_f:
        # load file in json object
        data = json.load(json_f)
        # Before and after encryption average entropy variable differs,
        # therefore, validation needed to find correct
        # variable name. The outcome of evaluation
        # is stored in variable aes_file
        aes_file = "aes" in file
        for d in data:
          if aes_file:
            if  'avg_entropy_after_encryption' in d:
              avg = d['avg_entropy_after_encryption']
          if not aes_file:
            if 'avg_entropy' in d:
              avg = d['avg_entropy']
          if not 'entropy' in d:
            continue
          entropies.append(d['entropy'])
        # Initialise size of av_list list to the size of
        # entropies list.
        avg_list = [None] * len(entropies)
        # Populate entire list with average entropy value.
        # This produces diagonal line in the graph to show average
        for i in range(0, len(entropies)):
          avg_list[i] = (avg)
        plot_on_graph(figure_counter, file, entropies, avg_list)
        figure_counter += 1
  plt.show()

# This function produces the graph from the given args
def plot_on_graph(figure_nr, title, entropies, avg_list):
  plt.figure(figure_nr)
  plt.ylabel("Entropy")
  plt.xlabel("Number of Files")
  plt.title(title)
  plt.plot(entropies)
  plt.plot(avg_list)  

if __name__== "__main__":
  main()  