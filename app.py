import os
import pandas as pd
import numpy as np

import doctor
import data

def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\n"*100)
  print("The \033[1m\033[93mDoctor\033[0m was called...\n")

  table = doctor.table(
    data.numerical((8, 4)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  print(table.get_result())
  

if __name__ == "__main__":
  import time
  start = time.perf_counter()
  main()
  end = time.perf_counter()
  elapsed = end - start
  print(f'Finished in \033[1m\033[93m{elapsed:.02f}s\033[0m')
