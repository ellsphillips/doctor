import pandas as pd

from ...utils.tex import TeXDefaults as tex
from ...utils.cli import *

class PlotBuilder():
  """
  """

  tab_space = " "*4
  double_backslash = "\\\\"

  colours = [
    "ons-blue",
    "ons-green",
    "ons-pink",
    "ons-orange",
    "ons-yellow",
  ]

  def __init__(
    self,
    data: dict = None,
    options: dict = None
  ):
    self.data = data
    self.options = options

    if data is None:
      log.warning("I'm not much good without data, you know...")

  def pluck(opts: dict, *args):
    return [opts[arg] for arg in args]

  def id_data(self) -> list:
    return [(name, series) for name, series in self.data.items()]

  def build_dataframe(self) -> pd.DataFrame:
    time_points = max([len(ts[1]) for ts in self.id_data()])
    log.comment(f"Built dataframe of dimension [{len(self.data), time_points}]")

    output = pd.DataFrame(
      dict(
        [(k, pd.Series(v)) for k,v in self.data.items()]
      )
    )
    output["time"] = range(time_points)

    return output[["time"] + [c for c in output.columns if c != "time" ] ]

  def cycle_colours(func):
    def wrapper(*args, **kwargs):
      wrapper.colour_index += 1
      return func(*args, **kwargs)
    wrapper.colour_index = 0
    return wrapper

  @cycle_colours
  def add_plot(self):
    args = [
      self.colours[(self.add_plot.colour_index - 1) % len(self.colours)],
      "thick",
      "mark=none"
    ] 

    elements = [
      "\\addplot[",
      ",\n".join([f"{self.tab_space}{arg}" for arg in args]),
		  f"] table[x=time, y={list(self.data)[self.add_plot.colour_index - 1]}]",
      "{src/graphs/timeseries.dat};\n"
    ]

    return "\n".join(e for e in elements)
    
  #

  def env_begin(self) -> str:
    return "\\begin{doctor-plot}\n"

  def env_end(self) -> str:
    return "\\end{doctor-plot}\n"

  def env_body(self) -> str:
    pass

  def get_result(self) -> str:
    """
    Compile the complete string representation of a LaTeX table.
    """
    elements = [
      self.env_begin,
      self.env_body,
      self.env_end,
    ]
    result = "\n".join([item for item in elements if item])
    trailing_newline = "\n"
    result += trailing_newline
    return result
  
  def export_data(self, out_path: str) -> None:
    destination = f"{tex.options['document']['path']}src/{out_path}.csv"
    dataframe = self.build_dataframe()
    dataframe.to_csv(destination, index=False, encoding='utf-8')
    log.output(destination)
