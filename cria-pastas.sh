#!/bin/bash

# Cria a estrutura de diretórios
mkdir -p mtg-reports/app/{models,routes,templates/analysis,static/{css,js},utils,analysis}
mkdir -p mtg-reports/migrations mtg-reports/tests

# Cria os arquivos dentro de app/
touch mtg-reports/app/__init__.py
touch mtg-reports/app/models/{__init__.py,player.py,event.py,deck.py,report.py,match.py,game.py}
touch mtg-reports/app/routes/{__init__.py,main_routes.py,api_routes.py}
touch mtg-reports/app/templates/{base.html,index.html,report_form.html}
touch mtg-reports/app/templates/analysis/{player.html,deck.html}
touch mtg-reports/app/static/css/.gitkeep mtg-reports/app/static/js/.gitkeep
touch mtg-reports/app/utils/{__init__.py,json_parser.py,text_parser.py}
touch mtg-reports/app/analysis/{__init__.py,deck_analysis.py,player_analysis.py,match_analysis.py}

# Cria os arquivos na raiz do projeto
touch mtg-reports/config.py mtg-reports/run.py mtg-reports/requirements.txt

# Cria os arquivos de teste
touch mtg-reports/tests/{__init__.py,test_models.py}

echo "Estrutura de pastas e arquivos criada com sucesso!"