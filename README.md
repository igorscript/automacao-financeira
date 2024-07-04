# Automação Financeira

## Descrição
Este projeto automatiza a obtenção de dados históricos de ações financeiras, calcula valores relevantes e envia um relatório por e-mail. O objetivo é facilitar o processo de análise e comunicação de resultados para gestores financeiros ou investidores.

## Tecnologias/Ferramentas Utilizadas
- Python 3.12.4
- Bibliotecas:
  - `pyautogui` (v0.9.54)
  - `pyperclip` (v1.9.0)
  - `webbrowser` (biblioteca padrão)
  - `time` (biblioteca padrão)
  - `yfinance` (v0.2.40)

## Instalação
1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/igorscript/automacao-financeira.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd automacao-financeira
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install pyautogui yfinance
    ```

## Uso

1. Execute o script Python:

    ```bash
    python automacao-financeira.py
    ```

2. Insira os dados solicitados pelo programa:
    - Código da ação (ex: AAPL para Apple)
    - Data inicial no formato aaaa-mm-dd (ex: 2023-01-01)
    - Data final no formato aaaa-mm-dd (ex: 2023-12-31)
    - Endereço de e-mail do destinatário 

    **Nota**: O programa obterá os dados históricos da ação, calculará a cotação máxima, mínima e média, e enviará um relatório com esses dados para o e-mail fornecido.

## Recursos
- Obtenção de dados históricos de ações.
- Cálculo da cotação máxima, mínima e média.
- Automação do envio de relatórios por e-mail.

## Contribuindo
1. Faça um fork do projeto.
2. Crie uma nova branch para sua feature ou correção:

    ```bash
    git checkout -b minha-feature
    ```

3. Commit suas alterações:

    ```bash
    git commit -m 'Adiciona minha nova feature'
    ```

4. Envie para o repositório remoto:

    ```bash
    git push origin minha-feature
    ```

5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a Licença MIT.

## Contato
- LinkedIn: [Igor Martins](https://www.linkedin.com/in/igorcoder/)
- E-mail: igorcoder@hotmail.com
