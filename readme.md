[doctor-build]: https://i.imgur.com/8iuEgjZ.gif

# Doctor

An automated documentation assitant built in Python and TeX for procedural, data-driven reporting.

Doctor aims to simplify the reporting build process through an intuitive Python API and customisable LaTeX class to responsively markup Pythonic data objects to professionally typeset documents.

## Installation

Clone the repo

```
git clone https://github.com/ellsphillips/doctor.git

cd doctor
```

Install the requirements

```
pip install -r requirements.txt
```

## Usage

To get started, import `doctor` into your python script. You have immediate access to 2 classes, `table` and `plot`- feed Doctor a dataframe object and watch it build beautiful `LaTeX` code. Returned as a literal, you can pass this result to any of the available methods to further build on or output to your `LaTeX` directory.

```python
  import doctor

  table = doctor.table(
    data.numerical((8, 4)),
    column_format=[0.1, 0.2, 0.3, 0.4],
    caption="Example table generated by Python",
    short_caption="Shorter caption for TOC",
    label="tabledemo"
  )

  print(table.get_result())

  doctor.build(outfile="report")
```

![Build your PDF with Doctor][doctor-build]

## Outputs

[](#outputs)

You can inspect the result through the console with `doctor.get_result()`, or use the provided `write_to()` method to output your LaTeX result to a relative directory path.

```python
  table = doctor.table(...)

  doctor.write_to("path/to/file")
```

This generates a new file if the name space is undefined, otherwise overwrites the content of the file. Doctor assumes you organise your LaTeX code through `input{}` calls.

Reference the [architecture below](#architecture) for an example.

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

## Architecture

[](#architecture)

```shell
  doctor/
  ├── data
  │   ├── __init__.py
  │   ├── data.py
  ├── demo
  │   ├── src
  │   │   └── ...
  │   ├── doctor.cls
  │   ├── main.tex
  │   ├── report.pdf
  ├── doctor
  │   ├── builder
  │   │   ├── plot
  │   │   └── table
  │   ├── utils
  │   │   ├── __init__.py
  │   │   ├── cli.py
  │   │   └── tex.py
  │   ├── __init__.py
  │   ├── doctor.py
  └── app.py
```
