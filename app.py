import os

import doctor
import data

@doctor.timer
def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("\n"*100)
  print(f"The {doctor.style.announce}Doctor{doctor.style.end} was called...\n")

  table = doctor.table(
    data.numerical((20, 8)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  print(table.get_result())

  # doctor.build(outfile="report", quick=False)

  #

  figure = doctor.plot(
    data = {
      "data1": data.timeseries_singleton(points=20, places=4),
      "data2": data.timeseries_singleton(points=34, places=4),
    },
    options = {
      "xlabel": "Horizontal",
      "ylabel": "Vertical",
      "caption": "Test caption",
      "shade": {
        "fill": "solid",
        "colour": "ONSpink",
        "regions": [[9, 27], [50, "end"]]
      }
    }
  )

  figure.export_data(out_path="graphs/test")

  doctor.log.comment("[This is] not [a] test...")

if __name__ == "__main__":
  main()
