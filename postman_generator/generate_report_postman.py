import json

# Carregar os dados do arquivo JSON
with open('results.json', 'r') as file:
    data = json.load(file)

# Criar o relatório HTML
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe de Pruebas</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
    </style>
</head>
<body>
    <h1>Informe de Pruebas - {data['name']}</h1>
    <p>ID: {data['id']}</p>
    <p>Timestamp: {data['timestamp']}</p>
    <p>Total Pass: {data['totalPass']}</p>
    <p>Total Fail: {data['totalFail']}</p>

    <table>
        <thead>
            <tr>
                <th>Caso de prueba</th>
                <th>URL</th>
                <th>Status</th>
                <th>Tiempo (ms)</th>
                <th>Validaciones</th>
            </tr>
        </thead>
        <tbody>
"""

# Adicionar resultados dos testes ao relatório HTML
for result in data['results']:
    status = "Pass" if all(result['tests'].values()) else "Fail"
    status_class = "pass" if status == "Pass" else "fail"
    tests_html = "".join([f"<li class='{ 'pass' if passed else 'fail' }'>{test}: {'Passou' if passed else 'Falhou'}</li>" for test, passed in result['tests'].items()])

    html += f"""
    <tr>
        <td>{result['name']}</td>
        <td><a href="{result['url']}">{result['url']}</a></td>
        <td class="{status_class}">{status}</td>
        <td>{result['time']}</td>
        <td><ul>{tests_html}</ul></td>
    </tr>
    """

# Fechar as tags HTML
html += """
        </tbody>
    </table>
</body>
</html>
"""

# Escrever o relatório HTML em um arquivo
with open('report_postman.html', 'w') as file:
    file.write(html)

print("Relatório HTML criado com sucesso!")
