class Bar():
  """
  """
  def __init__(
    self,
    data: dict = None,
    options: dict = None
  ) -> None:
    pass

  @staticmethod
  def _template() -> None:
    """
    \begin{doctor-bar}[%
      plot type={ybar},
      data source={src/plots/bar.dat},
      somebool=false,
      caption={Hello, world!},
      label={bar-test},
      xmin=0,
      xmax=12,
      ymin=0,
      ymax=35,
    ]%
      \addplot+[%
        nodes near coords,
        point meta=explicit symbolic,
        mark=none,
        ons-blue,
        very thick
      ] table [x=index, y=values, meta=values]%
      {\doctordatasource};
    \end{doctor-bar}
    """
    pass
