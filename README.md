# Teste Técnico – Desenvolvedor Back-end

## Objetivo
Avaliar a capacidade do candidato de manipular dados, trabalhar com banco de dados e estruturar um código back-end simples e organizado.

---

## Instruções

### 1. Banco de Dados
- Crie um banco de dados MySQL chamado **Graos**
- Crie duas tabelas:
  - `tb_soja`
  - `tb_milho`

Ambas devem conter as seguintes colunas:
- `id` (inteiro, chave primária, auto incremento)
- `estado`
- `cidade`
- `compra`

> Fica a critério do candidato definir os tipos de dados adequados para cada coluna.

---

### 2. Leitura de dados
- Desenvolva um código em **Python** que:
  - Leia o arquivo **Grao.xlsx**
  - Utilize as abas:
    - `milho`
    - `soja`
  - Insira os dados lidos nas tabelas correspondentes:
    - Aba `milho` → `tb_milho`
    - Aba `soja` → `tb_soja`

---

### 3. Requisitos gerais
- Utilize **Pandas** para leitura e manipulação dos dados
- Utilize **MySQL** como banco de dados
- O código deve ser claro, organizado e funcional

---

## O que esperamos
- Python
- Pandas
- MySQL
- Um **passo a passo** explicando como rodar a aplicação localmente

---

## Critérios de avaliação
- Organização do código
- Clareza e legibilidade
- Boas práticas
- Tratamento básico de erros
- Estrutura da solução proposta

---

## Observações
- É permitido usar qualquer editor de código
- É permitido consultar a internet durante o teste

---

## Entrega

Envie sua solução em um arquivo **.zip** para **at@scotconsultoria.com.br** em até **10 dias corridos** após o recebimento do teste.

- **Assunto do e-mail:** `Teste Back-end – Seu Nome`
- **Nome do arquivo:** `teste-backend-seu-nome.zip`

> ⚠️ **Não** faça fork nem Pull Request deste repositório.

### O .zip deve conter
- Todo o código-fonte do projeto
- Um arquivo **`README.md` na raiz** com o passo a passo para executar o projeto, incluindo:
  - Pré-requisitos e versões utilizadas
  - Instalação de dependências
  - Configuração necessária
  - Comando(s) para executar (ex.: `python main.py`)
- Arquivo `requirements.txt` com as dependências Python
- Script SQL de criação do banco e das tabelas (ex.: `database.sql`)

### Não inclua no .zip
- Pastas de dependências (`node_modules`, `vendor`, `venv`, `.venv`, `__pycache__`)
- Arquivos com senhas reais (`.env`); envie um `.env.example` no lugar

> Se o arquivo passar de 20 MB, envie um link de download (Google Drive, WeTransfer etc.).

---

Em caso de dúvidas, envie um e-mail para **at@scotconsultoria.com.br**

**Boa sorte! 🚀**
