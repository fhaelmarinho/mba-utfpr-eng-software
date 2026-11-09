# Guia Prático: Configuração do Ambiente Virtual e Execução de Testes

Este guia apresenta o passo a passo completo para configurar o ambiente Python no Linux/Ubuntu, instalar as dependências necessárias e executar os testes automatizados com relatórios de cobertura.

---

## Passo 1: Abrir o Terminal e Acessar a Pasta do Projeto
Navegue até o diretório onde os arquivos do seu projeto (`identifier.py`, `test_identifier.py`, `requirements.txt`) estão salvos:

```bash
cd ~/Documentos/Workspace/identifier
```

---

## Passo 2: Criar o Ambiente Virtual (`venv`)
Como sistemas modernos (Ubuntu/Debian) bloqueiam instalações globais via `pip` (erro `externally-managed-environment`), criamos um ambiente isolado:

```bash
python3 -m venv venv
```
*(Isso criará uma pasta chamada `venv` dentro do diretório do seu projeto).*

---

## Passo 3: Ativar o Ambiente Virtual
Ative o ambiente criado para que os comandos de instalação e execução utilizem o interpretador isolado:

```bash
source venv/bin/activate
```
> **Nota visual:** Quando o ambiente estiver ativo, o seu terminal exibirá o prefixo `(venv)` no início da linha de comandos.

---

## Passo 4: Instalar as Dependências do Projeto
Com o ambiente virtual ativo, instale as ferramentas de teste (`pytest` e `pytest-cov`) utilizando o arquivo de dependências:

```bash
pip install -r requirements.txt
```
*(Ou instale manualmente com: `pip install pytest pytest-cov`)*

---

## Passo 5: Executar os Testes com Relatório de Cobertura
Execute o `pytest` para rodar todos os casos de teste e gerar o relatório detalhado de cobertura em formato de terminal e HTML:

```bash
pytest --cov=identifier --cov-report=html --cov-report=term
```

---

## Passo 6: Desativar o Ambiente Virtual (Opcional)
Quando terminar de trabalhar e quiser sair do ambiente virtual isolado, basta digitar:

```bash
deactivate
```