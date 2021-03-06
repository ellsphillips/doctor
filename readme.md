[repo-card-api]: https://github-readme-stats.vercel.app/api/pin/?username=ellsphillips&theme=react&repo=doctor&card_width=100%
[repo-card]: https://github.com/ellsphillips/doctor
[doctor-build]: https://i.imgur.com/8iuEgjZ.gif
[doctor-logo]: https://raw.githubusercontent.com/ellsphillips/doctor/master/docs/img/doctor-logo.svg

# Doctor <img align="right" width="200" height="200" title="Doctor" src="https://raw.githubusercontent.com/ellsphillips/doctor/master/docs/img/doctor-logo.svg">

An automated documentation assistant built in Python and TeX for procedural, data-driven reporting.

Doctor simplifies the reporting build process through an intuitive Python API and customisable LaTeX class to responsively markup Pythonic data objects to professionally typeset lightweight documents.

---

## Installation

Install the package directly through GitHub.

```bash
$ pip install git+https://github.com/ellsphillips/doctor
```

Doctor will be available for installation through PyPI in future releases.

## Usage

Once installed, you readily have access to Doctor's `table` and `plot` builder methods. Basic examples of each are listed here, but for more complex example usage and a complete list of options from the API, head over to our documentation.

```python
  import doctor as dr

  def main() -> None:

    tabular = dr.table(
        dr.data.table(
            [
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
                dr.data.text.lorem(10),
            ]
        )
    )

    dr.render(tabular)

    figure = dr.plot(
        "line",
        [
            dr.data.series.brownian(),
            dr.data.series.brownian(),
            dr.data.series.brownian(),
        ],
        options={
            "plot type": "ybar",
            "data source": "src/plots/example.dat",
            "caption": "Demonstration of the doctor-plot environment",
            "label": "example-plot",
        },
    )

    dr.render(figure)

    dr.build(outfile="report")
```

Define each of your LaTeX figures with a new builder method. If your IDE doesn't provide intellisense, please see the manual for reference.

![Build your PDF with Doctor][doctor-build]

## Project structure

Doctor makes no assumption to how you structure you LaTeX project - you specify output paths per figure build. Output code is written to individual `.tex` and data files, allowing you to optionally load LaTeX code with `\input{}` for streamlined, maintainable workflows.

The example project structure given as demo in this repo has architecture:

[](#architecture)

```tree
  .
  ????????? data
  ???   ????????? __init__.py
  ???   ????????? data.py
  ????????? doctor
  ???   ????????? builder
  ???   ???   ????????? plot
  ???   ???   ????????? table
  ???   ????????? utils
  ???   ???   ????????? __init__.py
  ???   ???   ????????? cli.py
  ???   ???   ????????? tex.py
  ???   ????????? __init__.py
  ???   ????????? doctor.py
  ????????? document
  ???   ????????? src
  ???   ???   ????????? ...
  ???   ????????? doctor.cls
  ???   ????????? main.tex
  ???   ????????? report.pdf
  ????????? app.py
```

## Outputs

[](#outputs)

Doctor returns your custom LaTeX syntax as string objects. View these directly with `doctor.get_result()` or save to file through the builder options.

```latex
  \begin{doctor-table}{4}
    {% Column format
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
      >{{\raggedleft\arraybackslash\hsize=\hsize}}X
    }{% Column headers
      \bfseries Numbers &
      \bfseries More numbers &
      \bfseries Text &
      \bfseries Mash \\
    }{% Caption
      Example table generated by Python
    }{% Label
      test
    }
    25 & 43 &       Lorem & iswdufvbouwesdbnvg \\
    82 & 71 &       ipsum &                abc \\
    23 & 52 &       dolor &            sdvcsdv \\
    82 & 85 &         sit &       sdvdssdvdvvn \\
    93 & 63 &        amet &          yumyumyum \\
    83 & 35 & consectetur &               wqoe \\
    87 & 51 &  adipiscing &            qphjpgh \\
    79 & 41 &        elit &    owperjgpowegjwj \\
    84 & 88 &   Curabitur &        wepogjwpeog \\
    60 &  7 &         nec &                 oi \\
  \end{doctor-table}
```

```latex
  \begin{doctor-plot}[%
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
      very thick,
    ] table [x=index, y=values, meta=values]%
    {\doctordatasource};
  \end{doctor-plot}
```

## Citing Doctor

If you use Doctor in your research or as your reproting assistant, please use the following BibTeX entry:

```BibTeX
@Misc{EP2022Doctor,
  author =       {Elliott Phillips},
  title =        {Doctor - A documentation assistant to simplify the reporting of data-oriented, beautiful, lightweight documents},
  howpublished = {Github},
  year =         {2022},
  url =          {https://github.com/ellsphillips/doctor}
}
```

<!-- [![Doctor summary][repo-card-api]](https://github.com/ellsphillips/doctor) -->
