
# Sorteio 

Script em Python para realizar sorteio de vagas a partir de uma lista de e-mails, com confirmação manual se o ganhador está presente na live.

---

## Pré-requisitos

* Python 3.x
* Biblioteca `pandas`

Instale o pandas (se não tiver):

```bash
pip3 install pandas
```

---

## Arquivo de entrada

Crie um arquivo chamado **`contatos.csv`** no mesmo diretório do script.

Formato do arquivo:

```csv
Email
email1@dominio.com
email2@dominio.com
email3@dominio.com
```

> O arquivo deve conter **apenas uma coluna chamada `Email`**.

---

## Configurações

No início do arquivo Python você pode ajustar:

```python
Slots = 2        # Quantidade de vagas a sortear
File = "contatos.csv"  # Nome do arquivo CSV
```

---

## Como executar

No terminal:

```bash
python3 sorteio.py
```

---

## Como funciona o sorteio

1. O script sorteia um e-mail aleatoriamente.
2. O e-mail é exibido **mascarado** no terminal.
3. O sistema pergunta se o ganhador está na live:

   * Digite **`s`** para confirmar a vaga.
   * Digite **`n`** para descartar e sortear outro.
4. O processo se repete até preencher todas as vagas definidas em `Slots`.
5. Um mesmo e-mail **não pode ganhar duas vezes**.

---

## Observações

* O script utiliza cores no terminal (ANSI), recomendado usar no **Ubuntu/Linux**.
* Se os e-mails acabarem antes de preencher todas as vagas, o sorteio é encerrado automaticamente.

