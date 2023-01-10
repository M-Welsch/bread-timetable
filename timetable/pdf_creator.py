from datetime import datetime
from typing import List

import pandas as pd
from latex import build_pdf
from jinja2 import Environment

TEMPLATE = r"""
\documentclass{article}
\usepackage{geometry}
 \geometry{
 a4paper,
 total={170mm,257mm},
 left=20mm,
 top=20mm,
 }
\title{Backplan}
\author{Maximilian Welsch}
\date{\today}
\begin{document}
  \maketitle
  \section{Rezepte}
    \begin{itemize}
        {% for recipe in recipes %}
            \item {{recipe}}
        {% endfor %}
    \end{itemize}
    
  \newpage
  \section{Zeitplan}
  
    {% for timestamp, recipe, instruction, ingredients in timesteps %}
    \subsection*{ {{ timestamp }}: {{ recipe }}}
    {{ instruction }}{% if ingredients %}
        \begin{itemize}
        {% for ingredient in ingredients %}
            \item {{ingredient}}
        {% endfor %}
        \end{itemize}
    {% endif %}
    {% endfor %}
    
  \newpage
  \section{Zutaten}
    \begin{itemize}
    
      {% for name, amount in ingredients.items() %}
        \item {{amount}}{{name}}
      {% endfor %}
      
    \end{itemize}
\end{document}
"""


def _create_recipe_overview(baking_plan) -> list:
    recipes = []
    for recipe in baking_plan:
        name = recipe.recipe_name.value.name
        url = recipe.recipe_name.value.url
        recipes.append(name + ": " + url)
    return recipes


def _create_steps(timetable: pd.DataFrame) -> List[List[str]]:
    steps = []
    for index, row in timetable.sort_values("time").iterrows():
        if not row.instruction:
            continue
        steptime: datetime = row.time
        step = [steptime.strftime('%d.%m.%Y %H:%M:%S'), row.recipe, row.instruction]
        if row.ingredients:
            step.append(row.ingredients.split(', '))
        else:
            step.append("")
        steps.append(step)
    return steps


def create_pdf(baking_plan: list, timetable: pd.DataFrame, ingredients: dict):
    doc = Environment().from_string(TEMPLATE).render(
        recipes=_create_recipe_overview(baking_plan),
        ingredients=ingredients,
        timesteps=_create_steps(timetable)
    )
    pdf = build_pdf(doc)
    pdf.save_to("Backplan.pdf")
