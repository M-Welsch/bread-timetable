from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd
from latex import build_pdf
from jinja2 import Environment

TEMPLATE_MD = r"""
# Rezepte

{% for recipe in recipes %}
- {{recipe}}
{% endfor %}

# Zeitplan
{% for timestep in timesteps %}
## { {{ timestep.timestamp }}: {{ timestep.recipe }}}

{{ timestep.instruction }} {% if timestep.ingredients %}
{% for ingredient in timestep.ingredients %}
- {{ingredient}}
{% endfor %}
{% endif %}

{% endfor %}

# Zutaten
{% for name, amount in ingredients.items() %}
- {{'{0:0.1f}'.format(amount)}}{{name}}
{% endfor %}
"""

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
  
    {% for timestep in timesteps %}
        \subsection*{ {{ timestep.timestamp }}: {{ timestep.recipe }}}
        {{ timestep.instruction }}{% if timestep.ingredients %}
            \begin{itemize}
            {% for ingredient in timestep.ingredients %}
                \item {{ingredient}}
            {% endfor %}
            \end{itemize}
        {% endif %}
    {% endfor %}
    
  \newpage
  \section{Zutaten}
    \begin{itemize}
    
      {% for name, amount in ingredients.items() %}
        \item {{'{0:0.1f}'.format(amount)}}{{name}}
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
        step = {
            "timestamp": row.time.strftime('%d.%m.%Y %H:%M:%S'),
            "recipe": row.recipe,
            "instruction": row.instruction,
            "ingredients": row.ingredients.split(',') if row.ingredients else []
        }
        steps.append(step)
    return steps


def create_pdf(baking_plan: list, timetable: pd.DataFrame, ingredients: dict):
    doc = Environment().from_string(TEMPLATE).render(
        recipes=_create_recipe_overview(baking_plan),
        ingredients=ingredients,
        timesteps=_create_steps(timetable)
    )
    pdf = build_pdf(doc)
    today = datetime.now().strftime('%Y-%m-%d')
    pdf.save_to(f"{today}_Backplan.pdf")


def create_md(baking_plan: list, timetable: pd.DataFrame, ingredients: dict, savedir: Path):
    doc = Environment().from_string(TEMPLATE_MD).render(
        recipes=_create_recipe_overview(baking_plan),
        ingredients=ingredients,
        timesteps=_create_steps(timetable)
    )
    with open(savedir/f"{datetime.now().strftime('%Y-%d-%m')} Backsession") as f:
        f.write(doc)
