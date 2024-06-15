import json

project = "Ahumada Atención Médica - Médico"

# Carregar os dados do arquivo JSON
with open('collection.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Função para processar as suites recursivamente e gerar linhas de tabela
def process_suites(suites):
    html = ""
    for suite in suites:
        html += f"""
        <h2>{suite['title']}</h2>
        <p><em>{suite['description'] or "Sem descrição"}</em></p>
        <table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Type</th>
                    <th>Severity</th>
                    <th>Automation</th>
                    <th>Status</th>
                    <th>Is Flaky</th>
                </tr>
            </thead>
            <tbody>
        """
        for case in suite['cases']:
            html += f"""
            <tr>
                <td>{case['title']}</td>
                <td>{case['layer'] or "None"}</td>
                <td>{case['severity']}</td>
                <td>{case['automation']}</td>
                <td>{case['status']}</td>
                <td>{case['is_flaky']}</td>
            </tr>
            """
        if suite['suites']:
            html += process_suites(suite['suites'])
        html += "</tbody></table>"
    return html

# Criar o relatório HTML
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Cases Report - {project}</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        h2 {{ margin-top: 20px; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Test Cases Report - {project}</h1>
    {process_suites(data['suites'])}
</body>
</html>
"""

# Escrever o relatório HTML em um arquivo
with open('report_qase.html', 'w', encoding='utf-8') as file:
    file.write(html)

print("Relatório HTML criado com sucesso!")
